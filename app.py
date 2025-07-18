from flask import Flask, render_template, request
from db import connection, mycursor, IntegrityError
from werkzeug.security import generate_password_hash

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World"

@app.route('/register', methods=["GET"])
def user_creation():
   return render_template("register.html")

@app.route('/register', methods=["POST"])
def return_user_info():
    username = request.form["Username"]
    email = request.form["email"]
    password = request.form["password"]
    hashed_password = generate_password_hash(password)
 
    if len(password) < 6:
        return "Password should have at least six (6) characters"
    elif "@" not in email or "." not in email:
        return "Please enter a valid email"
    elif " " in username:
        return "Spaces are not allowed in your username"

    try:
        sql = """
            INSERT INTO USER (Username, Email, password_hash) 
            VALUES(%s, %s, %s)"""
        
        mycursor.execute(sql, (username, email, hashed_password))
        connection.commit()
        return "User created successfully"
    except IntegrityError:
        return "Username or email already exists"


if __name__ == '__main__':
    app.run(debug=True)