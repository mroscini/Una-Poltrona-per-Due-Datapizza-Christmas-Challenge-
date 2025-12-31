from datapizza.type import TextBlock, ROLE
from datapizza.memory import Memory
from utils.memory_store import save_memory_text

from agents import create_winthorpe, create_valentine
from ui_writer import write_line


def run():
    # 1️⃣ Documenti diegetici scoperti
    with open("docs/act12_13_duke_information_abuse.md", "r", encoding="utf-8") as f:
        abuse_text = f.read()

    with open("docs/act12_13_orange_report_objective.md", "r", encoding="utf-8") as f:
        orange_report_text = f.read()

    combined_docs = (
        "DOCUMENTO A – ABUSO DI INFORMAZIONI RISERVATE\n\n"
        + abuse_text
        + "\n\n"
        + "DOCUMENTO B – REPORT OBIETTIVO SUL RACCOLTO DI ARANCE\n\n"
        + orange_report_text
    )

    # 2️⃣ Memory per Winthorpe
    winthorpe_memory = Memory()
    winthorpe_memory.add_turn(
        TextBlock(content=combined_docs),
        role=ROLE.SYSTEM,
    )

    winthorpe = create_winthorpe(memory=winthorpe_memory)

    # 3️⃣ Winthorpe ragiona
    w = winthorpe.run(
        "Ragiona su come i Duke ottengono un vantaggio sleale sul mercato "
        "sfruttando informazioni riservate."
    )
    write_line("WINTHORPE", w.text)

    # 4️⃣ Memory per Valentine (stessi documenti)
    valentine_memory = Memory()
    valentine_memory.add_turn(
        TextBlock(content=combined_docs),
        role=ROLE.SYSTEM,
    )

    valentine = create_valentine(memory=valentine_memory)

    # 5️⃣ Valentine trasforma l’intuizione in un piano
    v = valentine.run(
        f"""
        Winthorpe ha capito questo:

        {w.text}

        Trasforma questa intuizione in una strategia concreta per colpire i Duke
        sul loro stesso terreno.
        """
    )
    write_line("VALENTINE", v.text)

    # 6️⃣ Salvataggio memoria testuale dell’episodio
    episode_memory = f"""
    EPISODIO – LA SCOPERTA DELL’ABUSO DI INFORMAZIONI

    DOCUMENTI:
    {combined_docs}

    ANALISI DI WINTHORPE:
    {w.text}

    PIANO DI VALENTINE:
    {v.text}
    """

    save_memory_text(
        episode_memory,
        episode="episode_information_abuse_discovered"
    )


if __name__ == "__main__":
    run()
