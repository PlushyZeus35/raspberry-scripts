const Backups = {};
const mysqldump = require('mysqldump');
const config = require('../config');
const EmailCtrl = require('./EmailCtrl');

Backups.databaseDumps = async function(){
    let ts = Date.now();
    let date_time = new Date(ts);
    let date = date_time.getDate();
    let month = date_time.getMonth() + 1;
    let year = date_time.getFullYear();
    const fileDate = year + "-" + month + "-" + date;
    const dumpFileName = './backups/' + fileDate + '.sql';

    try{
        mysqldump({
            connection: {
                host: config.database.host,
                user: config.database.user,
                password: config.database.password,
                database: config.database.database,
            },
            dumpToFile: dumpFileName,
        });
        EmailCtrl.sendEmail('plushyzeus35@gmail.com','Database Backup','Database backup bro!',[{filename: fileDate+'.sql', path: dumpFileName}]);
    }catch(error){
        EmailCtrl.sendErrorMail('Se ha producido un error en un script de servidor','Backup.js',error.toString());
    }
}

module.exports = Backups;