import sqlite3

conn = sqlite3.connect('data/derrick_data.db')
cursor = conn.cursor()

cursor.execute('''SELECT * from data''')
result = cursor.fetchall()

conn.commit()
conn.close()

if __name__ == "__main__":
    print(result)
