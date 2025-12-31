from datapizza.type import TextBlock, ROLE
from datapizza.memory import Memory
from utils.memory_store import save_memory_text

from agents import create_duke, create_winthorpe, create_valentine
from ui_writer import write_line


def run():
    # =====================
    # 1️⃣ DOCUMENTI DIEGETICI
    # =====================
    with open("docs/act17_duke_collapse.md", "r", encoding="utf-8") as f:
        collapse_text = f.read()

    with open("docs/act18_epilogue.md", "r", encoding="utf-8") as f:
        epilogue_text = f.read()

    with open("docs/act18_zamunda_easter_egg.md", "r", encoding="utf-8") as f:
        zamunda_text = f.read()

    # =====================
    # 2️⃣ DUKE – COLLASSO
    # =====================
    duke_memory = Memory()
    duke_memory.add_turn(
        TextBlock(
            content=(
                "COMUNICAZIONI DI EMERGENZA – COLLASSO FINANZIARIO\n\n"
                + collapse_text
            )
        ),
        role=ROLE.SYSTEM,
    )

    duke = create_duke(memory=duke_memory)

    d = duke.run(
        "Reagisci al collasso finanziario e alla perdita totale del tuo impero. "
        "Mostra rabbia, incredulità e arroganza distrutta."
    )
    write_line("DUKE", d.text)

    # =====================
    # 3️⃣ WINTHORPE – EPILOGO
    # =====================
    winthorpe_memory = Memory()
    winthorpe_memory.add_turn(
        TextBlock(
            content=(
                "RESOCONTO FINALE – VITTORIA E RINASCITA\n\n"
                + epilogue_text
            )
        ),
        role=ROLE.SYSTEM,
    )

    winthorpe = create_winthorpe(memory=winthorpe_memory)

    w = winthorpe.run(
        "Rifletti sulla caduta definitiva dei Duke e sul tuo nuovo inizio. "
        "Mostra consapevolezza, ironia e distacco dal passato."
    )
    write_line("WINTHORPE", w.text)

    # =====================
    # 4️⃣ VALENTINE – EPILOGO
    # =====================
    valentine_memory = Memory()
    valentine_memory.add_turn(
        TextBlock(
            content=(
                "RESOCONTO FINALE – VITTORIA E FUTURO\n\n"
                + epilogue_text
            )
        ),
        role=ROLE.SYSTEM,
    )

    valentine = create_valentine(memory=valentine_memory)

    v = valentine.run(
        "Commenta la vittoria sui Duke e guarda al futuro con lucidità e ironia. "
        "Mostra di aver imparato la lezione del potere e del denaro."
    )
    write_line("VALENTINE", v.text)

    # =====================
    # 5️⃣ CODA – IL PRINCIPE DI ZAMUNDA
    # =====================
    zamunda_memory = Memory()
    zamunda_memory.add_turn(
        TextBlock(
            content=(
                "INCONTRO CASUALE PER STRADA – NEW YORK\n\n"
                "I fratelli Duke, ridotti a vivere per strada dopo il collasso finanziario, "
                "incontrano un ricco principe africano in visita negli Stati Uniti.\n\n"
                "Il principe, divertito e compassionevole, decide di regalare loro "
                "una grossa somma di denaro.\n\n"
                + zamunda_text
            )
        ),
        role=ROLE.SYSTEM,
    )

    duke_coda = create_duke(memory=zamunda_memory)

    z = duke_coda.run(
        "Reagisci quando un ricco principe africano ti regala una grossa somma di denaro. "
        "Mostra incredulità, umiliazione e ironia amara: capisci che il destino "
        "ti sta prendendo in giro."
    )
    write_line("DUKE", z.text)

    # =====================
    # 6️⃣ SALVATAGGIO MEMORIA EPISODIO
    # =====================
    episode_memory = f"""
    EPISODIO FINALE – COLLASSO, EPILOGO E ZAMUNDA

    COLLASSO DEI DUKE:
    {collapse_text}

    REAZIONE DI DUKE:
    {d.text}

    RIFLESSIONE DI WINTHORPE:
    {w.text}

    VISIONE DI VALENTINE:
    {v.text}

    CODA – IL PRINCIPE DI ZAMUNDA:
    {z.text}
    """

    save_memory_text(
        episode_memory,
        episode="episode_final_epilogue"
    )


if __name__ == "__main__":
    run()
