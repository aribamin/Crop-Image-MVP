from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "demo_secret"  # for session management
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize DB
conn = sqlite3.connect("database.db")
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS images (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT,
                title TEXT,
                tags TEXT
            )''')
conn.commit()
conn.close()

# Hardcoded login credentials for MVP
USERNAME = "demo"
PASSWORD = "demo"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == USERNAME and password == PASSWORD:
            session["user"] = username
            return redirect(url_for("upload"))
        else:
            return "Invalid credentials"
    return render_template("login.html")

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if "user" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        file = request.files["image"]
        title = request.form.get("title")
        tags = request.form.get("tags")
        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            conn = sqlite3.connect("database.db")
            c = conn.cursor()
            c.execute("INSERT INTO images (filename, title, tags) VALUES (?, ?, ?)",
                      (file.filename, title, tags))
            conn.commit()
            conn.close()
            return redirect(url_for("gallery"))
    return render_template("upload.html")

@app.route("/gallery", methods=["GET"])
def gallery():
    if "user" not in session:
        return redirect(url_for("login"))
    search = request.args.get("search", "")
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    if search:
        c.execute("SELECT * FROM images WHERE title LIKE ? OR tags LIKE ?", (f"%{search}%", f"%{search}%"))
    else:
        c.execute("SELECT * FROM images")
    images = c.fetchall()
    conn.close()
    return render_template("gallery.html", images=images, search=search)

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
