const Database = require('./helpers/Database');
const EmailCtrl = require('./helpers/EmailCtrl');

const today = new Date();
const day = today.getDate();
const month = today.getMonth()+1;

async function run(){
    const connectionData = await Database.openConnection();
    const conn = connectionData.conn;
    const birthMap = [];
    try{
        const rows = await conn.query("SELECT name, userId FROM birthdays WHERE day = ? AND month = ?", [day,month]);
        for(let i=0; i<rows.length; i++){
            let find = false;
            for(let j=0; j<birthMap.length; j++){
                
                if(rows[i].userId == birthMap[j].user){
                    birthMap[j].names.push(rows[i].name);
                    find = true;
                }
                
            }
            if(!find){
                const user = await conn.query("SELECT email FROM users WHERE id = ?", [rows[i].userId]);
                birthMap.push({user: rows[i].userId, email:user[0].email, names: [rows[i].name]});
            }
        }
        for(let i=0; i<birthMap.length; i++){
            let names = '';
            for(let j=0; j<birthMap[i].names.length; j++){
                names += birthMap[i].names[j] + ' ';
            }
            EmailCtrl.sendBirthMail('¡Tienes cumpleaños que celebrar!',names,[]);
        }
        
    }catch(error){
        EmailCtrl.sendErrorMail('Se ha producido un error en un script de servidor','birthdayTracker.js',error.toString());
    }

    Database.closeConnection(connectionData.pool, conn);
}

run();