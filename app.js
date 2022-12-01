
const path = require('path');
const { database} = require('./config');
const Backup = require('./helpers/Backup');

Backup.databaseDumps();
