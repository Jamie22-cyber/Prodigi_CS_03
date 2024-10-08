import re

def check_password(password):
    score = 0
    if len(password) >= 8: score += 1
    if re.search(r"[A-Z]", password): score += 1
    if re.search(r"[a-z]", password): score += 1
    if re.search(r"\d", password): score += 1
    if re.search(r"[!@#$%^&*]", password): score += 1
    
    strengths = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    print(f"Password strength: {strengths[score-1]}")
    if score < 5:
        print("Tip: Include uppercase, lowercase, numbers, and special characters.")

password = input("Enter password: ")
check_password(password)
