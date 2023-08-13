const Database = require('./helpers/Database');

async function run(){
    const connectionData = await Database.openPLConnection();
    const conn = connectionData.conn;

    try{
        // Delete daily tasks
        const deletedRows = await conn.query("UPDATE passwordresets SET active = false WHERE active = true");
    }catch(error){

    }
    Database.closeConnection(connectionData.pool, conn);
}

run();