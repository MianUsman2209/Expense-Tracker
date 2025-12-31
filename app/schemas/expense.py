from pydantic import BaseModel, field_validator
from datetime import datetime
from typing import Optional
from app.models.constants import CATEGORY_CHOICES

class ExpenseCreate(BaseModel):
    title: str
    amount: float
    category: str
    date: Optional[datetime] = None

    @field_validator('category')
    @classmethod
    def validate_category(cls, v):
        if v not in CATEGORY_CHOICES:
            raise ValueError(f'Category must be one of: {", ".join(CATEGORY_CHOICES)}')
        return v

    class Config:
        from_attributes = True

class ExpenseUpdate(BaseModel):
    title: Optional[str] = None
    amount: Optional[float] = None
    category: Optional[str] = None
    date: Optional[datetime] = None

    @field_validator('category')
    @classmethod
    def validate_category(cls, v):
        if v is not None and v not in CATEGORY_CHOICES:
            raise ValueError(f'Category must be one of: {", ".join(CATEGORY_CHOICES)}')
        return v

    class Config:
        from_attributes = True

class ExpenseResponse(BaseModel):
    id: int
    title: str
    amount: float
    category: str
    date: datetime
    user_id: int

    class Config:
        from_attributes = True

