import sqlite3
# Create or connect to database
conn = sqlite3.connect('IBABEmployee.db')
cur = conn.cursor()
# Create table
cur.execute('''
CREATE TABLE IF NOT EXISTS Employee (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    ResearchArea TEXT,
    Designation TEXT,
    Gender TEXT
)
''')
conn.commit()
print("Database and table created successfully.")
conn.close()
#(i)
conn = sqlite3.connect('IBABEmployee.db')
cur = conn.cursor()
while True:
    id_ = int(input("Enter ID: "))
    name = input("Enter name: ")
    research = input("Enter research area: ")
    designation = input("Enter designation: ")
    gender = input("Enter gender: ")

    cur.execute("INSERT INTO Employee VALUES (?, ?, ?, ?, ?)",
                (id_, name, research, designation, gender))
    conn.commit()

    choice = input("Add another record? (y/n): ")
    if choice.lower() != 'y':
        break

print("Records added successfully.")
conn.close()
#(ii)
conn = sqlite3.connect('IBABEmployee.db')
cur = conn.cursor()
id_ = int(input("Enter ID of employee to edit: "))

#(iii) Get current details
cur.execute("SELECT * FROM Employee WHERE ID=?", (id_,))
record = cur.fetchone()

if record:
    print("Current record:", record)
    name = input("Enter new name: ")
    research = input("Enter new research area: ")
    designation = input("Enter new designation: ")
    gender = input("Enter new gender: ")

    cur.execute('''
        UPDATE Employee 
        SET Name=?, ResearchArea=?, Designation=?, Gender=?
        WHERE ID=?
    ''', (name, research, designation, gender, id_))
    conn.commit()
    print("Record updated successfully.")
else:
    print("No record found with that ID.")
conn.close()

#(iv)
conn = sqlite3.connect('IBABEmployee.db')
cur = conn.cursor()
ids = input("Enter IDs to delete (space-separated): ").split()
for i in ids:
    cur.execute("DELETE FROM Employee WHERE ID=?", (int(i),))
conn.commit()
print("Records deleted successfully.")
conn.close()
#(v)
from tabulate import tabulate  # pip install tabulate (optional for neat formatting)
conn = sqlite3.connect('IBABEmployee.db')
cur = conn.cursor()
cur.execute("SELECT * FROM Employee")
rows = cur.fetchall()
if rows:
    print(tabulate(rows, headers=["ID", "Name", "Research Area", "Designation", "Gender"], tablefmt="grid"))
else:
    print("No records found.")
conn.close()