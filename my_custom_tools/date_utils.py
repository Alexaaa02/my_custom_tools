from datetime import datetime, timedelta

def get_current_timestamp():
    """Возвращает текущую дату и время в читаемом формате."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def days_between(date_str1, date_str2):
    """Считает количество дней между двумя датами (ГГГГ-ММ-ДД)."""
    d1 = datetime.strptime(date_str1, "%Y-%m-%d")
    d2 = datetime.strptime(date_str2, "%Y-%m-%d")
    return abs((d2 - d1).days)
