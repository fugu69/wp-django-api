# Wild Politics: Overview API Backend

This is a Django + Django REST Framework (DRF) backend for the **Wild Politics** browser game. It replicates the data and functionality found in the in-game “Overview” menu and exposes it via a REST API and basic HTML views. The project demonstrates Django and PostgreSQL development capabilities.

---

## 🚀 Features

- **Player Management**
  - View player details (HTML + API)
  - Edit player information

- **Article Management**
  - List and view articles
  - Update article content

---

## 🔌 REST API Endpoints

### Player
- `GET /api/players/<id>/`  
  Returns player information by ID.

- `GET /api/player/<id>/edit/`  
  `POST /api/player/<id>/edit/`  
  View and update player info using an HTML form.

### Article
- `GET /api/articles/`
  Returns a list of all articles. 
  
- `GET /api/articles/<id>/`  
  Returns article information by ID.

- `GET /api/articles/<id>/edit/`  
  `POST /api/articles/<id>/edit/`  
  View and update article content using an HTML form.

---

## 🛠️ Tech Stack

- Python 3
- Django 5
- Django REST Framework
- PostgreSQL

---

## 🔧 Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/wp-django-api.git
   cd wp-django-api
   ```

2. **Set Up Virtual Environment**
   ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**
   ```bash
    pip install -r requirements.txt
    ```
4. **Set Up the Database**

> ⚠️ This project requires a PostgreSQL database dump (`.sql`) that is **not included** in this repository.

- Ensure PostgreSQL is installed.
- Create a new database, e.g. `wp_overview`:
  ```bash
  createdb wp_overview

---

## 📂 Project Structure

overview/
├── models.py         # Player and Article models
├── serializers.py    # DRF serializers
├── views.py          # API and HTML views
├── forms.py          # Forms for editing
├── urls.py           # App-level routing
└── templates/        # Basic HTML templates
    └── overview/
        ├── player_detail.html
        ├── player_update.html
        ├── article_detail.html
        └── article_update.html

---

## ❓Notes
- This project is local-only (not deployed)
- Intended for demonstration and development purposes
- Future expansions may include authentication, user roles, or richer article formatting tools

---

## 🧠 Author & License
Created by Maximus Brutalis — for educational and portfolio use.

License: MIT