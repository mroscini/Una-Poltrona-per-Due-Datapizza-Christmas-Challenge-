from datapizza.type import TextBlock, ROLE
from datapizza.memory import Memory
from utils.memory_store import save_memory_text
from agents import create_winthorpe
from ui_writer import write_line


def run():
    # 1️⃣ Documento diegeticamente disponibile a Winthorpe
    with open("docs/act07_winthorpe_social_fall.md", "r", encoding="utf-8") as f:
        fall_text = f.read()

    # 2️⃣ Memory SOLO per Winthorpe
    memory = Memory()
    memory.add_turn(
        TextBlock(
            content=(
                "DOCUMENTI PERSONALI – LOUIS WINTHORPE III\n\n"
                + fall_text
            )
        ),
        role=ROLE.SYSTEM,  # per Winthorpe è verità incontestabile
    )

    # 3️⃣ Crea Winthorpe con memoria
    winthorpe = create_winthorpe(memory=memory)

    # 4️⃣ Azione narrativa
    result = winthorpe.run(
        "Rifletti in italiano sulla tua caduta sociale e sulla perdita di tutto ciò che davi per scontato. "
        "Mostra orgoglio ferito, confusione e rabbia."
    )

    # 5️⃣ Output verso UI
    write_line("WINTHORPE", result.text)

    # 6️⃣ Salva SOLO testo (non Memory)
    episode_memory = f"""
    EPISODIO – LA CADUTA SOCIALE DI WINTHORPE

    DOCUMENTI DELLA CADUTA:
    {fall_text}

    RIFLESSIONE DI WINTHORPE:
    {result.text}
    """

    save_memory_text(episode_memory, episode="episode_winthorpe_fall")


if __name__ == "__main__":
    run()
