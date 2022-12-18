module.exports = {
    database: {
        password: process.env.DATABASE_PASSWORD,
        database: process.env.DATABASE_DATABASE,
        host: process.env.DATABASE_HOST,
        user: process.env.DATABASE_USER,
        port: 3306
    },
    email: {
        password: process.env.EMAIL_PASSWORD,
        receiver: process.env.EMAIL_RECEIVER
    }
}