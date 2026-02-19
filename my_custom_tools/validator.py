import re

def is_valid_email(email):
    """Проверяет, является ли строка корректным email-адресом."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def is_strong_password(password):
    """Проверяет пароль: минимум 8 символов и наличие цифр."""
    return len(password) >= 8 and any(char.isdigit() for char in password)
