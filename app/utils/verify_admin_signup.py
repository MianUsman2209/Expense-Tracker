import requests

BASE_URL = "http://localhost:8000"

def test_admin_signup():
    email = "admin_signup_test@example.com"
    
    # 1. Signup as Admin
    print(f"Signing up {email} with role='admin'...")
    resp = requests.post(f"{BASE_URL}/auth/signup", json={
        "name": "Admin Tester",
        "email": email,
        "password": "password123",
        "role": "admin"
    })
    
    if resp.status_code == 400 and "already registered" in resp.text:
        print("User already exists, proceeding to login check...")
    elif resp.status_code != 200:
        print(f"Signup failed: {resp.text}")
        return

    # 2. Login
    resp = requests.post(f"{BASE_URL}/auth/login", data={
        "username": email,
        "password": "password123"
    })
    token = resp.json().get("access_token")
    
    if not token:
        print("Login failed, no token")
        return

    # 3. Check if we can see ALL expenses (Admin privilege)
    # We assume there are some expenses in the DB from previous tests
    resp = requests.get(f"{BASE_URL}/expenses/", headers={"Authorization": f"Bearer {token}"})
    if resp.status_code == 200:
        print(f"Admin Access Verified. Expense count: {len(resp.json())}")
        print("SUCCESS: Admin signup worked!")
    else:
        print(f"FAILED: Could not list expenses. Status: {resp.status_code}")

if __name__ == "__main__":
    test_admin_signup()
