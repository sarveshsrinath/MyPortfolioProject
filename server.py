from flask import Flask, request, send_from_directory, redirect, url_for
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/images/<path:path>')
def send_images(path):
    return send_from_directory('images', path)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Save the data to the database
    save_to_db(name, email, message)
    
    return f"Form submitted successfully! Name: {name}, Email: {email}, Message: {message}"

def save_to_db(name, email, message):
    # Connect to MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="sarvesh",
        password="root123",
        database="contacts"  # Replace with your actual database name
    )
    cursor = conn.cursor()
    
    # Insert form data into the database
    cursor.execute("INSERT INTO submissions (name, email, message) VALUES (%s, %s, %s)",
                   (name, email, message))
    
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    app.run(debug=True)



