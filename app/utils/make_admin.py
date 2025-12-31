import sys
from app.database.session import SessionLocal
from app.models.user import User

def make_admin(email: str):
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.email == email).first()
        if user:
            user.role = "admin"
            db.commit()
            print(f"SUCCESS: User '{email}' has been promoted to ADMIN.")
        else:
            print(f"ERROR: User '{email}' not found. Please sign up first.")
    finally:
        db.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python app/utils/make_admin.py <email>")
        print("Example: python app/utils/make_admin.py john@example.com")
    else:
        make_admin(sys.argv[1])
