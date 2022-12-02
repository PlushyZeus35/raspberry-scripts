const EmailCtrl = require('./EmailCtrl');
const { Spot } = require('@binance/connector');
const CriptoHelper = {};

CriptoHelper.getBinanceKeys = async function(conn){
    try{
        const rows = await conn.query("SELECT apikey, apisecret, userId FROM binances WHERE active = true");
        return rows;
    }catch(error){
        EmailCtrl.sendEmail('plushyzeus35@gmail.com','Script error',error.toString(),[]);
    }
}

CriptoHelper.getBinanceAssets = async function(apikey, apisecret){
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

CriptoHelper.setNewBinanceData = async function(assets, userId, conn){
    let date_time = new Date();
    let date = ("0" + date_time.getDate()).slice(-2);
    let month = ("0" + (date_time.getMonth() + 1)).slice(-2);
    let year = date_time.getFullYear();
    let hours = date_time.getHours();
    let minutes = date_time.getMinutes();
    let seconds = date_time.getSeconds();
    let finalDate = year + "-" + month + "-" + date + " " + hours + ":" + minutes + ":" + seconds;
    for(let j=0;j<assets.length;j++){
        try{
            const value = parseFloat(assets[j].free) + parseFloat(assets[j].locked);
            await conn.query("INSERT INTO `criptodata` (`asset`, `value`, `fromSystem`, `createdAt`, `updatedAt`, `deletedAt`, `userId`) VALUES (?, ?, ?, ?, ?, ?, ?)", [assets[j].asset, value, 0, finalDate, finalDate, null, userId]);
        }catch(error){
            EmailCtrl.sendEmail('plushyzeus35@gmail.com','Script error',error.toString(),[]);
        }
    }
}

module.exports = CriptoHelper;