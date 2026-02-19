def capitalize_words(text):
    """Делает заглавной первую букву каждого слова."""
    return text.title()

def count_vowels(text):
    """Считает количество гласных в тексте."""
    vowels = "aeiouаеёиоуыэюя"
    return sum(1 for char in text.lower() if char in vowels)
