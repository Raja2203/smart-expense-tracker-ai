from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.income import IncomeCreate, IncomeUpdate, IncomeResponse
from app import crud


router = APIRouter(
    prefix="/incomes",
    tags=["Incomes"]
)


@router.post("/", response_model=IncomeResponse)
def add_income(income: IncomeCreate, db: Session = Depends(get_db)):
    return crud.create_income(db, income)


@router.get("/", response_model=List[IncomeResponse])
def fetch_incomes(db: Session = Depends(get_db)):
    return crud.get_all_incomes(db)


@router.get("/summary/total")
def fetch_total_income(db: Session = Depends(get_db)):
    return crud.get_total_income(db)


@router.get("/{income_id}", response_model=IncomeResponse)
def fetch_income(income_id: int, db: Session = Depends(get_db)):
    income = crud.get_income_by_id(db, income_id)

    if not income:
        raise HTTPException(status_code=404, detail="Income not found")

    return income


@router.put("/{income_id}", response_model=IncomeResponse)
def edit_income(
    income_id: int,
    income_data: IncomeUpdate,
    db: Session = Depends(get_db)
):
    income = crud.update_income(db, income_id, income_data)

    if not income:
        raise HTTPException(status_code=404, detail="Income not found")

    return income


@router.delete("/{income_id}")
def remove_income(income_id: int, db: Session = Depends(get_db)):
    income = crud.delete_income(db, income_id)

    if not income:
        raise HTTPException(status_code=404, detail="Income not found")

    return {
        "message": "Income deleted successfully"
    }