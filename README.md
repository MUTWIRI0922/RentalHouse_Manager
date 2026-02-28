# 🏠 Rental House Manager

**RentalHouse_Manager** is a Django-powered web application for managing rental properties, tenants, leases, and users. It provides APIs for property managers to track rentals, tenants and payments.

---

## 📋 Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
   - [Database Setup](#database-setup)
   - [Running the Server](#running-the-server)
5. [API Endpoints](#api-endpoints)
6. [Testing](#testing)
7. [Project Structure](#project-structure)
8. [Contributing](#contributing)
9. [License](#license)
10. [Contact](#contact)

---

## 🔍 Project Overview

This application helps manage rental houses with focus on:

- Tracking available units
- Managing tenants and leases
- Organizing users (staff/owners)
- Providing RESTful APIs for front‑end or mobile clients

Built using Django and Django REST Framework.

---

## ✅ Features

- CRUD for **Rentals** (houses/rooms)
- Tenant registration and profile management
- Lease creation/termination
- User authentication and permissions
- Serialized JSON API responses
- Unit tests for models, views and serializers

---

## 🛠️ Tech Stack

- **Python 3.11+**
- **Django 5.x**
- **Django REST Framework**
- **SQLite** (default; easily swapable)
- **pytest / Django’s test runner**

---

## 🚀 Getting Started

### Prerequisites

Make sure you have:

- Python 3.11+ installed
- `pip` or `pipenv`/`poetry`
- (Optional) virtual environment tool such as `venv` or `virtualenv`

### Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/yourusername/RentalHouse_Manager.git
   cd RentalHouse_Manager
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   .\venv\Scripts\activate       # Windows
   source venv/bin/activate      # macOS/Linux
   ```

3. Install dependencies:

   > ```bash
   > pip install django djangorestframework
   > ```

### Database Setup

Run migrations to create the SQLite database (or configured DB):

```bash
python manage.py migrate
```

(Optional) create a superuser:

```bash
python manage.py createsuperuser
```

### Running the Server

Start Django’s development server:

```bash
python manage.py runserver
```

Access the app at: <http://127.0.0.1:8000/>

---

## 📡 API Endpoints

(Adapt these to match your `urls.py` routing; example below)

- `GET /rentals/` – list rentals
- `POST /rentals/` – create a rental
- `GET /rentals/{id}/` – retrieve rental
- `PUT /rentals/{id}/` – update rental
- `DELETE /rentals/{id}/` – delete rental

- `GET /users/`, `POST /users/`, etc.
- `GET /tenants/`, `POST /tenants/`, etc.

Use the Django REST Framework browsable API or a tool like Postman.

---


## 🗂️ Project Structure

```
RentalHouse_Manager/
├── RentalHouse_Manager/      # project config
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── Rentals/                  # rentals app
│   ├── models.py
│   ├── views.py
│   └── ...
├── users/                    # users app
│   ├── models.py
│   ├── serializers.py
│   └── ...
├── db.sqlite3
├── manage.py
└── README.md
```

---

## 🤝 Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/YourFeature`.
3. Commit your changes and push to your branch.
4. Open a pull request describing your changes.

Please follow PEP 8 and write tests for new functionality.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE) – feel free to use or modify it responsibly.



