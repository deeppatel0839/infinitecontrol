from flask import Flask, render_template, request, jsonify, redirect, url_for
import sqlite3, os

app = Flask(__name__)
DB = os.path.join(os.path.dirname(__file__), 'inquiries.db')

def init_db():
    conn = sqlite3.connect(DB)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS inquiries (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            name       TEXT NOT NULL,
            email      TEXT NOT NULL,
            phone      TEXT,
            panel_type TEXT,
            message    TEXT,
            created_at TEXT DEFAULT (datetime('now','localtime'))
        )
    """)
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    d = request.form
    conn = sqlite3.connect(DB)
    conn.execute(
        "INSERT INTO inquiries (name,email,phone,panel_type,message) VALUES (?,?,?,?,?)",
        (d.get('name',''), d.get('email',''), d.get('phone',''),
         d.get('panel_type',''), d.get('message',''))
    )
    conn.commit()
    conn.close()
    return jsonify({'ok': True, 'message': 'Inquiry saved!'})

@app.route('/inquiries')
def view_inquiries():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    rows = conn.execute("SELECT * FROM inquiries ORDER BY id DESC").fetchall()
    conn.close()
    return render_template('inquiries.html', inquiries=rows)

if __name__ == '__main__':
    init_db()
    print("\n∞  Infinite Control Panel System Inc.")
    print("   Marketing site → http://127.0.0.1:5000\n")
    app.run(debug=True, port=5000)
