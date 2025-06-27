from flask import Flask, request
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
    cursor.execute('INSERT OR IGNORE INTO users VALUES (1, "Admin"), (2, "User")')
    conn.commit()
    conn.close()

init_db()

@app.route('/search')
def search():
    user_input = request.args.get('id')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # VULNERABLE: String concatenation
    query = f"SELECT * FROM users WHERE id = {user_input}"
    cursor.execute(query)
    
    result = cursor.fetchall()
    conn.close()
    return {'data': result}

if __name__ == '__main__':
    app.run(debug=True, port=5000)