import sqlite3

conn = sqlite3.connect('demo.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
''')

# insert the data 
cursor.executemany('''
    INSERT INTO customers (name, age) VALUES (?, ?)
''',[
    ('John Doe', 30),
    ('Jane Smith', 25),
    ('Alice Johnson', 35),
    ]
)


## now order table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Sales (
        id INTEGER PRIMARY KEY,
        customer_id INTEGER NOT NULL,
        product_name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        price REAL NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES customers (id)
    )
''')

# insert the data 
cursor.executemany('''
    INSERT INTO Sales (customer_id, product_name, quantity, price) VALUES (?, ?, ?, ?)
''',[
    (1, 'Laptop', 1, 1200.00),
    (2, 'Smartphone', 2, 800.00),
    (3, 'Tablet', 1, 500.00),
    (1, 'Headphones', 2, 150.00),
    (2, 'Mouse', 1, 50.00),
    (3, 'Keyboard', 1, 100.00),
    (1, 'Monitor', 1, 200.00),
    (2, 'Printer', 2, 100.00),
    (3, 'Headphones', 1, 50.00),
    ]
)

conn.commit()
conn.close()
