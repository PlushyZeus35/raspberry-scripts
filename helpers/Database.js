DatabaseHelper = {};
const EmailCtrl = require('./EmailCtrl');
const mariadb = require('mariadb');
const config = require('../config');

DatabaseHelper.openConnection = async function(){
    try{
        const pool = mariadb.createPool({
            host: config.database.personalApp.host, 
            user:config.database.personalApp.user, 
            password: config.database.personalApp.password,
            connectionLimit: 5
        });
        const conn = await pool.getConnection();
        await conn.query("use personalApp");
        return {pool: pool,conn: conn};
    }catch(error){
        EmailCtrl.sendErrorMail('Se ha producido un error en un script de servidor','Database.js',error.toString());
    }
}

DatabaseHelper.closeConnection = function(pool, conn){
    conn.end();
    pool.end();
}

DatabaseHelper.openPLConnection = async function(){
    try{
        const pool = mariadb.createPool({
            host: config.database.plusLearn.host, 
            user:config.database.plusLearn.user, 
            password: config.database.plusLearn.password,
            connectionLimit: 5
        });
        const conn = await pool.getConnection();
        await conn.query("use PlusLearn_DB");
        return {pool: pool,conn: conn};
    }catch(error){
        EmailCtrl.sendErrorMail('Se ha producido un error en un script de servidor','Database.js',error.toString());
    }
}

module.exports = DatabaseHelper;