import os

MEMORY_DIR = "memory"
os.makedirs(MEMORY_DIR, exist_ok=True)

def save_memory_text(text: str, episode: str):
    """
    Salva memoria narrativa come testo.
    """
    path = f"{MEMORY_DIR}/{episode}.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def load_memory_text(episode: str) -> str:
    """
    Carica memoria narrativa testuale.
    """
    path = f"{MEMORY_DIR}/{episode}.txt"
    if not os.path.exists(path):
        return ""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
