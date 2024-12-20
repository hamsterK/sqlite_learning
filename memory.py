import sqlite3 as sq

data = [("car", "машина"), ("house", "дом"), ("tree", "дерево"), ("color", "цвет")]

con = sq.connect(':memory:')  # to create db in memory (temp)
with con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS dict(
        eng TEXT, rus TEXT)
    """)

    cur.executemany("INSERT INTO dict VALUES(?, ?)", data)

    cur.execute("SELECT rus FROM dict WHERE eng LIKE 'c%'")
    print(cur.fetchall())