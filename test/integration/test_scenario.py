import unittest
from american_hospital.users import create_user, search_user, delete_user
from american_hospital.storage.queries import select_by_login
from american_hospital.security.password import verify_password

class TestScenarioComplet(unittest.TestCase):
    def test_creation_recherche_suppression(self):
        user, plain = create_user("Jean", "Dupont", "admin", "Paris")
        self.addCleanup(delete_user, user["id"])

        self.assertTrue(user["login"].startswith("jdupont"))

        stored = select_by_login(user["login"])
        self.assertNotEqual(stored["password_hash"], plain)
        self.assertTrue(verify_password(plain, stored["password_hash"]))

        self.assertIn(user["login"], [u["login"] for u in search_user("dupont")])

        delete_user(user["id"])
        self.assertIsNone(select_by_login(user["login"]))