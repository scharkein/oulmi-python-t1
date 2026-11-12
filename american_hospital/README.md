# American Hospital - Boîte à outils admin (T1)

Gestion des utilisateurs/administrateurs en CLI (Python 3.13, MySQL, Docker).

## Installation
1. cp .env.example .env  (puis mettre de vrais mots de passe)
2. docker compose up -d --build
3. docker compose exec app python main.py

## Rôles et droits
- super_admin (Paris) : tout, sur tous les sites
- admin : gère les utilisateurs de son site
- user : aucun accès à l'outil

## Règles de sécurité
- Login : 1re lettre du prénom + nom (ex : jdupont)
- Mot de passe : généré aléatoirement, hashé avant stockage, durée de validité 90 jours
- Blocage du compte après 3 échecs

## Structure du projet
```bash
├── american_hospital
│   ├── auth
│   ├── cli
│   │   ├── display
│   │   │   ├── __init__.py
│   │   │   ├── print_message.py
│   │   │   └── print_users_table.py
│   │   ├── menus
│   │   │   ├── __init__.py
│   │   │   ├── login_menu.py
│   │   │   ├── main_menu.py
│   │   │   └── user_menu.py
│   │   └── prompts
│   │       ├── ask_choice.py
│   │       ├── ask_confirm.py
│   │       ├── ask_password.py
│   │       ├── ask_text.py
│   │       └── __init__.py
│   ├── config
│   │   ├── env.py
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── db
│   │   └── init.sql
│   ├── docker-compose.yml
│   ├── Dockerfile
│   ├── main.py
│   ├── README.md
│   ├── requirements.txt
│   ├── security
│   ├── storage
│   └── users
└── test
    ├── cli
    │   └── test_ask_text.py
    └── integration
        └── test_scenario.py
```


## Tests
docker compose exec app python -m unittest discover tests

## Équipe
Lucas : sécurité/auth, Marko : données/logique métier, Mathieu : CLI/intégration