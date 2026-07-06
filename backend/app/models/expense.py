from sqlalchemy import Column, Integer, String, Float, DateTime, Date
from datetime import datetime, date
from app.database import Base


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    amount = Column(Float, nullable=False)
    category = Column(String(50), nullable=False)
    payment_mode = Column(String(50), nullable=False)
    description = Column(String(255), nullable=True)
    expense_date = Column(Date, default=date.today, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)