import sqlite3
from flask import Flask, request

app = Flask(__name__)

# Initialize a sample SQLite database
conn = sqlite3.connect('users.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
conn.commit()

# Secure login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    # Secure SQL query using parameterized queries to prevent SQL Injection
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()

    if user:
        return "Welcome, " + user[1]
    else:
        return "Invalid credentials"

if __name__ == '__main__':
    app.run(debug=True)