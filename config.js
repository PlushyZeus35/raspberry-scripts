require('dotenv').config();

module.exports = {
    database: {
        personalApp: {
            password: process.env.PERSONALAPP_PASSWORD,
            database: process.env.PERSONALAPP_DATABASE,
            host: process.env.DATABASE_HOST,
            user: process.env.PERSONALAPP_USER,
            port: 3306
        },
        plusLearn: {
            password: process.env.PLUSLEARN_PASSWORD,
            database: process.env.PLUSLEARN_DATABASE,
            host: process.env.DATABASE_HOST,
            user: process.env.PLUSLEARN_USER,
            port: 3306
        }
    },
    email: {
        password: process.env.EMAIL_PASSWORD,
        receiver: 'plushyzeus35@gmail.com'
    }
}