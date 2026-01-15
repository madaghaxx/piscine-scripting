def clean_list(lista):
    if not lista:
        return []
    new = []
    for i, item in enumerate(lista):
        klma = item.strip()
        klma = klma.capitalize()
        klma = f"{i+1}/ {klma}"
        new.append(klma)
    if not any("milk" in item.lower() for item in lista):
        new.append(f"{len(new)}x/ Milk")

    return new