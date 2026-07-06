from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine, Base
from app.models import expense, income, budget
from app.routes import expense_routes, income_routes, dashboard_routes, budget_routes

app = FastAPI(
    title="Smart Expense Tracker API",
    description="Backend API for Smart Expense Tracker AI project",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(expense_routes.router)
app.include_router(income_routes.router)
app.include_router(dashboard_routes.router)
app.include_router(budget_routes.router)


@app.get("/")
def home():
    return {
        "message": "Smart Expense Tracker API is running"
    }