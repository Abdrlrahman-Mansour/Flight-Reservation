import sqlite3

def create_connection():
    conn = sqlite3.connect("flights.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            flight_number TEXT NOT NULL,
            departure TEXT NOT NULL,
            destination TEXT NOT NULL,
            date TEXT NOT NULL,
            seat_number TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# CRUD Functions
def insert_reservation(data):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', data)
    conn.commit()
    conn.close()

def fetch_all_reservations():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservations")
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_reservation(reservation_id, data):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE reservations 
        SET name=?, flight_number=?, departure=?, destination=?, date=?, seat_number=?
        WHERE id=?
    ''', (*data, reservation_id))
    conn.commit()
    conn.close()

def delete_reservation(reservation_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM reservations WHERE id=?", (reservation_id,))
    conn.commit()
    conn.close()