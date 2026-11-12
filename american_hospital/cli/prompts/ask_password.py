from getpass import getpass

def ask_password(label: str = "Mot de passe") -> str:
    return getpass(f"{label} : ")