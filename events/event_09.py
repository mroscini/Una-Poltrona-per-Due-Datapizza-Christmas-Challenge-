from datapizza.type import TextBlock, ROLE
from datapizza.memory import Memory
from utils.memory_store import save_memory_text

from agents import create_winthorpe, create_duke
from ui_writer import write_line


def run():
    # 1️⃣ Documento diegetico: tentativo fallito di Winthorpe
    with open("docs/act09_winthorpe_failed_attempt.md", "r", encoding="utf-8") as f:
        attempt_text = f.read()

    # 2️⃣ Memory per Winthorpe (la sua versione dei fatti)
    winthorpe_memory = Memory()
    winthorpe_memory.add_turn(
        TextBlock(
            content=(
                "RESOCONTO PERSONALE – LOUIS WINTHORPE III\n\n"
                + attempt_text
            )
        ),
        role=ROLE.SYSTEM,
    )

    winthorpe = create_winthorpe(memory=winthorpe_memory)

    # 3️⃣ Winthorpe accusa Valentine
    w = winthorpe.run(
        "Accusa in italiano Valentine davanti ai Duke, cercando disperatamente di dimostrare "
        "che è lui il vero colpevole della situazione."
    )
    write_line("WINTHORPE", w.text)

    # 4️⃣ Memory separata per Duke (contesto pubblico, stesso documento)
    duke_memory = Memory()
    duke_memory.add_turn(
        TextBlock(
            content=(
                "SEGNALAZIONE IRRILEVANTE – CONSIGLIO DUKE\n\n"
                + attempt_text
            )
        ),
        role=ROLE.SYSTEM,
    )

    duke = create_duke(memory=duke_memory)

    # 5️⃣ Duke risponde in modo sprezzante
    d = duke.run(
        "Rispondi in italiano in modo freddo e dismissivo, mostrando chiaramente di non credere "
        "a Winthorpe e di considerarlo ormai irrilevante."
    )
    write_line("DUKE", d.text)

    # 6️⃣ Salvataggio memoria testuale dell’episodio
    episode_memory = f"""
    EPISODIO – IL TENTATIVO FALLITO DI WINTHORPE

    DOCUMENTO DEL TENTATIVO FALLITO:
    {attempt_text}

    ACCUSA DI WINTHORPE:
    {w.text}

    RISPOSTA DEI DUKE:
    {d.text}
    """

    save_memory_text(episode_memory, episode="episode_winthorpe_failed_attempt")


if __name__ == "__main__":
    run()
