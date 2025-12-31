from datapizza.type import TextBlock, ROLE
from datapizza.memory import Memory
from utils.memory_store import save_memory_text

from agents import create_valentine
from ui_writer import write_line


def run():
    # 1️⃣ Documento di promozione (diegetico)
    with open("docs/act06_valentine_promotion.md", "r", encoding="utf-8") as f:
        promotion_text = f.read()

    # 2️⃣ Memory SOLO per Valentine
    memory = Memory()
    memory.add_turn(
        TextBlock(
            content=(
                "COMUNICAZIONE INTERNA – FRATELLI DUKE\n\n"
                "OGGETTO: PROMOZIONE DI BILLY RAY VALENTINE\n\n"
                + promotion_text
            )
        ),
        role=ROLE.SYSTEM,  # documento autorevole
    )

    # 3️⃣ Crea Valentine con memoria
    valentine = create_valentine(memory=memory)

    # 4️⃣ Azione narrativa
    result = valentine.run(
        "Racconta in italiano la tua promozione, spiegando perché la consideri meritata. "
        "Mostra entusiasmo, gratitudine e fiducia nei fratelli Duke."
    )

    write_line("VALENTINE", result.text)

    # 5️⃣ Salva SOLO testo (non Memory)
    episode_memory = f"""
    EPISODIO 3 – LA PROMOZIONE DI VALENTINE

    DOCUMENTO DI PROMOZIONE:
    {promotion_text}

    REAZIONE DI VALENTINE:
    {result.text}
    """

    save_memory_text(episode_memory, episode="episode_03")


if __name__ == "__main__":
    run()
