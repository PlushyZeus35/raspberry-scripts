const DatabaseHelper = require('./helpers/Database');
const CriptoHelper = require('./helpers/Crypto');

async function run(){
	const connectionInfo = await DatabaseHelper.openConnection();
	const conn = connectionInfo.conn;
	const pool = connectionInfo.pool;
	const rows = await CriptoHelper.getBinanceKeys(conn);
	for(let i=0; i<rows.length;i++){
    	const userAssets = await CriptoHelper.getBinanceAssets(rows[i].apikey, rows[i].apisecret);
    	await CriptoHelper.setNewBinanceData(userAssets, rows[i].userId, conn);
  	}
  	DatabaseHelper.closeConnection(pool,conn);
}


run();
