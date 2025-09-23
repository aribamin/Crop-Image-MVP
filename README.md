# Crop Image MVP

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-orange)](https://flask.palletsprojects.com/)

A **minimal viable product (MVP)** web application for crop research image management, designed for demonstration to the **National Research Council Canada (NRC)**. This tool showcases **secure image upload, metadata tagging, search functionality, and gallery visualization**, aligned with FAIR principles.

---

## 🇨🇦 Overview | Vue d'ensemble

This project simulates a **Government of Canada–style research portal** for managing crop images collected from high-throughput imaging platforms. It allows researchers to:

- Upload images with **title and tags**.
- Search images by title or tags.
- Browse a **clean, responsive gallery**.
- Experience a simple **login system** for authentication.

---

## 🎯 Features

- **Login/Logout** (hardcoded credentials for MVP)
- **Image upload** with title & tags
- **Search functionality** (title & tags)
- **Gallery view** with uniform cards and badges
- **Responsive design** suitable for desktop and mobile
- **Government of Canada–inspired styling** (header, footer, colors, bilingual labels)

---

## 🛠️ Tech Stack

- **Python 3.11**  
- **Flask 2.3.3**  
- **SQLite** (local database)  
- **Bootstrap 5.3** (front-end styling)  

---

## ⚙️ Setup & Installation

```bash
1. Clone this repository:
git clone https://github.com/aribamin/crop_mvp.git
cd crop_mvp

2. Install dependencies:
pip install -r requirements.txt

3. Run the Flask app:
python app.py

4. Open your browser at:
http://127.0.0.1:5000

5. Login with demo credentials:
Username: demo
Password: demo
```