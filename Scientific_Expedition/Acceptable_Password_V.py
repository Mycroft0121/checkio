def is_acceptable_password(password: str) -> bool:
    # your code here
    l =len(password)
    return ("password" not in password.lower()) and ((l>6 and any(char.isdigit() for char in password) and not all(char.isdigit() for char in password)) or l>9)

