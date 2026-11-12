from users import create_user, list_users, search_user, update_user, delete_user
from security.roles import has_permission
from config.settings import ROLES, SITES
from cli.prompts import ask_text, ask_choice, ask_confirm
from cli.display import (
    print_title, print_success, print_error, print_info, print_users_table,
)

def _scope_site(admin: dict) -> str | None:
    """None = tous les sites (super admin), sinon son site uniquement."""
    return None if admin["role"] == "super_admin" else admin["site"]

def _create(admin: dict) -> None:
    prenom = ask_text("Prénom")
    nom = ask_text("Nom")
    role = ask_choice("Rôle :", ROLES)
    site = admin["site"] if _scope_site(admin) else ask_choice("Site :", SITES)

    if not has_permission(admin, "create", site):
        print_error("Vous n'avez pas le droit de créer cet utilisateur.")
        return
    try:
        user, plain_password = create_user(prenom, nom, role, site)
    except ValueError as e:
        print_error(str(e))
        return

    print_success(f"Utilisateur créé : {user['login']}")
    print_info(f"Mot de passe temporaire (affiché une seule fois) : {plain_password}")

def _list(admin: dict) -> None:
    print_users_table(list_users(site=_scope_site(admin)))

def _search(admin: dict) -> None:
    term = ask_text("Recherche (login, nom ou prénom)")
    results = search_user(term)
    scope = _scope_site(admin)
    if scope:
        results = [u for u in results if u["site"] == scope]
    print_users_table(results)

def _pick_user(admin: dict, action: str) -> dict | None:
    """Affiche les users visibles et demande un id valide."""
    visible = list_users(site=_scope_site(admin))
    print_users_table(visible)
    if not visible:
        return None

    raw = ask_text("ID de l'utilisateur (vide pour annuler)", allow_empty=True)
    if not raw:
        return None
    target = next((u for u in visible if str(u["id"]) == raw), None)
    if target is None:
        print_error("ID introuvable dans votre périmètre.")
        return None
    if not has_permission(admin, action, target["site"]):
        print_error("Droits insuffisants.")
        return None
    return target

def _update(admin: dict) -> None:
    target = _pick_user(admin, "update")
    if not target:
        return

    print_info("Laisser vide pour ne pas modifier.")
    fields = {}
    prenom = ask_text(f"Prénom [{target['prenom']}]", allow_empty=True)
    nom = ask_text(f"Nom [{target['nom']}]", allow_empty=True)
    if prenom:
        fields["prenom"] = prenom
    if nom:
        fields["nom"] = nom
    if ask_confirm(f"Changer le rôle (actuel : {target['role']}) ?"):
        fields["role"] = ask_choice("Nouveau rôle :", ROLES)
    if ask_confirm(f"Changer le site (actuel : {target['site']}) ?"):
        fields["site"] = ask_choice("Nouveau site :", SITES)

    if not fields:
        print_info("Rien à modifier.")
        return
    try:
        update_user(target["id"], fields)
        print_success("Utilisateur modifié.")
    except ValueError as e:
        print_error(str(e))

def _delete(admin: dict) -> None:
    target = _pick_user(admin, "delete")
    if not target:
        return
    if target["login"] == admin["login"]:
        print_error("Vous ne pouvez pas vous supprimer vous-même.")
        return
    if ask_confirm(f"Supprimer définitivement {target['login']} ?"):
        delete_user(target["id"])
        print_success("Utilisateur supprimé.")

ACTIONS = {
    "1": ("Créer un utilisateur", _create),
    "2": ("Lister les utilisateurs", _list),
    "3": ("Rechercher un utilisateur", _search),
    "4": ("Modifier un utilisateur", _update),
    "5": ("Supprimer un utilisateur", _delete),
}

def user_menu(admin: dict) -> None:
    while True:
        print_title("Gestion des utilisateurs")
        for key, (label, _) in ACTIONS.items():
            print(f"{key}. {label}")
        print("0. Retour")

        choice = ask_text("Choix")
        if choice == "0":
            return
        if choice in ACTIONS:
            ACTIONS[choice][1](admin)
        else:
            print_error("Choix invalide.")