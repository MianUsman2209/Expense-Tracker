# Expense Tracker API (Backend Only)

A **backend-only RESTful API** for an Expense Tracker application.  
This project provides secure user authentication and full CRUD operations for managing personal expenses.  
There is **no frontend** (no HTML, CSS, or JavaScript UI) — this project focuses purely on backend development.

This project is designed as a **beginner-level backend project**, following best practices for authentication, authorization, and API design.

---

## 🚀 Features

### 🔐 Authentication & Authorization
- User **Sign Up**
- User **Login**
- **JWT (JSON Web Token)** based authentication
- Protected routes using JWT
- Each user can only access **their own expenses**

---

### 💸 Expense Management (CRUD)
- **Create** a new expense
- **Read / List** expenses
- **Update** existing expenses
- **Delete** expenses

---

### 📅 Expense Filtering
Users can filter their expenses by date:
- Past week
- Past month
- Last 3 months
- Custom date range (start date & end date)

---

### 🗂 Expense Categories
Expenses can belong to one of the following categories:
- Groceries
- Leisure
- Electronics
- Utilities
- Clothing
- Health
- Others

---

## 🧱 Tech Stack

- **Backend:** API-only (no frontend)
- **Authentication:** JWT (JSON Web Tokens)
- **Database:** Any relational or NoSQL database
- **ORM / DB Library:** Optional (based on implementation)
- **Architecture:** RESTful API

> Note: This repository focuses on backend logic and API development only.

---

## 📌 API Capabilities Summary

| Feature | Supported |
|------|---------|
| User Registration | ✅ |
| User Login | ✅ |
| JWT Authentication | ✅ |
| Create Expense | ✅ |
| Read Expenses | ✅ |
| Update Expense | ✅ |
| Delete Expense | ✅ |
| Date-Based Filters | ✅ |
| Multi-user Support | ✅ |

---

## 🔒 Security
- JWT is required to access protected endpoints
- User identity is derived from the JWT
- Users can only view or modify their own data

---

## 🧪 Usage
This API can be tested using tools such as:
- Postman
- Insomnia
- cURL

It can later be connected to:
- Web frontend (React, Vue, etc.)
- Mobile apps (Flutter, React Native)
- Any client that consumes REST APIs

---

## 📚 Learning Outcome

This project helps you understand:
- Backend API development
- JWT-based authentication
- Secure user-specific data handling
- RESTful design principles
- CRUD operations with databases

This is the **final beginner project** in the backend roadmap.  
After completing this, you’re ready to move on to **intermediate backend projects**.

---

## 📄 License
This project is for learning and educational purposes.
