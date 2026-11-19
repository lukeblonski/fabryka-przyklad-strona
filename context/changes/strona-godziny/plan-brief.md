# Godziny otwarcia na stronie — Plan Brief

> Full plan: `context/changes/strona-godziny/plan.md`

## What & Why

Strona pokazuje „Godziny otwarcia: nieustalone”, więc klient nie wie, kiedy przyjść do pracowni. Ustawiamy godziny na `pn–pt 9–17` w jedynym miejscu, gdzie żyją: w `strona/ustawienia.json`.

## Starting Point

Szablon i `zbuduj.py` już podstawiają pole `godziny`. Istniejący test sprawdza tylko, że linia z godzinami istnieje, nie jej wartość.

## Desired End State

Zbudowana strona zawiera „Godziny otwarcia: pn–pt 9–17”, a testy projektu przechodzą i oblewają się przy starej wartości.

## Key Decisions Made

| Decision | Choice | Why (1 sentence) | Source |
| --- | --- | --- | --- |
| Test wartości godzin | Jedna asercja w `testy/test_zbuduj.py` | Bez niej polecenie z C1 przechodziłoby także bez zmiany. | Plan |
| Kolejność | Najpierw test (czerwony), potem wartość | Dowodzi, że test wykrywa „nieustalone”. | Plan |
| Liczba faz | Jedna | Dwie drobne zmiany bez zależności. | Plan |
| Wiersze Manual | Brak | Decyzja z góry w `change.md`. | Intent |
| Publikacja | Poza planem | Robi ją workflow repo po scaleniu. | Intent |

## Scope

**In scope:** wartość `godziny` w `strona/ustawienia.json`; jeden test wartości.

**Out of scope:** godziny w weekend, wygląd strony, `strona/szablon.html`, `zbuduj.py`, `.github/workflows/`, `cofnij.sh`, `sprawdzenie.py`.

## Architecture / Approach

Zmiana danych w pliku ustawień plus test budujący stronę do katalogu tymczasowego i szukający pełnego tekstu godzin.

## Phases at a Glance

| Phase | What it delivers | Key risk |
| --- | --- | --- |
| 1. Godziny w ustawieniach i teście | Wartość `pn–pt 9–17` i test jej pilnujący | Półpauza „–” (U+2013) musi być identyczna w pliku, teście i `sprawdzenie.py`. |

**Prerequisites:** brak.
**Estimated effort:** jedna krótka sesja, jedna faza.

## Open Risks & Assumptions

- Znak „–” to półpauza U+2013; zwykły myślnik „-” zepsułby sprawdzenie na żywo.

## Success Criteria (Summary)

- `python3 -m unittest discover -s testy -t .` przechodzi.
- Zbudowana strona zawiera „Godziny otwarcia: pn–pt 9–17”.
