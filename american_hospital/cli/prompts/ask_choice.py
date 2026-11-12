from cli.display.print_message import print_error

def ask_choice(label: str, options: tuple | list) -> str:
    print(label)
    for i, opt in enumerate(options, start=1):
        print(f"  {i}. {opt}")
    while True:
        raw = input("Choix : ").strip()
        if raw.isdigit() and 1 <= int(raw) <= len(options):
            return options[int(raw) - 1]
        print_error("Numéro invalide.")