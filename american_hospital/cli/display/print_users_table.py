from .print_message import print_info

COLUMNS = [
    ("id", "ID"), ("login", "Login"), ("prenom", "Prénom"), ("nom", "Nom"),
    ("role", "Rôle"), ("site", "Site"), ("password_expires_at", "Expire le"),
]

def print_users_table(users: list[dict]) -> None:
    if not users:
        print_info("Aucun résultat.")
        return

    headers = [label for _, label in COLUMNS]
    rows = [[str(u.get(key, "")) for key, _ in COLUMNS] for u in users]
    widths = [max(len(h), *(len(r[i]) for r in rows)) for i, h in enumerate(headers)]

    line = "+" + "+".join("-" * (w + 2) for w in widths) + "+"
    fmt = lambda cells: "| " + " | ".join(c.ljust(w) for c, w in zip(cells, widths)) + " |"

    print(line)
    print(fmt(headers))
    print(line)
    for row in rows:
        print(fmt(row))
    print(line)