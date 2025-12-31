import requests
import sys

BASE_URL = "http://localhost:8000"

def run_test():
    # 1. Signup Jane (if not exists)
    try:
        requests.post(f"{BASE_URL}/auth/signup", json={
            "name": "Jane Doe",
            "email": "jane@example.com",
            "password": "password123"
        })
    except:
        pass

    # 2. Login Jane
    resp = requests.post(f"{BASE_URL}/auth/login", data={
        "username": "jane@example.com",
        "password": "password123"
    })
    if resp.status_code != 200:
        print("Jane login failed")
        return
    token_jane = resp.json()["access_token"]
    
    # 3. Create Expense for Jane
    resp = requests.post(f"{BASE_URL}/expenses/", 
        json={"title": "Jane Expense", "amount": 10.0, "category": "Others", "date": "2025-12-17T12:00:00"},
        headers={"Authorization": f"Bearer {token_jane}"}
    )
    if resp.status_code != 200:
        print(f"Jane create expense failed: {resp.text}")
        return
    jane_expense_id = resp.json()["id"]
    print(f"Jane Created Expense ID: {jane_expense_id}")

    # 4. Login John (Admin)
    resp = requests.post(f"{BASE_URL}/auth/login", data={
        "username": "john@example.com",
        "password": "password123"
    })
    token_john = resp.json()["access_token"]

    # 5. List Expenses as John (Should see Jane's)
    resp = requests.get(f"{BASE_URL}/expenses/", headers={"Authorization": f"Bearer {token_john}"})
    expenses = resp.json()
    found = any(e["id"] == jane_expense_id for e in expenses)
    print(f"Admin see Jane's expense: {found}")

    # 6. Delete Jane's Expense as John
    resp = requests.delete(f"{BASE_URL}/expenses/{jane_expense_id}", headers={"Authorization": f"Bearer {token_john}"})
    if resp.status_code == 200:
        print("Admin deleted Jane's expense: Success")
    else:
        print(f"Admin delete failed: {resp.status_code} {resp.text}")

if __name__ == "__main__":
    run_test()
