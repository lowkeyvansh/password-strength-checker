import re

def check_password_strength(password):
    strength = {
        'length': len(password) >= 8,
        'digit': re.search(r"\d", password) is not None,
        'uppercase': re.search(r"[A-Z]", password) is not None,
        'lowercase': re.search(r"[a-z]", password) is not None,
        'special_char': re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None
    }
    return all(strength.values()), strength

password = input("Enter password: ")
is_strong, criteria = check_password_strength(password)
print(f"Password is {'strong' if is_strong else 'weak'}")
for criterion, met in criteria.items():
    print(f"{criterion.capitalize()}: {'Met' if met else 'Not met'}")
