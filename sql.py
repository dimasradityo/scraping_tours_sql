import sqlite3

# Establish Connection
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# Query Data
cursor.execute("select * from events")
rows = cursor.fetchall()
print(rows)

# Insert new rows
# new_rows = [('Cats', 'Cats City', '2088.10.17'), ('Dogs', 'Dogs City', '2088.10.17')]
# cursor.executemany("insert into events values(?,?,?)", new_rows)
# connection.commit()