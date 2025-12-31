import json
from pathlib import Path
from threading import Lock

DIALOGUE_PATH = Path("ui/dialogue.json")
_LOCK = Lock()


def write_line(character: str, text: str):
    """
    Scrive una riga di dialogo per la UI live.
    Viene chiamata dagli eventi DOPO che un agente ha parlato.
    """

    with _LOCK:
        if DIALOGUE_PATH.exists():
            try:
                data = json.loads(DIALOGUE_PATH.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                data = []
        else:
            data = []

        data.append(
            {
                "character": character.upper(),
                "text": text.strip(),
            }
        )

        DIALOGUE_PATH.parent.mkdir(parents=True, exist_ok=True)
        DIALOGUE_PATH.write_text(
            json.dumps(data, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
