# 🤖 FastAPI AI Chat Bot

A simple AI chatbot API built with **FastAPI**, **MySQL**, and **SQLAlchemy**.

## 🚀 Features

* FastAPI
* MySQL Database
* SQLAlchemy ORM
* Alembic Migration
* Multiple AI Providers
* Swagger API Documentation

## 🛠️ Installation

### 1. Clone the Project

```bash
git clone https://github.com/DevelSajjad/fastapi-chat-bot.git
cd fastapi-chat-bot
```

### 2. Create Virtual Environment. Note: if you see venv folder then delete that folder at first.

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create MySQL Database

```sql
CREATE DATABASE fastapi_chat_bot;
```

### 5. Configure `.env`

```env
DATABASE_URL=mysql+pymysql://root:password@localhost/fastapi_chat_bot
```

Add your AI provider API keys/configuration in `.env` as needed.

### 6. Run Migration

```bash
alembic upgrade head
```

### 7. Start Server

```bash
uvicorn app.main:app --reload
```

## 📚 API Documentation

Swagger:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

## 📁 Project Structure

```text
fastapi-chat-bot/
├── app/
├── alembic/
├── .env
├── requirements.txt
└── README.md
```

## 🗄️ Database

MySQL is used as the database and SQLAlchemy is used for database operations.

Migrations are managed with Alembic.

## 👨‍💻 Author

Sajjad

## 📄 License

This project is for learning and development purposes.
