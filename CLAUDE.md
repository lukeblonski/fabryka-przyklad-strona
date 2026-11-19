# Pracownia Przykład — strona

Strona statyczna pracowni. `zbuduj.py` składa `strona/szablon.html` z polami `{{pole}}` i wartości z `strona/ustawienia.json` w `index.html`. Publikuje ją workflow `.github/workflows/publikacja.yml` na GitHub Pages; przy publikacji workflow wstawia ustawienia produkcji.

Godziny, nazwa i inne treści strony zmienia się w `strona/ustawienia.json`. Bez zmian w `.github/workflows/`, w `cofnij.sh` i w `sprawdzenie.py`.

## Verify

`python3 -m unittest discover -s testy -t .`

## Sprawdzenie na żywo

- godziny: `python3 sprawdzenie.py`

## Wdrożenie

- workflow: publikacja.yml
- krok wdrożenia: Publikacja na Pages
- cofnięcie: bash cofnij.sh
- adres: https://lukeblonski.github.io/fabryka-przyklad-strona/
