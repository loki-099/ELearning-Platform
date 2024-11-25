import sqlite3

def initialize_database():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    # Create tables
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Person (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        email TEXT,
        full_name TEXT,
        birthdate TEXT,
        address TEXT,
        gender TEXT,
        user_type TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Course (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_title TEXT UNIQUE,
        course_description TEXT,
        instructor TEXT,
        total_students INTEGER DEFAULT 0
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Enrollment (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        course_id INTEGER,
        progress TEXT,
        completed BOOLEAN DEFAULT 0,
        FOREIGN KEY(student_id) REFERENCES Person(id),
        FOREIGN KEY(course_id) REFERENCES Course(id)
    )
    ''')

    connection.commit()
    connection.close()

# Initialize database
initialize_database()
