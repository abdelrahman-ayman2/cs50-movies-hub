import os

import sqlite3
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helper import lookup, login_required

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
conn = sqlite3.connect("movies.db", check_same_thread=False)
db = conn.cursor()

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    """show movies"""
    user_id = session["user_id"]

    search_history = db.execute("SELECT movie_name, timestamp FROM search_history WHERE user_id = ? ORDER BY timestamp DESC", (user_id,)).fetchall()

    if request.method == "POST":
        movie_name = request.form.get("movie_name")

        if not movie_name:
            return render_template("error.html", message="Movie name is required.")
        
        movie_details = lookup(movie_name)

        if not movie_details:
            return render_template("error.html", message="Movie not found.")
        
        db.execute("INSERT INTO search_history (user_id, movie_name) VALUES(?, ?)", (user_id, movie_name))
        conn.commit()

        return render_template("movies.html", movie=movie_details)
    
    return render_template("index.html", history=search_history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    session.clear()
    if request.method == "POST":
        useremail = request.form.get("useremail")
        userpassword = request.form.get("userpassword")
        if not useremail:
            return render_template("error.html", message="user email is not right")
        if not userpassword:
            return render_template("error.html", message="user password is not right") 
        rows = db.execute("SELECT * FROM users WHERE user_email = ?", (useremail,)).fetchall()
        if len(rows) != 1 or not check_password_hash(rows[0][2], userpassword):
             return render_template("error.html", message="Invalid email or password.")
        session["user_id"] = rows[0][0]
        return redirect("/")

    return render_template("login.html")



@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        useremail = request.form.get("useremail")
        userpassword = request.form.get("userpassword")
        confirmation = request.form.get("confirmation")
        users = db.execute("SELECT * FROM users")
        emails = [row[1] for row in users]
        if not useremail or not userpassword or not confirmation:
            return render_template("error.html", message="Please complete all fields: email, password, and confirmation.")
        if userpassword != confirmation:
            return render_template("error.html", message="Passwords do not match.")
        if useremail in emails:
            return render_template("error.html", message="Email is already registered.")
        db.execute("INSERT INTO users (user_email, hash) VALUES(?, ?)", 
                   (useremail, generate_password_hash(userpassword)))

        user_id = db.lastrowid
        conn.commit()
        session["user_id"] = user_id
        return redirect("/login")
    return render_template("register.html")


@app.route("/favorites")
@login_required
def favorites():
    """user favorites"""
    return render_template("favorites.html")


if __name__ == "__main__":
    app.run(debug=True)