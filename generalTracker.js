const Database = require('./helpers/Database');
const EmailCtrl = require('./helpers/EmailCtrl');

async function run(){
    const connectionData = await Database.openConnection();
    const conn = connectionData.conn;
    const users = await conn.query("SELECT id, username, email FROM users");
    //console.log(users)
    //console.log(users.length)
    for(let user of users){
        const activeBooks = await conn.query("SELECT id, title, initDate, predictedFinished, pages, predictedPPD FROM books WHERE reading = ? AND finished = ? and userId = ?", [true, false, user.id]);
        const weightData = await conn.query("SELECT id, createdAt FROM weights WHERE userId = ?", [user.id]);
        //console.log(activeBooks)
        const readGoals = booksToString(activeBooks)
        const weightGoals = weightToString(weightData)
        await EmailCtrl.sendTrackingMail('Tu resumen semanal', user.email, readGoals, weightGoals, []);
    }
    Database.closeConnection(connectionData.pool, conn);
}

function booksToString(books){
    const goal = [];
    if(books.length==0){
        goal.push('No tienes ningún libro en activo ahora mismo.')
        goal.push('¡Hay miles de libros esperandote! Entra en la aplicación e introduce el que quieras leer.')
        return goal;
    }
    for(let book of books){
        if(new Date(book.predictedFinished) < new Date()){
            let diff = parseInt((new Date() - new Date(book.predictedFinished))/(1000*60*60*24));
            goal.push('Tu libro actual ' + book.title + ' tiene un retraso de ' + diff + ' días en base a la predicción de fecha de fin.')
            goal.push('¡Ánimo! Recuerda que tienes un libro esperandote. Si en realidad ya has acabado este libro actualizalo en nuestra plataforma.')
            return goal;
        }else{
            let diff = parseInt((new Date() - new Date(book.initDate))/(1000*60*60*24));
            let pages = diff*book.predictedPPD;
            goal.push('Actualmente tienes activo el libro ' + book.title + ' y deberías ir alrededor de la página ' + pages);
            goal.push('Vas por buen camino, no olvides actualizar el progreso en la plataforma en caso de que lo termines o empieces otro.')
            return goal;
        }
    }
    return goal;
}

function weightToString(weightData){
    const goal = [];
    var limit = new Date();
    limit.setDate(limit.getDate() - 5);
    const thisWeekData = weightData.filter((i) => i.createdAt>limit)
    if(thisWeekData.length>0){
        goal.push('Esta semana has incorporado ' + thisWeekData.length + ' datos de peso.')
    }else{
        goal.push('¡No has incorporado ningún dato de peso este mes!')
    }
    goal.push('Recuerda que para mantener una buena monitorización de datos y controlar tu progreso se recomiendo introducir una media de dos valores al día.')
    return goal;
}

run();