from datapizza.type import TextBlock, ROLE
from datapizza.memory import Memory
from utils.memory_store import save_memory_text

from agents import create_duke
from ui_writer import write_line


def run():
    # 1️⃣ Documento FALSO visto SOLO dai Duke
    with open("docs/act15_orange_crop_fake.md", "r", encoding="utf-8") as f:
        fake_report_text = f.read()

    # 2️⃣ Memory SOLO per Duke (verità percepita, ma sbagliata)
    memory = Memory()
    memory.add_turn(
        TextBlock(
            content=(
                "REPORT CONFIDENZIALE – PREVISIONI RACCOLTO DI ARANCE\n\n"
                "⚠️ DOCUMENTO NON VERIFICATO ⚠️\n\n"
                + fake_report_text
            )
        ),
        role=ROLE.SYSTEM,  # per Duke è fonte autorevole (anche se falsa)
    )

    duke = create_duke(memory=memory)

    # 3️⃣ Duke valuta il report falso
    result = duke.run(
        "Valuta il report che indica una grave scarsità nel raccolto di arance. "
        "Agisci con sicurezza, convinto che le informazioni siano corrette."
    )

    # 4️⃣ Output verso UI
    write_line("DUKE", result.text)

    # 5️⃣ Salva SOLO testo (memoria narrativa)
    episode_memory = f"""
    EPISODIO – IL REPORT FALSO SUL RACCOLTO DI ARANCE (DUKE)

    DOCUMENTO FALSO:
    {fake_report_text}

    VALUTAZIONE DEI DUKE:
    {result.text}
    """

    save_memory_text(
            episode_memory,
            episode="episode_duke_fake_orange_report"
        )


if __name__ == "__main__":
    run()
