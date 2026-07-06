from sqlalchemy.orm import Session
from app.models.expense import Expense
from app.schemas.expense import ExpenseCreate, ExpenseUpdate
from app.models.income import Income
from app.schemas.income import IncomeCreate, IncomeUpdate
from app.models.budget import Budget
from app.schemas.budget import BudgetCreate, BudgetUpdate
from sqlalchemy import func
from datetime import date


def create_expense(db: Session, expense: ExpenseCreate):
    new_expense = Expense(
    title=expense.title,
    amount=expense.amount,
    category=expense.category,
    payment_mode=expense.payment_mode,
    description=expense.description,
    expense_date=expense.expense_date
    )

    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)

    return new_expense


def get_all_expenses(db: Session):
    return db.query(Expense).all()


def get_expense_by_id(db: Session, expense_id: int):
    return db.query(Expense).filter(Expense.id == expense_id).first()


def update_expense(db: Session, expense_id: int, expense_data: ExpenseUpdate):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()

    if not expense:
        return None

    update_data = expense_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(expense, key, value)

    db.commit()
    db.refresh(expense)

    return expense


def delete_expense(db: Session, expense_id: int):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()

    if not expense:
        return None

    db.delete(expense)
    db.commit()

    return expense

def get_total_expense(db: Session):
    total = db.query(func.sum(Expense.amount)).scalar()

    return {
        "total_expense": total if total else 0
    }


def get_category_summary(db: Session):
    results = (
        db.query(
            Expense.category,
            func.sum(Expense.amount).label("total_amount")
        )
        .group_by(Expense.category)
        .all()
    )

    return [
        {
            "category": category,
            "total_amount": total_amount
        }
        for category, total_amount in results
    ]


def get_expenses_by_category(db: Session, category: str):
    return db.query(Expense).filter(Expense.category == category).all()


def get_expenses_by_payment_mode(db: Session, payment_mode: str):
    return db.query(Expense).filter(Expense.payment_mode == payment_mode).all()

def get_expenses_by_date(db: Session, expense_date: date):
    return (
        db.query(Expense)
        .filter(func.date(Expense.created_at) == expense_date)
        .all()
    )


def get_monthly_summary(db: Session, year: int, month: int):
    total = (
        db.query(func.sum(Expense.amount))
        .filter(func.extract("year", Expense.expense_date) == year)
        .filter(func.extract("month", Expense.expense_date) == month)
        .scalar()
    )

    category_results = (
        db.query(
            Expense.category,
            func.sum(Expense.amount).label("total_amount")
        )
        .filter(func.extract("year", Expense.expense_date) == year)
        .filter(func.extract("month", Expense.expense_date) == month)
        .group_by(Expense.category)
        .all()
    )

    return {
        "year": year,
        "month": month,
        "total_expense": total if total else 0,
        "category_summary": [
            {
                "category": category,
                "total_amount": total_amount
            }
            for category, total_amount in category_results
        ]
    }

def create_income(db: Session, income: IncomeCreate):
    new_income = Income(
        source=income.source,
        amount=income.amount,
        description=income.description,
        income_date=income.income_date
    )

    db.add(new_income)
    db.commit()
    db.refresh(new_income)

    return new_income


def get_all_incomes(db: Session):
    return db.query(Income).all()


def get_income_by_id(db: Session, income_id: int):
    return db.query(Income).filter(Income.id == income_id).first()


def update_income(db: Session, income_id: int, income_data: IncomeUpdate):
    income = db.query(Income).filter(Income.id == income_id).first()

    if not income:
        return None

    update_data = income_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(income, key, value)

    db.commit()
    db.refresh(income)

    return income


def delete_income(db: Session, income_id: int):
    income = db.query(Income).filter(Income.id == income_id).first()

    if not income:
        return None

    db.delete(income)
    db.commit()

    return income


def get_total_income(db: Session):
    total = db.query(func.sum(Income.amount)).scalar()

    return {
        "total_income": total if total else 0
    }

def get_dashboard_summary(db: Session):
    total_income = db.query(func.sum(Income.amount)).scalar()
    total_expense = db.query(func.sum(Expense.amount)).scalar()

    total_income = total_income if total_income else 0
    total_expense = total_expense if total_expense else 0

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": total_income - total_expense
    }
    
def get_monthly_dashboard_summary(db: Session, year: int, month: int):
    total_income = (
        db.query(func.sum(Income.amount))
        .filter(func.extract("year", Income.income_date) == year)
        .filter(func.extract("month", Income.income_date) == month)
        .scalar()
    )

    total_expense = (
        db.query(func.sum(Expense.amount))
        .filter(func.extract("year", Expense.expense_date) == year)
        .filter(func.extract("month", Expense.expense_date) == month)
        .scalar()
    )

    total_income = total_income if total_income else 0
    total_expense = total_expense if total_expense else 0

    return {
        "year": year,
        "month": month,
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": total_income - total_expense
    }
    
def get_expense_category_percentage_summary(db: Session):
    total_expense = db.query(func.sum(Expense.amount)).scalar()

    if not total_expense:
        return []

    category_results = (
        db.query(
            Expense.category,
            func.sum(Expense.amount).label("total_amount")
        )
        .group_by(Expense.category)
        .all()
    )

    return [
        {
            "category": category,
            "total_amount": total_amount,
            "percentage": round((total_amount / total_expense) * 100, 2)
        }
        for category, total_amount in category_results
    ]

