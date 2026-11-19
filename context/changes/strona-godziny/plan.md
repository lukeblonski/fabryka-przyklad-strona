# Godziny otwarcia na stronie Implementation Plan

## Overview

Strona pokazuje „Godziny otwarcia: nieustalone”. Zmieniamy wartość pola `godziny` w `strona/ustawienia.json` na `pn–pt 9–17` i dodajemy jeden test, który pilnuje tej wartości, żeby polecenie z kryterium C1 naprawdę mogło się nie powieść.

## Current State Analysis

- `strona/ustawienia.json` ma `{"nazwa": "Pracownia Przykład", "godziny": "nieustalone"}`.
- `strona/szablon.html` ma linię `<p>Godziny otwarcia: {{godziny}}</p>`; `zbuduj.py` podstawia pola z ustawień.
- `testy/test_zbuduj.py:16` sprawdza tylko, że na stronie jest tekst „Godziny otwarcia: ”, bez wartości. Dziś testy przechodzą (2 testy OK) i przeszłyby także bez zmiany godzin, więc samo polecenie z C1 niczego by nie wykryło.
- `sprawdzenie.py` (sprawdzenie na żywo „godziny”) szuka tekstu „Godziny otwarcia: pn–pt 9–17”; działa na opublikowanej stronie i nie jest częścią planu.

## Desired End State

`strona/ustawienia.json` ma `"godziny": "pn–pt 9–17"`, zbudowana strona zawiera „Godziny otwarcia: pn–pt 9–17”, a `python3 -m unittest discover -s testy -t .` przechodzi, w tym test, który oblewa się przy innej wartości.

### Key Discoveries:

- Szablon i `zbuduj.py` już obsługują pole `godziny`; potrzebna jest tylko wartość (`strona/ustawienia.json`).
- Znak w wartości to półpauza „–” (U+2013), taka sama jak w `TEKST` w `sprawdzenie.py`; plik JSON jest czytany jako UTF-8.
- Ograniczenia z `change.md`: godziny zmienia się tylko w polu `godziny`; bez zmian w `strona/szablon.html`, `zbuduj.py`, `.github/workflows/`, `cofnij.sh`, `sprawdzenie.py`.

## Decyzje planu

| Decyzja | Wybór | Uzasadnienie |
|---|---|---|
| Czy dodać test wartości godzin | Tak, jedna asercja w `testy/test_zbuduj.py` | Obecny test nie sprawdza wartości, więc polecenie z C1 przechodziłoby także bez zmiany; test w katalogu `testy/` nie łamie ograniczeń zmiany. |
| Kolejność w fazie | Najpierw test (czerwony), potem wartość w ustawieniach | Pokazuje, że test faktycznie wykrywa starą wartość „nieustalone”. |
| Liczba faz | Jedna | Dwie drobne zmiany w dwóch plikach, bez zależności między fazami. |
| Wiersze Manual | Brak | Decyzja z góry w `change.md`: każde kryterium sukcesu to polecenie. |
| Publikacja | Poza planem | Publikuje ją workflow repo po scaleniu (zwykła droga projektu, zgoda w decyzjach z góry); plan nie dotyka `.github/workflows/`. |

## What We're NOT Doing

- Innych godzin w weekend ani zmian w wyglądzie strony.
- Zmian w `strona/szablon.html`, `zbuduj.py`, `.github/workflows/`, `cofnij.sh`, `sprawdzenie.py`.
- Nowych pól ustawień ani nowych podstron.

## Implementation Approach

Jedna faza: test oczekujący pełnego tekstu „Godziny otwarcia: pn–pt 9–17” w zbudowanej stronie, potem zmiana wartości w `strona/ustawienia.json`, potem pełne testy projektu.

## Phase 1: Godziny pn–pt 9–17 w ustawieniach i w teście

**Criteria**: C1

### Overview

Wartość godzin w ustawieniach strony i test, który ją pilnuje.

### Changes Required:

#### 1. Test wartości godzin

**File**: `testy/test_zbuduj.py`

**Intent**: Dopisać test sprawdzający, że zbudowana strona zawiera dokładnie „Godziny otwarcia: pn–pt 9–17”, żeby polecenie z C1 wykrywało stare „nieustalone”.

**Contract**: Nowa metoda w `ZbudujTest`, budująca stronę do katalogu tymczasowego tak jak istniejące testy i porównująca z tekstem `Godziny otwarcia: pn–pt 9–17` (półpauza U+2013). Istniejące testy zostają bez zmian.

#### 2. Wartość godzin

**File**: `strona/ustawienia.json`

**Intent**: Ustawić pole `godziny` na `pn–pt 9–17`.

**Contract**: Plik zostaje poprawnym JSON-em w UTF-8 z tymi samymi kluczami; zmienia się tylko wartość `godziny`, `nazwa` bez zmian.

### Success Criteria:

#### Automated Verification:

- Testy projektu przechodzą: `python3 -m unittest discover -s testy -t .`
- Pole ma właściwą wartość: `python3 -c "import json; assert json.load(open('strona/ustawienia.json', encoding='utf-8'))['godziny'] == 'pn–pt 9–17'"`
- Zbudowana strona podaje godziny: `d=$(mktemp -d) && python3 zbuduj.py "$d" && grep -F "Godziny otwarcia: pn–pt 9–17" "$d/index.html"`

---

## Testing Strategy

### Unit Tests:

- Nowy test: zbudowana strona zawiera „Godziny otwarcia: pn–pt 9–17”.
- Istniejące testy: żadne pole szablonu nie zostaje puste; na stronie jest linia z godzinami.

### Integration Tests:

- Sprawdzenie na żywo `python3 sprawdzenie.py` należy do przebiegu publikacji autopilota, nie do tego planu.

## Performance Considerations

Brak.

## Migration Notes

Brak danych do migracji. Cofnięcie zmiany to przywrócenie poprzedniej wartości pola; cofnięcie publikacji to `bash cofnij.sh` (poza planem).

## References

- Intencja: `context/changes/strona-godziny/change.md`
- Istniejący test: `testy/test_zbuduj.py:16`

## Plan Changes

> Append-only. One entry per departure from the plan, written in the same commit as the phase. See `references/progress-format.md`.

## Progress

> Convention: `- [ ]` pending, `- [x]` done. Append ` — <commit sha>` when a step lands. Do not rename step titles. See `references/progress-format.md`.

### Phase 1: Godziny pn–pt 9–17 w ustawieniach i w teście

#### Automated

- [x] 1.1 Testy projektu przechodzą: `python3 -m unittest discover -s testy -t .` — daa717f
- [x] 1.2 Pole ma właściwą wartość: `python3 -c "import json; assert json.load(open('strona/ustawienia.json', encoding='utf-8'))['godziny'] == 'pn–pt 9–17'"` — daa717f
- [x] 1.3 Zbudowana strona podaje godziny: `d=$(mktemp -d) && python3 zbuduj.py "$d" && grep -F "Godziny otwarcia: pn–pt 9–17" "$d/index.html"` — daa717f
