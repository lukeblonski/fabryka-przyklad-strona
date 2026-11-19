"""Sprawdzenie na żywo „godziny”: strona pokazuje godziny otwarcia pn–pt 9–17.

Uruchamia je autopilot (## Sprawdzenie na żywo w CLAUDE.md) ze zmiennymi NA_ZYWO_MIEJSCE, NA_ZYWO_ADRES i
NA_ZYWO_WYNIK (oraz PORT przed publikacją):

- przed publikacją (NA_ZYWO_MIEJSCE=przed-publikacja): buduje stronę z plików bieżącego folderu (worktree commitu)
  w folderze tymczasowym, podaje ją pod NA_ZYWO_ADRES na porcie PORT i czyta jej tekst;
- po publikacji (NA_ZYWO_MIEJSCE=po-publikacji): czeka, aż <NA_ZYWO_ADRES>wersja.txt poda commit HEAD bieżącego
  folderu (najwyżej CZEKANIE sekund), i czyta tekst strony pod NA_ZYWO_ADRES.

Sprawdzenie tylko czyta stronę, więc niczego nie tworzy i niczego nie sprząta. Wynik zapisuje w pliku NA_ZYWO_WYNIK;
kod 0 tylko wtedy, gdy strona ma tekst TEKST.
"""

import functools
import http.server
import json
import os
import subprocess
import sys
import tempfile
import threading
import time
import urllib.request

NAZWA = "godziny"
TEKST = "Godziny otwarcia: pn–pt 9–17"
STAN = "strona podaje godziny otwarcia pn–pt 9–17"
CZEKANIE = 600


def pobierz(adres):
    """Tekst spod adresu, z parametrem, który omija pamięć podręczną serwera stron."""
    znak = "&" if "?" in adres else "?"
    zapytanie = urllib.request.Request(f"{adres}{znak}t={time.time_ns()}", headers={"Cache-Control": "no-cache"})
    with urllib.request.urlopen(zapytanie, timeout=30) as odpowiedz:
        return odpowiedz.read().decode("utf-8", errors="replace")


def przed_publikacja(adres, port):
    """Tekst strony zbudowanej z bieżącego folderu i podanej na porcie `port`."""
    sys.path.insert(0, os.getcwd())
    import zbuduj

    with tempfile.TemporaryDirectory() as cel:
        zbuduj.zbuduj(cel, os.getcwd())
        obsluga = functools.partial(http.server.SimpleHTTPRequestHandler, directory=cel)
        serwer = http.server.ThreadingHTTPServer(("127.0.0.1", port), obsluga)
        watek = threading.Thread(target=serwer.serve_forever, daemon=True)
        watek.start()
        try:
            return pobierz(adres.rstrip("/") + "/")
        finally:
            serwer.shutdown()
            serwer.server_close()


def po_publikacji(adres):
    """Tekst opublikowanej strony, gdy pod adresem działa już wersja commitu HEAD."""
    commit = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
    baza = adres if adres.endswith("/") else adres + "/"
    koniec, wersja = time.monotonic() + CZEKANIE, ""
    while True:
        try:
            wersja = pobierz(baza + "wersja.txt").strip()
        except OSError as blad:
            wersja = f"błąd odczytu: {blad}"
        if wersja == commit:
            return pobierz(baza)
        if time.monotonic() >= koniec:
            raise RuntimeError(f"pod {baza}wersja.txt po {CZEKANIE} s jest {wersja!r}, a nie commit {commit}")
        time.sleep(15)


def main():
    miejsce = os.environ.get("NA_ZYWO_MIEJSCE", "")
    adres = os.environ.get("NA_ZYWO_ADRES", "")
    plik = os.environ.get("NA_ZYWO_WYNIK", "")
    wynik = {"sciezka": NAZWA, "miejsce": miejsce, "adres": adres, "ustawienia": "docelowe", "atrapy": [],
             "uslugi": [], "stan_koncowy": STAN, "sprzatanie": {"usuniete": [], "wynik": "nic nie tworzy"}}
    try:
        if miejsce == "po-publikacji":
            tekst = po_publikacji(adres)
        elif miejsce == "przed-publikacja":
            tekst = przed_publikacja(adres, int(os.environ["PORT"]))
        else:
            raise RuntimeError(f"miejsce {miejsce!r} nie jest obsługiwane")
    except (OSError, RuntimeError, KeyError, ValueError, subprocess.CalledProcessError) as blad:
        wynik.update(wynik="nie przeszło", powod=str(blad), dowod="")
        kod = 1
    else:
        linia = next((l.strip() for l in tekst.splitlines() if "Godziny otwarcia" in l), "brak linii z godzinami")
        if TEKST in tekst:
            wynik.update(wynik="przeszło", dowod=f"strona pod {adres}: {linia}")
            kod = 0
        else:
            wynik.update(wynik="nie przeszło", powod=f"strona pod {adres} nie ma tekstu {TEKST!r}",
                         dowod=f"strona pod {adres}: {linia}")
            kod = 1
    if plik:
        with open(plik, "w", encoding="utf-8") as fh:
            json.dump(wynik, fh, ensure_ascii=False)
    print(json.dumps(wynik, ensure_ascii=False))
    return kod


if __name__ == "__main__":
    sys.exit(main())