def get_monthly_expense_category_percentage_summary(
    db: Session,
    year: int,
    month: int
):
    total_expense = (
        db.query(func.sum(Expense.amount))
        .filter(func.extract("year", Expense.expense_date) == year)
        .filter(func.extract("month", Expense.expense_date) == month)
        .scalar()
    )

    if not total_expense:
        return []

    category_results = (
        db.query(
            Expense.category,
            func.sum(Expense.amount).label("total_amount")
        )
        .filter(func.extract("year", Expense.expense_date) == year)
        .filter(func.extract("month", Expense.expense_date) == month)
        .group_by(Expense.category)
        .all()
    )

    return [
        {
            "category": category,
            "total_amount": total_amount,
            "percentage": round((total_amount / total_expense) * 100, 2)
        }
        for category, total_amount in category_results
    ]
    
def get_recent_transactions(db: Session, limit: int = 10):
    recent_expenses = (
        db.query(Expense)
        .order_by(Expense.created_at.desc())
        .limit(limit)
        .all()
    )

    recent_incomes = (
        db.query(Income)
        .order_by(Income.created_at.desc())
        .limit(limit)
        .all()
    )

    transactions = []

    for expense in recent_expenses:
        transactions.append({
            "id": expense.id,
            "type": "expense",
            "title": expense.title,
            "amount": expense.amount,
            "category": expense.category,
            "payment_mode": expense.payment_mode,
            "date": expense.expense_date,
            "created_at": expense.created_at
        })

    for income in recent_incomes:
        transactions.append({
            "id": income.id,
            "type": "income",
            "title": income.source,
            "amount": income.amount,
            "category": "Income",
            "payment_mode": None,
            "date": income.income_date,
            "created_at": income.created_at
        })

    transactions.sort(
        key=lambda item: item["created_at"],
        reverse=True
    )

    return transactions[:limit]

def get_monthly_recent_transactions(
    db: Session,
    year: int,
    month: int,
    limit: int = 10
):
    recent_expenses = (
        db.query(Expense)
        .filter(func.extract("year", Expense.expense_date) == year)
        .filter(func.extract("month", Expense.expense_date) == month)
        .order_by(Expense.created_at.desc())
        .limit(limit)
        .all()
    )

    recent_incomes = (
        db.query(Income)
        .filter(func.extract("year", Income.income_date) == year)
        .filter(func.extract("month", Income.income_date) == month)
        .order_by(Income.created_at.desc())
        .limit(limit)
        .all()
    )

    transactions = []

    for expense in recent_expenses:
        transactions.append({
            "id": expense.id,
            "type": "expense",
            "title": expense.title,
            "amount": expense.amount,
            "category": expense.category,
            "payment_mode": expense.payment_mode,
            "date": expense.expense_date,
            "created_at": expense.created_at
        })

    for income in recent_incomes:
        transactions.append({
            "id": income.id,
            "type": "income",
            "title": income.source,
            "amount": income.amount,
            "category": "Income",
            "payment_mode": None,
            "date": income.income_date,
            "created_at": income.created_at
        })

    transactions.sort(
        key=lambda item: item["created_at"],
        reverse=True
    )

    return transactions[:limit]

def create_budget(db: Session, budget: BudgetCreate):
    new_budget = Budget(
        category=budget.category,
        amount=budget.amount,
        month=budget.month,
        year=budget.year
    )

    db.add(new_budget)
    db.commit()
    db.refresh(new_budget)

    return new_budget


def get_all_budgets(db: Session):
    return db.query(Budget).all()


def get_budget_by_id(db: Session, budget_id: int):
    return db.query(Budget).filter(Budget.id == budget_id).first()


def update_budget(db: Session, budget_id: int, budget_data: BudgetUpdate):
    budget = db.query(Budget).filter(Budget.id == budget_id).first()

    if not budget:
        return None

    update_data = budget_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(budget, key, value)

    db.commit()
    db.refresh(budget)

    return budget


def delete_budget(db: Session, budget_id: int):
    budget = db.query(Budget).filter(Budget.id == budget_id).first()

    if not budget:
        return None

    db.delete(budget)
    db.commit()

    return budget


def get_monthly_budgets(db: Session, year: int, month: int):
    return (
        db.query(Budget)
        .filter(Budget.year == year)
        .filter(Budget.month == month)
        .all()
    )
    
def get_budget_vs_actual(db: Session, year: int, month: int):
    budgets = (
        db.query(Budget)
        .filter(Budget.year == year)
        .filter(Budget.month == month)
        .all()
    )

    result = []

    for budget in budgets:
        spent_amount = (
            db.query(func.sum(Expense.amount))
            .filter(Expense.category == budget.category)
            .filter(func.extract("year", Expense.expense_date) == year)
            .filter(func.extract("month", Expense.expense_date) == month)
            .scalar()
        )

        spent_amount = spent_amount if spent_amount else 0
        remaining_amount = budget.amount - spent_amount

        used_percentage = (
            round((spent_amount / budget.amount) * 100, 2)
            if budget.amount > 0
            else 0
        )

        status = "Within Budget"

        if spent_amount > budget.amount:
            status = "Over Budget"
        elif used_percentage >= 80:
            status = "Near Limit"

        result.append({
            "category": budget.category,
            "budget_amount": budget.amount,
            "spent_amount": spent_amount,
            "remaining_amount": remaining_amount,
            "used_percentage": used_percentage,
            "status": status
        })

    return result