import unittest
from unittest.mock import patch
from american_hospital.cli.prompts import ask_text

class TestAskText(unittest.TestCase):
    @patch("builtins.input", side_effect=["", "Jean"])
    def test_retry_si_vide(self, _):
        self.assertEqual(ask_text("Prénom"), "Jean")

    @patch("builtins.input", side_effect=["abc", "123"])
    def test_validator(self, _):
        self.assertEqual(ask_text("Code", validator=str.isdigit), "123")