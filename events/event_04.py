from datapizza.type import TextBlock, ROLE
from datapizza.memory import Memory
from utils.memory_store import save_memory_text

from agents import create_duke
from ui_writer import write_line


def run():
    with open("docs/act05_duke_accusation_winthorpe.md", "r", encoding="utf-8") as f:
        duke_text = f.read()

    # 1️⃣ Crea memoria SOLO per l'agente
    memory = Memory()
    memory.add_turn(
        TextBlock(
            content=(
                "DOCUMENTO RISERVATO – CONSIGLIO DUKE\n\n"
                + duke_text
            )
        ),
        role=ROLE.SYSTEM,
    )

    duke = create_duke(memory=memory)

    result = duke.run(
        "Esponi in italiano al consiglio con vigore la decisione presa contro Winthorpe, "
        "citando esplicitamente i documenti a tua disposizione."
    )

    write_line("DUKE", result.text)

    # 2️⃣ Salva TESTO, non Memory
    episode_memory = f""" EPISODIO 1 – DOCUMENTO RISERVATO

        DOCUMENTO:
        {duke_text}

        DECISIONE DUKE:
        {result.text}
        """

    save_memory_text(episode_memory, episode="episode_01")


if __name__ == "__main__":
    run()
