import re

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^a-z0-9\sáéíóúâêîôûãõç]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text
