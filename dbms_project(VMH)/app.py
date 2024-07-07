# DBMS Project
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL configuration
db_config = {
    'user': 'root',
    'password': '3031',
    'host': 'localhost',
    'database': 'books_db'
}

# Connect to MySQL
def get_db_connection():
    conn = mysql.connector.connect(**db_config)
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', books=books)

@app.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        id = request.form['id']
        book_name = request.form['book_name']
        cost = request.form['cost']
        rating = request.form['rating']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (id, book_name, cost, rating) VALUES (%s, %s, %s, %s)",
                       (id, book_name, cost, rating))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('insert.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE id=%s", (id,))
    book = cursor.fetchone()
    if request.method == 'POST':
        book_name = request.form['book_name']
        cost = request.form['cost']
        rating = request.form['rating']
        cursor.execute("UPDATE books SET book_name=%s, cost=%s, rating=%s WHERE id=%s",
                       (book_name, cost, rating, id))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    cursor.close()
    conn.close()
    return render_template('update.html', book=book)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
