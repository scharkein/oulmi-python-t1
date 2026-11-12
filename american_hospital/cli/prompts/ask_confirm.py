def ask_confirm(question: str) -> bool:
    while True:
        answer = input(f"{question} (o/n) : ").strip().lower()
        if answer in ("o", "oui"):
            return True
        if answer in ("n", "non"):
            return False