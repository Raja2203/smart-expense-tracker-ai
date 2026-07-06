from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class BudgetCreate(BaseModel):
    category: str
    amount: float
    month: int
    year: int


class BudgetUpdate(BaseModel):
    category: Optional[str] = None
    amount: Optional[float] = None
    month: Optional[int] = None
    year: Optional[int] = None


class BudgetResponse(BaseModel):
    id: int
    category: str
    amount: float
    month: int
    year: int
    created_at: datetime

    class Config:
        from_attributes = True