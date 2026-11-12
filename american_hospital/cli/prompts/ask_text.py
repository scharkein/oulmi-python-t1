from cli.display.print_message import print_error

def ask_text(label: str, validator=None, allow_empty: bool = False) -> str:
    while True:
        value = input(f"{label} : ").strip()
        if not value and not allow_empty:
            print_error("Champ obligatoire.")
            continue
        if value and validator and not validator(value):
            print_error("Valeur invalide.")
            continue
        return value