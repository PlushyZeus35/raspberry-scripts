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
    const PersonalAppdumpFileName = './backups/' + 'PersonalApp' + fileDate + '.sql';
    const PlushLearndumpFileName = './backups/' + 'PlusLearn' + fileDate + '.sql';

    try{
        mysqldump({
            connection: {
                host: config.database.personalApp.host,
                user: config.database.personalApp.user,
                password: config.database.personalApp.password,
                database: config.database.personalApp.database,
            },
            dumpToFile: PersonalAppdumpFileName,
        });
        EmailCtrl.sendEmail('plushyzeus35@gmail.com','Database Backup','Database backup bro!',[{filename: fileDate+'.sql', path: PersonalAppdumpFileName}]);
    }catch(error){
        EmailCtrl.sendErrorMail('Se ha producido un error en un script de servidor','Backup.js',error.toString());
    }

    try{
        mysqldump({
            connection: {
                host: config.database.plusLearn.host,
                user: config.database.plusLearn.user,
                password: config.database.plusLearn.password,
                database: config.database.plusLearn.database,
            },
            dumpToFile: PlushLearndumpFileName,
        });
        EmailCtrl.sendEmail('plushyzeus35@gmail.com','Database Backup','Database backup bro!',[{filename: fileDate+'.sql', path: PlushLearndumpFileName}]);
    }catch(error){
        EmailCtrl.sendErrorMail('Se ha producido un error en un script de servidor','Backup.js',error.toString());
    }
}

module.exports = Backups;