from flask import Flask, render_template
import sqlite3
from sqlite3 import Error
app = Flask(__name__)
DB_FILE = 'cafe.db'
# Inputs: database file location
# Outputs: returns the connection to the database or an error
# Overall: This function connects to our database

def connect_to_database(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print("There was an error connecting")
        print(e)
    return None


@app.route('/')
def render_homepage():
    return render_template('home.html')


@app.route('/menu')
def render_menu_page():
    con = connect_to_database(DB_FILE)
    query = 'SELECT name, description, image, volume, price FROM products'
    cur = con.cursor()
    cur.execute(query)
    product_list = cur.fetchall()
    return render_template('menu.html', products=product_list)


@app.route('/contact')
def render_contact_page():
    return render_template('contact.html')


app.run(host='0.0.0.0', debug=True)