from datapizza.type import TextBlock, ROLE
from datapizza.memory import Memory
from utils.memory_store import save_memory_text

from agents import create_valentine
from ui_writer import write_line


def run():
    # 1️⃣ Documento scoperto da Valentine
    with open("docs/act10_valentine_discovers_truth.md", "r", encoding="utf-8") as f:
        truth_text = f.read()

    # 2️⃣ Memory SOLO per Valentine (verità finalmente chiara)
    memory = Memory()
    memory.add_turn(
        TextBlock(
            content=(
                "DOCUMENTI CONFIDENZIALI – SCOPERTA PERSONALE\n\n"
                + truth_text
            )
        ),
        role=ROLE.SYSTEM,  # per Valentine ora è verità incontestabile
    )

    # 3️⃣ Crea Valentine con memoria
    valentine = create_valentine(memory=memory)

    # 4️⃣ Azione narrativa
    result = valentine.run(
        "Rifletti su ciò che hai appena scoperto. "
        "Realizza di essere stato usato in un esperimento. "
        "Mostra rabbia, lucidità improvvisa e desiderio di rivalsa."
    )

    # 5️⃣ Output verso UI
    write_line("VALENTINE", result.text)

    # 6️⃣ Salva SOLO testo
    episode_memory = f"""
    EPISODIO – VALENTINE SCOPRE LA VERITÀ

    DOCUMENTO SCOPERTO:
    {truth_text}

    REAZIONE DI VALENTINE:
    {result.text}
    """

    save_memory_text(episode_memory, episode="episode_valentine_discovers_truth")


if __name__ == "__main__":
    run()
