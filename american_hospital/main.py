from cli.menus import login_menu, main_menu
from cli.display import print_info, print_error

def main() -> None:
    try:
        while True:
            admin = login_menu()
            if admin is None:
                break
            if main_menu(admin) == "quit":
                break
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print_error(f"Erreur main.py : {e}")
    print_info("Au revoir.")

if __name__ == "__main__":
    main()