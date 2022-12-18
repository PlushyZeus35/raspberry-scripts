DatabaseHelper = {};
const EmailCtrl = require('./EmailCtrl');
const mariadb = require('mariadb');
const config = require('../config');

DatabaseHelper.openConnection = async function(){
    try{
        const pool = mariadb.createPool({
            host: config.database.host, 
            user:config.database.user, 
            password: config.database.password,
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

module.exports = DatabaseHelper;