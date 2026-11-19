# Przebieg autopilota: strona-godziny

## Koszty kroków

| Krok | Sesja | Początek | Czas (s) | Model | Wejście | Wyjście | Odczyt cache | Zapis cache | Największy kontekst | Koszt USD | Czas modelu (s) | Czas narzędzi (s) | Testy | Pełne testy | Czas testów (s) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| archiwum | f907b3a8-a41a-417b-a15b-4d153152e192 | 2026-11-19T05:23:30+00:00 | 21 | claude-sonnet-5-5 | 12 | 1919 | 137803 | 17093 | 26852 | 0.1014 | 20 | 0 | 0 | 0 | 0 |

## Zatrzymania po archiwum

- czas: 2026-11-19 05:26 · krok: wynik-wdrozenia · powód: sprawdzenie po publikacji nie przeszło (po publikacji, commit de59ec8): krok 1 (sprawdzenie godziny): polecenie zakończyło się kodem 1; wyjście polecenia w logu .autopilot-local/strona-godziny/20261119-052353-wynik-wdrozenia.log; autopilot cofnął wersję kodu poleceniem bash cofnij.sh; commit 5f031e… · zrobiono: przyjęcie: agent, wynik po publikacji do zapisu przebiegu · skutek: krok przyjęty, łańcuch dalej

## Pliki chronione

Brak.

## Sprawdzenie na żywo

- krok 1 (godziny): przeszło (commit 7ada10f)

## Obietnice

- krok 1 (godziny): nie przeszło na Twojej opublikowanej aplikacji (commit de59ec8): polecenie zakończyło się kodem 1; wcześniej przeszło na wersji próbnej przed publikacją (commit 7ada10f)
Werdykt: nie przeszło (krok 1)

## Testy przed scaleniem

- CI gałęzi: brak, testy uruchomił autopilot (commit de59ec8): `python3 -m unittest discover -s testy -t .`

## Pytania do właściciela

- zbędne pytania: 0
- niepełne pytania: 0
