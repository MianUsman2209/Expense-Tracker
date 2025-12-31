from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from app.database.session import get_db
from app.models.expense import Expense
from app.models.user import User
from app.schemas.expense import ExpenseResponse
from app.api.deps import get_current_admin

router = APIRouter(prefix="/admin/expenses", tags=["admin-expenses"])

@router.get("/", response_model=List[ExpenseResponse])
def get_all_expenses(
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin),
    filter: Optional[str] = Query(None),
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None
):
    query = db.query(Expense)

    if filter == "past_week":
        query = query.filter(Expense.date >= datetime.utcnow() - timedelta(weeks=1))
    elif filter == "past_month":
        query = query.filter(Expense.date >= datetime.utcnow() - timedelta(days=30))
    elif filter == "last_3_months":
        query = query.filter(Expense.date >= datetime.utcnow() - timedelta(days=90))
    elif start_date and end_date:
        query = query.filter(Expense.date.between(start_date, end_date))

    return query.all()

@router.delete("/{expense_id}")
def delete_any_expense(
    expense_id: int,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    
    db.delete(expense)
    db.commit()
    return {"detail": "Expense deleted successfully"}
