# stato narrativo globale (runtime)
REVEALED_SOURCES = set()

def reveal(sources):
    for s in sources:
        REVEALED_SOURCES.add(s)
