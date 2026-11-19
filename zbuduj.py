"""Buduje stronę: strona/szablon.html z polami {{pole}} wypełnionymi wartościami z strona/ustawienia.json.

    python3 zbuduj.py [folder]   (domyślnie _site)

Wynik: <folder>/index.html.
"""

import json
import os
import sys

TU = os.path.dirname(os.path.abspath(__file__))


def zbuduj(cel, zrodlo=TU):
    """Zapisuje <cel>/index.html zbudowany z plików strony w folderze `zrodlo`; zwraca jego tekst."""
    with open(os.path.join(zrodlo, "strona", "ustawienia.json"), encoding="utf-8") as fh:
        ustawienia = json.load(fh)
    with open(os.path.join(zrodlo, "strona", "szablon.html"), encoding="utf-8") as fh:
        tekst = fh.read()
    for klucz, wartosc in ustawienia.items():
        tekst = tekst.replace("{{" + klucz + "}}", str(wartosc))
    os.makedirs(cel, exist_ok=True)
    with open(os.path.join(cel, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(tekst)
    return tekst


if __name__ == "__main__":
    zbuduj(sys.argv[1] if len(sys.argv) > 1 else "_site")
