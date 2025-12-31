from datapizza.type import TextBlock, ROLE
from datapizza.memory import Memory
from utils.memory_store import save_memory_text

from agents import create_valentine, create_winthorpe
from ui_writer import write_line


def run():
    # 1️⃣ Documento diegetico: nascita dell’alleanza
    with open("docs/act11_alliance_formed.md", "r", encoding="utf-8") as f:
        alliance_text = f.read()

    # 2️⃣ Memory per Valentine (nuova consapevolezza)
    valentine_memory = Memory()
    valentine_memory.add_turn(
        TextBlock(
            content=(
                "INFORMAZIONI CONDIVISE – NUOVA ALLEANZA\n\n"
                + alliance_text
            )
        ),
        role=ROLE.SYSTEM,
    )

    valentine = create_valentine(memory=valentine_memory)

    # 3️⃣ Valentine parla per primo
    v = valentine.run(
        "Parla con Winthorpe e spiega con chiarezza cosa hai capito della situazione, "
        "rivelando l’esperimento dei Duke e proponendo un’alleanza."
    )
    write_line("VALENTINE", v.text)

    # 4️⃣ Memory per Winthorpe (stesso documento, prospettiva diversa)
    winthorpe_memory = Memory()
    winthorpe_memory.add_turn(
        TextBlock(
            content=(
                "RIVELAZIONE INASPETTATA – POSSIBILE ALLEANZA\n\n"
                + alliance_text
            )
        ),
        role=ROLE.SYSTEM,
    )

    winthorpe = create_winthorpe(memory=winthorpe_memory)

    # 5️⃣ Winthorpe reagisce
    w = winthorpe.run(
        f"""
        Valentine ti ha appena detto questo:

        {v.text}

        Valuta se fidarti di lui e rispondi di conseguenza.
        """
    )
    write_line("WINTHORPE", w.text)

    # 6️⃣ Salvataggio memoria testuale dell’episodio
    episode_memory = f"""
        EPISODIO – L’ALLEANZA TRA VALENTINE E WINTHORPE

        DOCUMENTO DELL’ALLEANZA:
        {alliance_text}

        POSIZIONE DI VALENTINE:
        {v.text}

        RISPOSTA DI WINTHORPE:
        {w.text}
        """

    save_memory_text(episode_memory, episode="episode_alliance_formed")


if __name__ == "__main__":
    run()
