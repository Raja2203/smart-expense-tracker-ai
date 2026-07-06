from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/summary")
def fetch_dashboard_summary(db: Session = Depends(get_db)):
    return crud.get_dashboard_summary(db)


@router.get("/summary/month/{year}/{month}")
def fetch_monthly_dashboard_summary(
    year: int,
    month: int,
    db: Session = Depends(get_db)
):
    return crud.get_monthly_dashboard_summary(db, year, month)


@router.get("/expense-category-summary")
def fetch_expense_category_percentage_summary(db: Session = Depends(get_db)):
    return crud.get_expense_category_percentage_summary(db)


@router.get("/expense-category-summary/month/{year}/{month}")
def fetch_monthly_expense_category_percentage_summary(
    year: int,
    month: int,
    db: Session = Depends(get_db)
):
    return crud.get_monthly_expense_category_percentage_summary(
        db,
        year,
        month
    )


@router.get("/recent-transactions")
def fetch_recent_transactions(
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return crud.get_recent_transactions(db, limit)


@router.get("/recent-transactions/month/{year}/{month}")
def fetch_monthly_recent_transactions(
    year: int,
    month: int,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return crud.get_monthly_recent_transactions(
        db,
        year,
        month,
        limit
    )
    
@router.get("/budget-vs-actual/{year}/{month}")
def fetch_budget_vs_actual(
    year: int,
    month: int,
    db: Session = Depends(get_db)
):
    return crud.get_budget_vs_actual(db, year, month)