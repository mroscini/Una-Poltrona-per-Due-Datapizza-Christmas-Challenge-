from agents import create_duke, create_winthorpe
from ui_writer import write_line
from utils.memory_store import save_memory_text

def run():
    # 1️⃣ Crea gli agenti (senza documenti riservati)
    duke = create_duke()
    winthorpe = create_winthorpe()

    # 2️⃣ Duke accusa
    d = duke.run(
        "Accusa in Italiano Winthorpe davanti al consiglio e giustifica le tue azioni."
    )
    write_line("DUKE", d.text)

    # 3️⃣ Winthorpe risponde conoscendo l'accusa
    w = winthorpe.run(
        f"""
Questa è l'accusa mossa contro di te:

{d.text}

Difenditi punto per punto.
"""
    )
    write_line("WINTHORPE", w.text)

    # 4️⃣ Salva memoria episodio
    episode_memory = f"""
    EPISODIO 2 – ACCUSA PUBBLICA

    ACCUSA (DUKE):
    {d.text}

    DIFESA (WINTHORPE):
    {w.text}
    """

    save_memory_text(episode_memory, episode="episode_02")

if __name__ == "__main__":
    run()
