const Database = require('./helpers/Database');

async function run(){
    const connectionData = await Database.openConnection();
    const conn = connectionData.conn;

    try{
        // Delete daily tasks
        const deletedRows = await conn.query("DELETE FROM tasks WHERE daily = ?", [true]);
    }catch(error){

    }
    Database.closeConnection(connectionData.pool, conn);
}

run();