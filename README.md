#  Scalable E-Commerce API (FastAPI + PostgreSQL)

A high-performance backend REST API for managing products, users, and orders, built using **FastAPI** and **PostgreSQL**. The system implements secure authentication using **JWT tokens** and ensures data protection with **bcrypt password hashing**.

---

## 🚀 Live Demo

🔗 API Base URL:
https://ecommerce-fastapi-myor.onrender.com

📄 Swagger Docs:
https://ecommerce-fastapi-myor.onrender.com/docs

---

## 📌 Features

*  User Authentication using JWT
*  Secure Password Hashing (bcrypt)
*  Product Management (Add / View)
*  Order Placement with User Association
*  Pagination Support for Products
*  Modular Code Structure (Clean Architecture)
*  Deployed on Render with PostgreSQL

---

## 🛠️ Tech Stack

* **Backend:** FastAPI (Python)
* **Database:** PostgreSQL
* **Authentication:** JWT (JSON Web Tokens)
* **Security:** bcrypt (Password Hashing)
* **ORM:** SQLAlchemy
* **Deployment:** Render

---

## 📂 Project Structure

```
ecommerce-api/
│── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   ├── crud.py
│   ├── routes/
│   │     ├── user.py
│   │     ├── product.py
│   │     ├── order.py
│── requirements.txt
│── .env
```

---

## 🔐 Authentication Flow

1. User registers with email & password
2. Password is hashed using bcrypt
3. User logs in → receives JWT token
4. Token is used to access protected routes
5. Orders are linked to authenticated users

---

## 📸 Screenshots

### 🔹 Swagger UI

(Add your Swagger screenshot here)

### 🔹 Login & Token Response

(Add login response screenshot)

### 🔹 Postman Request with Bearer Token

(Add Postman screenshot)

### 🔹 Order API Response

(Add final output screenshot)

---

## ⚙️ Setup Instructions (Local)

### 1️⃣ Clone Repository

```bash
git clone https://github.com/SiddhiMalwadkar/ecommerce-fastapi
cd ecommerce-fastapi
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create `.env` file:

```
DATABASE_URL=postgresql://siddhi:cAdaGbAC9Vd1N338o3nWNuxDudiEUZk9@dpg-d7auegudqaus73c4iqrg-a.oregon-postgres.render.com/ecommerce_oz3l
SECRET_KEY=mysupersecretkey123
ALGORITHM=HS256
```

### 5️⃣ Run Server

```bash
uvicorn app.main:app --reload
```

---

## 🧪 API Endpoints

| Method | Endpoint       | Description               |
| ------ | -------------- | ------------------------- |
| POST   | /auth/register | Register user             |
| POST   | /auth/login    | Login & get token         |
| POST   | /products/     | Add product               |
| GET    | /products/     | Get products (pagination) |
| POST   | /orders/       | Place order (Protected)   |

---

## 🔒 Security Features

* Passwords stored as hashed values using bcrypt
* JWT-based authentication for protected routes
* User-specific order handling
* Input validation using Pydantic schemas

---

## 🚀 Future Improvements

*  Role-based access (Admin/User)
*  Cart system
*  Order history
*  Advanced filtering & search
*  Docker support

---

## 👩‍💻 Author

**Siddhi Girish Malwadkar**
 [malwadkarsiddhigirish@gmail.com](mailto:malwadkarsiddhigirish@gmail.com)
 LinkedIn: https://www.linkedin.com/in/siddhi-malwadkar-a2018b246

---

## ⭐ Acknowledgement

This project was built as part of backend development learning to implement real-world scalable API design and deployment.

---
