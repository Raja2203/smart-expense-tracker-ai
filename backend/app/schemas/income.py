from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional


class IncomeCreate(BaseModel):
    source: str
    amount: float
    description: Optional[str] = None
    income_date: Optional[date] = None


class IncomeUpdate(BaseModel):
    source: Optional[str] = None
    amount: Optional[float] = None
    description: Optional[str] = None
    income_date: Optional[date] = None


class IncomeResponse(BaseModel):
    id: int
    source: str
    amount: float
    description: Optional[str] = None
    income_date: date
    created_at: datetime

    class Config:
        from_attributes = True