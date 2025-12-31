from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from typing import List, Optional

from app.database.session import get_db
from app.models.expense import Expense
from app.schemas.expense import ExpenseCreate, ExpenseUpdate, ExpenseResponse
from app.api.deps import get_current_user
from app.models.user import User

router = APIRouter(prefix="/expenses", tags=["expenses"])

# Add expense
@router.post("/", response_model=ExpenseResponse)
def add_expense(
    expense: ExpenseCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_expense = Expense(
        title=expense.title,
        amount=expense.amount,
        category=expense.category,
        date=expense.date or datetime.utcnow(),
        user_id=current_user.id
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense

# List expenses with optional filters
@router.get("/", response_model=List[ExpenseResponse])
def list_expenses(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    filter: Optional[str] = Query(None),
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None
):
    # User sees own expenses only
    query = db.query(Expense).filter(Expense.user_id == current_user.id)

    if filter == "past_week":
        query = query.filter(Expense.date >= datetime.utcnow() - timedelta(weeks=1))
    elif filter == "past_month":
        query = query.filter(Expense.date >= datetime.utcnow() - timedelta(days=30))
    elif filter == "last_3_months":
        query = query.filter(Expense.date >= datetime.utcnow() - timedelta(days=90))
    elif start_date and end_date:
        query = query.filter(Expense.date.between(start_date, end_date))

    return query.all()

# Update expense
@router.put("/{expense_id}", response_model=ExpenseResponse)
def update_expense(
    expense_id: int,
    expense: ExpenseUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # User can update only own
    query = db.query(Expense).filter(Expense.id == expense_id, Expense.user_id == current_user.id)
        
    existing = query.first()
    
    if not existing:
        raise HTTPException(status_code=404, detail="Expense not found")

    # Update only fields that were provided
    for field, value in expense.model_dump(exclude_unset=True).items():
        setattr(existing, field, value)
    
    db.commit()
    db.refresh(existing)
    return existing

