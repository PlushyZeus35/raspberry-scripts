const mariadb = require('mariadb');
const config = require('./config');
const { Spot } = require('@binance/connector')
const EmailCtrl = require('./helpers/EmailCtrl');

const pool = mariadb.createPool({
     host: config.database.host, 
     user:config.database.user, 
     password: config.database.password,
     connectionLimit: 5
});

async function getConnection(pool){
  try{
    conn = await pool.getConnection();
    await conn.query("use personalApp");
    return conn;
  }catch(error){
    EmailCtrl.sendEmail('plushyzeus35@gmail.com','Script error',error.toString(),[]);
  }
}

async function getBinanceKeys(conn){
  try{
    const rows = await conn.query("SELECT apikey, apisecret, userId FROM binances WHERE active = true");
    return rows;
  }catch(error){
    EmailCtrl.sendEmail('plushyzeus35@gmail.com','Script error',error.toString(),[]);
  }
}

function closeConnection(conn){
  conn.end();
  pool.end();
}

async function getBinanceAssets(apikey, apisecret){
  const client = new Spot(apikey, apisecret);
  const myAssets = [];
  // Get account information
  try{
    const assets = await client.account();
    for(let i=0; i<assets.data.balances.length; i++){
      if(parseFloat(assets.data.balances[i].free)>0 || parseFloat(assets.data.balances[i].locked)>0){
          myAssets.push(assets.data.balances[i]);
      }
    }
    return myAssets;
  }catch(error){
    EmailCtrl.sendEmail('plushyzeus35@gmail.com','Script error',error.toString(),[]);
    return [];
  }
}

async function setNewBinanceData(assets, userId, conn){
  try{
    for(let i=0; i<assets.length;i++){
      const value = parseFloat(assets[i].free) + parseFloat(assets[i].locked);
      const res = conn.query("INSERT INTO `criptodata` (`asset`, `value`, `fromSystem`, `createdAt`, `updatedAt`, `deletedAt`, `userId`) VALUES (?, ?, ?, ?, ?, ?, ?)", [assets[i].asset, value, 0, '2022-11-29 20:34:13', '2022-11-29 20:34:13', null, userId]);
      //console.log(res);
    }
  }catch(error){
    EmailCtrl.sendEmail('plushyzeus35@gmail.com','Script error',error.toString(),[]);
  }
}

async function run(){
  const conn = await getConnection(pool);
  const rows = await getBinanceKeys(conn);
  for(let i=0; i<rows.length;i++){
    const userAssets = await getBinanceAssets(rows[i].apikey, rows[i].apisecret);
    //console.log(userAssets);
    setNewBinanceData(userAssets, rows[i].userId, conn);
  }
  closeConnection(conn);
}

//getConnection(pool);
//asyncFunction();
run();

////////
/*const { Spot } = require('@binance/connector')

const apiKey = 'qPazU1QrtMr0psFO0sFa7kn0W3Wxw8gOg3cyfvKtFX2534f0rPpleAWvmOjfZWoC'
const apiSecret = 'tGHBnV5WHYLqoAfWRIkmvUiHOJrh4dKHMgyoT4edqGHJwX7u3jCvk6BuMiEaaQQD'
const client = new Spot(apiKey, apiSecret)

/* GET Index page. 
router.get('/', (req, res) => {
    const myAssets = [];
    // Get account information
    client.account()
        .then((response) => {
            client.logger.log(response.data.balances.length);
            //client.logger.log(response.data);
            for(let i=0; i<response.data.balances.length; i++){
                if(parseFloat(response.data.balances[i].free)>0 || parseFloat(response.data.balances[i].locked)>0){
                    myAssets.push(response.data.balances[i]);
                }
                client.logger.log(response.data.balances[i]);
            }
            console.log(myAssets);
        })
        .catch((error) => {
            console.error(error);
          });
    res.send('Hello World!');
})*/