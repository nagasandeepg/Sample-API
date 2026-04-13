import sqlite3

def init_db():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT,
        role TEXT
    )
    """)

    # Insert sample data
    cursor.execute("INSERT OR IGNORE INTO employees VALUES (101, 'John Doe', 'Engineer')")
    cursor.execute("INSERT OR IGNORE INTO employees VALUES (102, 'Alice Smith', 'Manager')")

    conn.commit()
    conn.close()


def get_employee(emp_id):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees WHERE id=?", (emp_id,))
    row = cursor.fetchone()

    conn.close()

    if row:
        return f"Employee ID: {row[0]}, Name: {row[1]}, Role: {row[2]}"
    else:
        return "Employee not found"