import json
import sqlite3

# Load JSON data from the file
with open('C:\Users\ulask\Desktop\cmnd.ai\cmnd-extension-sample-python\output.json', 'r') as file:
    data = json.load(file)

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('properties.db')
c = conn.cursor()

# Create a table
c.execute('''
    CREATE TABLE IF NOT EXISTS properties (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT,
        location TEXT,
        price REAL,
        pricetype TEXT,
        thumb TEXT,
        cover TEXT,
        type TEXT,
        map TEXT,
        content TEXT
    )
''')

# Insert data into the table
for item in data['items']['item']:
    c.execute('''
        INSERT INTO properties (title, description, location, price, pricetype, thumb, cover, type, map, content) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (item['title'], item.get('description'), item['location'], float(item['price']), item['pricetype'],
          item['thumb'], item['cover'], item['type'], item.get('map'), item['content']))

# Commit changes and close the connection
conn.commit()
conn.close()
print("Data has been inserted into the database successfully.")