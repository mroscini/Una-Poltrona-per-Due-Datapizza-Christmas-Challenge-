from datapizza.type import TextBlock, ROLE
from datapizza.memory import Memory
from utils.memory_store import save_memory_text

from agents import create_winthorpe, create_valentine
from ui_writer import write_line


def run():
    # 1️⃣ Documento ufficiale sul raccolto di arance
    with open("docs/act14_orange_crop_real.md", "r", encoding="utf-8") as f:
        orange_crop_text = f.read()

    # 2️⃣ Memory per Winthorpe (analisi tecnica)
    winthorpe_memory = Memory()
    winthorpe_memory.add_turn(
        TextBlock(
            content=(
                "REPORT UFFICIALE – RACCOLTO DI ARANCE\n\n"
                + orange_crop_text
            )
        ),
        role=ROLE.SYSTEM,
    )

    winthorpe = create_winthorpe(memory=winthorpe_memory)

    # 3️⃣ Winthorpe analizza il report
    w = winthorpe.run(
        "Analizza il report ufficiale sul raccolto di arance, "
        "traendone le implicazioni economiche principali."
    )
    write_line("WINTHORPE", w.text)

    # 4️⃣ Memory per Valentine (stesso documento)
    valentine_memory = Memory()
    valentine_memory.add_turn(
        TextBlock(
            content=(
                "REPORT UFFICIALE – RACCOLTO DI ARANCE\n\n"
                + orange_crop_text
            )
        ),
        role=ROLE.SYSTEM,
    )

    valentine = create_valentine(memory=valentine_memory)

    # 5️⃣ Valentine valuta la strategia
    v = valentine.run(
        f"""
        Winthorpe ha concluso questo:

        {w.text}

        Valuta come sfruttare il fatto che il raccolto sarà abbondante
        per ribaltare la posizione dei Duke sul mercato.
        """
    )
    write_line("VALENTINE", v.text)

    # 6️⃣ Salvataggio memoria testuale dell’episodio
    episode_memory = f"""
    EPISODIO – IL REPORT REALE SUL RACCOLTO DI ARANCE

    DOCUMENTO UFFICIALE:
    {orange_crop_text}

    ANALISI DI WINTHORPE:
    {w.text}

    VALUTAZIONE STRATEGICA DI VALENTINE:
    {v.text}
    """

    save_memory_text(
        episode_memory,
        episode="episode_orange_crop_real"
    )


if __name__ == "__main__":
    run()
