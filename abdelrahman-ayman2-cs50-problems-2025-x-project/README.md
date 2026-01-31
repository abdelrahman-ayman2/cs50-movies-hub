# 🎬 Movies Hub

#### Video Demo: https://youtu.be/AqvpSfYSWFQ  
#### GitHub Username: abdelrahman-ayman2  
#### edX Username: abdelrahman_9825  
#### City and Country: Cairo, Egypt
#### Date: August 8, 2025

---

## 📌 Description

**Movies Hub** is a Flask-based web application that allows users to search for movies and view detailed information including the title, release year, poster, genres, directors, cast, and streaming availability. The app integrates with the **Streaming Availability API** via RapidAPI.

It also provides user authentication (register/login/logout), a personalized search history, and a responsive user interface using Bootstrap 5.

This project was built as my final project for CS50x, combining many concepts covered in the course such as web development, SQL databases, APIs, and user authentication.

---

## ✅ Features

- 🔐 User registration, login, and logout
- 🔎 Movie search by title using external API
- 🖼️ Movie details with poster, genres, cast, and directors
- 📜 Logged-in users can view their own search history
- 💡 Error handling for empty or incorrect movie names
- 🎨 Clean, responsive UI built with Bootstrap 5

---

## 🧰 Technologies Used

- Python (Flask)
- SQLite (movies.db)
- HTML5, CSS3, Bootstrap 5
- Jinja2 Templates
- `requests`, `flask_session`, and `werkzeug.security` modules
- Streaming Availability API from RapidAPI

---

## 🧱 Project Structure

movies-hub/
├── app.py # Main application file (Flask routes)
├── helper.py # Helper functions including lookup()
├── init_db.py # Script to initialize SQLite database
├── movies.db # SQLite database file
├── requirements.txt # Required Python libraries
├── README.md # This file
├── templates/ # HTML templates (layout, index, login, register, movies, error)
│ ├── layout.html
│ ├── index.html
│ ├── login.html
│ ├── register.html
│ ├── movies.html
│ └── error.html

---

## ▶️ How to Run the App

1. Clone the repository or copy the files into a folder.
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate

3. Install the required packages:
pip install -r requirements.txt

4. Initialize the database (run this once):
python init_db.py

5. Start the Flask app:
flask run
Open your browser and go to http://127.0.0.1:5000/.

💡 Design Decisions:
I used Flask-Session to store user sessions securely on the server.

Passwords are hashed using werkzeug.security for security.

I separated the lookup logic in helper.py to keep routes clean.

Search history is stored per user to personalize the experience.

The movie poster and streaming options are fetched directly from the API response.

The app handles common edge cases like missing movie titles or bad inputs.


🤖 Use of AI Tools:
Parts of the logic (e.g. formatting streaming results or optimizing error handling) were improved using ChatGPT, but the core code, structure, and logic were fully written and implemented by me.

📽️ Final Thoughts
I learned a lot during the development of this project, especially about Flask, APIs, and database design. I'm proud of how it turned out, and it helped solidify many concepts I learned in CS50x. I hope to continue building on this by adding a favorites feature and maybe deploying it live!

Thank you, CS50! 🙏
