from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional


class ExpenseCreate(BaseModel):
    title: str
    amount: float
    category: str
    payment_mode: str
    description: Optional[str] = None
    expense_date: Optional[date] = None


class ExpenseUpdate(BaseModel):
    title: Optional[str] = None
    amount: Optional[float] = None
    category: Optional[str] = None
    payment_mode: Optional[str] = None
    description: Optional[str] = None
    expense_date: Optional[date] = None


class ExpenseResponse(BaseModel):
    id: int
    title: str
    amount: float
    category: str
    payment_mode: str
    description: Optional[str] = None
    expense_date: date
    created_at: datetime

    class Config:
        from_attributes = True