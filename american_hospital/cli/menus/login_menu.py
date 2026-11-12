from auth import authenticate_admin
from security.password import is_expired
from cli.prompts import ask_text, ask_password
from cli.display import print_title, print_error

def login_menu() -> dict | None:
    """Retourne l'admin connecté, ou None si l'utilisateur quitte."""
    print_title("American Hospital - Connexion administrateur")
    print("(laisser le login vide pour quitter)")

    while True:
        login = ask_text("Login", allow_empty=True)
        if not login:
            return None
        password = ask_password()

        admin = authenticate_admin(login, password)
        if admin is None:
            print_error("Identifiants invalides ou compte bloqué.")
            continue
        if is_expired(admin["password_expires_at"]):
            print_error("Mot de passe expiré, contactez le super admin.")
            continue
        return admin