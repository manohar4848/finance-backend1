# Finance Data Processing and Access Control Backend

## 📌 Overview

This project is a backend system for a finance dashboard that manages financial records, user roles, and provides analytical insights. It includes authentication, role-based access control, and dashboard APIs.

---

## 🚀 Features

### 👤 User & Role Management

* Custom user model with roles:

  * Viewer (read-only)
  * Analyst (view + insights)
  * Admin (full access)
* Role-based access control implemented using custom permissions

---

### 🔐 Authentication

* Token-based login implemented
* Users can log in and receive a token
* Token is used to access protected APIs

#### 🔑 Login Endpoint

POST `/api/users/login/`

Example:

```json
{
  "username": "manohar",
  "password": "1234"
}
```

Response:

```json
{
  "token": "your_token_here"
}
```

---

### 💰 Financial Records

* Create, Read, Update, Delete (CRUD)
* Fields:

  * Amount
  * Type (income/expense)
  * Category
  * Date
  * Notes

---

### 🔍 Filtering

* Filter records by:

  * Type → `/api/records/?type=income`
  * Category → `/api/records/?category=food`
  * Date → `/api/records/?date=2026-04-01`

---

### 📊 Dashboard APIs

* Total income
* Total expenses
* Net balance
* Category-wise summary

#### Endpoints:

* GET `/api/records/dashboard/`
* GET `/api/records/category-summary/`

---

## 📡 API Endpoints

### Records

* GET `/api/records/`
* POST `/api/records/`
* GET `/api/records/{id}/`
* PUT `/api/records/{id}/`
* DELETE `/api/records/{id}/`

### Authentication

* POST `/api/users/login/`

---

## 🛠️ Tech Stack

* Python
* Django
* Django REST Framework
* SQLite

---

## ⚙️ Setup Instructions

1. Clone repository
2. Install dependencies:

   ```
   pip install django djangorestframework
   ```
3. Apply migrations:

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Create user:

   ```
   python manage.py createsuperuser
   ```
5. Run server:

   ```
   python manage.py runserver
   ```

---

## 📸 Sample Access

* Home: http://127.0.0.1:8000/
* Records: http://127.0.0.1:8000/api/records/
* Dashboard: http://127.0.0.1:8000/api/records/dashboard/
* Login: http://127.0.0.1:8000/api/users/login/

---

## 🔐 How to Use Token

Add header in requests:

```
Authorization: Token your_token_here
```

---

## 📌 Assumptions

* SQLite used for simplicity
* Authentication kept simple using token system
* Focus is on backend logic and API design

---

## 🎯 Conclusion

This project demonstrates backend development skills including API design, data modeling, authentication, role-based access control, and financial data analytics.
