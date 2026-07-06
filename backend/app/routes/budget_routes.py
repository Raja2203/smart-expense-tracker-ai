from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.budget import BudgetCreate, BudgetUpdate, BudgetResponse
from app import crud


router = APIRouter(
    prefix="/budgets",
    tags=["Budgets"]
)


@router.post("/", response_model=BudgetResponse)
def add_budget(budget: BudgetCreate, db: Session = Depends(get_db)):
    return crud.create_budget(db, budget)


@router.get("/", response_model=List[BudgetResponse])
def fetch_budgets(db: Session = Depends(get_db)):
    return crud.get_all_budgets(db)


@router.get("/month/{year}/{month}", response_model=List[BudgetResponse])
def fetch_monthly_budgets(year: int, month: int, db: Session = Depends(get_db)):
    return crud.get_monthly_budgets(db, year, month)


@router.get("/{budget_id}", response_model=BudgetResponse)
def fetch_budget(budget_id: int, db: Session = Depends(get_db)):
    budget = crud.get_budget_by_id(db, budget_id)

    if not budget:
        raise HTTPException(status_code=404, detail="Budget not found")

    return budget


@router.put("/{budget_id}", response_model=BudgetResponse)
def edit_budget(
    budget_id: int,
    budget_data: BudgetUpdate,
    db: Session = Depends(get_db)
):
    budget = crud.update_budget(db, budget_id, budget_data)

    if not budget:
        raise HTTPException(status_code=404, detail="Budget not found")

    return budget


@router.delete("/{budget_id}")
def remove_budget(budget_id: int, db: Session = Depends(get_db)):
    budget = crud.delete_budget(db, budget_id)

    if not budget:
        raise HTTPException(status_code=404, detail="Budget not found")

    return {
        "message": "Budget deleted successfully"
    }