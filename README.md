evolvedsqlite.py
================

## Script is completely untested. Use at your own risk.

### Description
Python based simple evolution (schema versioning) for sqlite. This is similar to [Play2 framework's evolutions](https://www.playframework.com/documentation/2.0/Evolutions).

### Installation and use
1. Download/Install the latest evolvedsqlite.py
2. Import the script into your project `from evolvedsqlite import evolvedb`
3. Run the evolution `evolvedb("path/to/evolve/scripts/", "dbname.db")`

### Tutorial
You need to create a directory:

```
~ mkdir evolutions
```

Then create a script:

```
~ vi 1.sql
```

* Notice the number. Evolutions work by building your database sequentially. Your first script will create your initial database. Your next script will add new tables or alter the current ones, thus you may name them 1.sql, 2.sql, 3.sql, 4.sql. It doesn't matter what number you give the scripts, this will run them in sorted ascending order.

Fill your file like so.

```
//--upgrade
CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL UNIQUE, password TEXT NOT NULL);
//--downgrade
DROP TABLE users;
```

Then run your app.
