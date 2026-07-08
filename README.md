# Smart Expense Tracker AI

Smart Expense Tracker AI is a full-stack expense management application built with React, FastAPI, PostgreSQL, and AI integration. It allows users to add, view, and manage expenses, with future support for AI-based expense categorization and spending insights.

## Features

* Add new expenses
* View all expenses
* Store expense data in PostgreSQL
* FastAPI backend with REST APIs
* React frontend using Vite
* Clean project structure for frontend and backend
* Docker-ready project setup
* Planned AI-based categorization and monthly insights

## Tech Stack

### Frontend

* React.js
* Vite
* JavaScript
* CSS

### Backend

* Python
* FastAPI
* SQLAlchemy
* Pydantic
* PostgreSQL

### Tools

* Git and GitHub
* Postman
* pgAdmin
* Docker

## Project Structure

```text
smart-expense-tracker-ai/
│
├── backend/
│   ├── app/
│   │   ├── database.py
│   │   ├── main.py
│   │   ├── models/
│   │   ├── routes/
│   │   └── schemas/
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── App.jsx
│   │   └── main.jsx
│   └── package.json
│
├── docker-compose.yml
├── .env.example
├── .gitignore
└── README.md
```

## Expense Model

Each expense contains:

```text
id
title
amount
category
payment_mode
description
expense_date
created_at
```

## Backend Setup

Go to the backend folder:

```bash
cd backend
```

Create and activate virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run FastAPI server:

```bash
uvicorn app.main:app --reload
```

Backend will run at:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

## Frontend Setup

Go to the frontend folder:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run frontend:

```bash
npm run dev
```

Frontend will run at:

```text
http://localhost:5173
```

## API Endpoints

### Create Expense

```http
POST /expenses
```

Sample request:

```json
{
  "title": "Lunch",
  "amount": 250,
  "category": "Food",
  "payment_mode": "UPI",
  "description": "Lunch at restaurant",
  "expense_date": "2026-07-08"
}
```

### Get Expenses

```http
GET /expenses
```

## Current Status

* Backend setup completed
* PostgreSQL connected
* Expense model created
* Expense create API working
* Frontend expense form connected with backend
* Expense creation from UI working successfully

## Upcoming Enhancements

* Update expense
* Delete expense
* Dashboard with monthly totals
* Category-wise spending summary
* AI-based expense categorization
* Monthly AI spending insights
* Docker containerization
* Deployment-ready configuration

## Resume Highlight

Built a full-stack AI-powered expense tracker using React, FastAPI, PostgreSQL, and Docker, enabling users to manage expenses with planned AI-based categorization and spending insights.
