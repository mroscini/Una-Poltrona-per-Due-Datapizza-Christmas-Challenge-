from datapizza.type import TextBlock, ROLE
from datapizza.memory import Memory
from utils.memory_store import save_memory_text

from agents import create_duke, create_winthorpe, create_valentine
from ui_writer import write_line


def run():
    # 1️⃣ Regole ufficiali del trading day (note a tutti)
    with open("docs/act16_trading_day_rules.md", "r", encoding="utf-8") as f:
        rules_text = f.read()

    # =====================
    # DUKE
    # =====================
    duke_memory = Memory()
    duke_memory.add_turn(
        TextBlock(
            content=(
                "REGOLE UFFICIALI DEL TRADING DAY\n\n"
                + rules_text
            )
        ),
        role=ROLE.SYSTEM,
    )

    duke = create_duke(memory=duke_memory)

    d = duke.run(
        "Agisci sul mercato con sicurezza, convinto che le informazioni "
        "sul raccolto di arance in tuo possesso siano corrette."
    )
    write_line("DUKE", d.text)

    # =====================
    # WINTHORPE
    # =====================
    winthorpe_memory = Memory()
    winthorpe_memory.add_turn(
        TextBlock(
            content=(
                "REGOLE UFFICIALI DEL TRADING DAY\n\n"
                + rules_text
            )
        ),
        role=ROLE.SYSTEM,
    )

    winthorpe = create_winthorpe(memory=winthorpe_memory)

    w = winthorpe.run(
        "Osserva l’andamento del mercato durante il trading day. "
        "Riconosci gli errori dei Duke e anticipa le conseguenze."
    )
    write_line("WINTHORPE", w.text)

    # =====================
    # VALENTINE
    # =====================
    valentine_memory = Memory()
    valentine_memory.add_turn(
        TextBlock(
            content=(
                "REGOLE UFFICIALI DEL TRADING DAY\n\n"
                + rules_text
            )
        ),
        role=ROLE.SYSTEM,
    )

    valentine = create_valentine(memory=valentine_memory)

    v = valentine.run(
        "Metti in atto la strategia pianificata con Winthorpe durante il trading day, "
        "sfruttando le mosse sbagliate dei Duke."
    )
    write_line("VALENTINE", v.text)

    # =====================
    # SALVATAGGIO MEMORIA EPISODIO
    # =====================
    episode_memory = f"""
    EPISODIO FINALE – IL TRADING DAY

    REGOLE DEL MERCATO:
    {rules_text}

    AZIONE DEI DUKE:
    {d.text}

    OSSERVAZIONE DI WINTHORPE:
    {w.text}

    ESECUZIONE DI VALENTINE:
    {v.text}
    """

    save_memory_text(
        episode_memory,
        episode="episode_trading_day"
    )


if __name__ == "__main__":
    run()
