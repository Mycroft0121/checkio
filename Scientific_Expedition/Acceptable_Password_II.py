def is_acceptable_password(password: str) -> bool:
    # your code here
    return len(password)>6 and any(char.isdigit() for char in password)