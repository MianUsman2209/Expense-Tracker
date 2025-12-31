from fastapi import FastAPI
from app.api.routes import auth, expenses
from app.api.routes.admin import user as admin_users, expense as admin_expenses
from app.database.session import init_db

app = FastAPI(title="Expense Tracker API")

# Create tables if they don't exist
init_db()

# Include routes
app.include_router(auth.router)
app.include_router(expenses.router)
app.include_router(admin_users.router)
app.include_router(admin_expenses.router)
