module.exports = {
    database: {
        password: process.env.DATABASE_PASSWORD,
        database: process.env.DATABASE_DATABASE,
        host: process.env.DATABASE_HOST,
        user: process.env.DATABASE_USER,
        port: 3306
    }
}