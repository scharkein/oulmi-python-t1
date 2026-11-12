from cli.prompts import ask_text
from cli.display import print_title, print_error
from .user_menu import user_menu

def main_menu(admin: dict) -> str:
    """Retourne 'logout' ou 'quit'."""
    while True:
        print_title(f"Menu principal - {admin['login']} ({admin['role']}, {admin['site']})")
        print("1. Gérer les utilisateurs")
        print("2. Se déconnecter")
        print("0. Quitter")

        choice = ask_text("Choix")
        if choice == "1":
            user_menu(admin)
        elif choice == "2":
            return "logout"
        elif choice == "0":
            return "quit"
        else:
            print_error("Choix invalide.")