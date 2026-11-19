import os
import tempfile
import unittest

import zbuduj


class ZbudujTest(unittest.TestCase):
    def test_kazde_pole_szablonu_ma_wartosc(self):
        with tempfile.TemporaryDirectory() as cel:
            tekst = zbuduj.zbuduj(cel)
            self.assertNotIn("{{", tekst)
            self.assertIn("Pracownia Przykład", tekst)
            self.assertTrue(os.path.isfile(os.path.join(cel, "index.html")))

    def test_godziny_otwarcia_sa_na_stronie(self):
        with tempfile.TemporaryDirectory() as cel:
            self.assertIn("Godziny otwarcia: ", zbuduj.zbuduj(cel))


if __name__ == "__main__":
    unittest.main()
