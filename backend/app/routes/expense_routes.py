from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import date

from app.database import get_db
from app.schemas.expense import ExpenseCreate, ExpenseUpdate, ExpenseResponse
from app import crud


router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"]
)


@router.post("/", response_model=ExpenseResponse)
def add_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
    return crud.create_expense(db, expense)


@router.get("/", response_model=List[ExpenseResponse])
def fetch_expenses(db: Session = Depends(get_db)):
    return crud.get_all_expenses(db)


@router.get("/summary/total")
def fetch_total_expense(db: Session = Depends(get_db)):
    return crud.get_total_expense(db)


@router.get("/summary/category")
def fetch_category_summary(db: Session = Depends(get_db)):
    return crud.get_category_summary(db)


@router.get("/filter/category/{category}", response_model=List[ExpenseResponse])
def fetch_expenses_by_category(category: str, db: Session = Depends(get_db)):
    return crud.get_expenses_by_category(db, category)


@router.get("/filter/payment-mode/{payment_mode}", response_model=List[ExpenseResponse])
def fetch_expenses_by_payment_mode(payment_mode: str, db: Session = Depends(get_db)):
    return crud.get_expenses_by_payment_mode(db, payment_mode)


@router.get("/{expense_id}", response_model=ExpenseResponse)
def fetch_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = crud.get_expense_by_id(db, expense_id)

    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    return expense


@router.put("/{expense_id}", response_model=ExpenseResponse)
def edit_expense(
    expense_id: int,
    expense_data: ExpenseUpdate,
    db: Session = Depends(get_db)
):
    expense = crud.update_expense(db, expense_id, expense_data)

    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    return expense


@router.delete("/{expense_id}")
def remove_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = crud.delete_expense(db, expense_id)

    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    return {
        "message": "Expense deleted successfully"
    }
    
@router.get("/filter/date/{expense_date}", response_model=List[ExpenseResponse])
def fetch_expenses_by_date(expense_date: date, db: Session = Depends(get_db)):
    return crud.get_expenses_by_date(db, expense_date)


@router.get("/summary/month/{year}/{month}")
def fetch_monthly_summary(year: int, month: int, db: Session = Depends(get_db)):
    return crud.get_monthly_summary(db, year, month)