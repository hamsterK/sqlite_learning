import sqlite3 as sq

with sq.connect("cars.db") as con:
    cur = con.cursor()

    with open("sql_damp.sql", "w") as f:
        for sql in con.iterdump():  # iterdump shows instructions to recreate the table
            f.write(sql)

    # with open("sql_damp.sql", "r") as f:
    #     sql = f.read()
    #     cur.executescript(sql)  # execute sql script from file

     