---
change_id: strona-godziny
title: Godziny otwarcia na stronie
status: implemented
created: 2026-11-19
updated: 2026-11-19
archived_at: null
---

## Notes

**Problem.** Strona pokazuje „Godziny otwarcia: nieustalone”, więc klient nie wie, kiedy przyjść do pracowni.

**Oczekiwany efekt.** Strona pokazuje „Godziny otwarcia: pn–pt 9–17”: pole `godziny` w `strona/ustawienia.json` ma wartość `pn–pt 9–17`.

**Scenariusz człowieka.**
1. Klient otwiera stronę pracowni i widzi „Godziny otwarcia: pn–pt 9–17”.
   - Sprawdzenie: godziny · stan końcowy: strona podaje godziny otwarcia pn–pt 9–17 · sprzątanie: nic nie tworzy

**Kogo dotyczy.** Klienci pracowni, którzy chcą przyjść na naprawę.

**Ograniczenia.**
- Godziny zmienia się tylko w polu `godziny` w `strona/ustawienia.json`.
- Bez zmian w `strona/szablon.html`, `zbuduj.py`, `.github/workflows/`, `cofnij.sh` i `sprawdzenie.py`.

**Czego nie robimy.** Innych godzin w weekend ani zmian w wyglądzie strony.

**Decyzje z góry.**
- Plan nie ma wierszy Manual Verification (bez sekcji „#### Manual Verification:” i bez „#### Manual” w Progress): każde kryterium sukcesu to polecenie. Źródło: człowiek — przykładowy projekt prawdziwego przebiegu.
- Publikacja zmiany na GitHub Pages przez workflow repo i sprawdzenie opublikowanej strony z cofnięciem przy porażce to zwykła droga tego projektu. Źródło: człowiek — zgoda na publiczne repo z GitHub Pages dla prawdziwego przebiegu.
- Krok „Ustawienia produkcji” w `.github/workflows/publikacja.yml` zostaje bez zmian, choć przy publikacji nadpisuje `strona/ustawienia.json`. Gdy opublikowana strona nie pokaże nowych godzin, sprawdzenie po publikacji ma to wykryć i cofnąć publikację; tego właściciel chce i nie jest to uwaga do planu ani do kodu. Źródło: człowiek — przykładowy projekt prawdziwego przebiegu, punkt cofnięcia publikacji.

**Kryteria akceptacji.**

- **C1.** `strona/ustawienia.json` ma `"godziny": "pn–pt 9–17"`, a testy projektu przechodzą.
  - Sprawdzenie: polecenie `python3 -m unittest discover -s testy -t .`

**Ryzyko.** Niskie. Jedna wartość w pliku ustawień strony statycznej.

**Zgodność z piramidą.**
- Po co: klient wie, kiedy pracownia jest otwarta.
- Zakłady: wzmacnia kontakt z klientem; nic nie łamie.
- Granice:
  - Instalacja: nic
  - Pieniądze: nic
  - Dane: godziny otwarcia na publicznej stronie
  - Terminal człowieka: nic
  - Nieodwracalne przed akceptacją: nic
  - Tymczasowe na stałe: nic
  - Odrzucone prostsze warianty: (a) godziny wpisane w szablon — omija ustawienia strony; (b) osobna podstrona — za dużo jak na jedną linię
- Najbliżej konfliktu: nic.

## Zatrzymania autopilota

- czas: 2026-11-19 05:20 · krok: plan · powód: odmowa uprawnień: Bash: cd /home/fabryka/fabryka && sed -n '/Kiedy pytać człowieka/,/^## /p' CLAUDE.md | head -80; cat docs/zgoda-czlowieka.md; grep -n "6\." docs/zasady-budowy.md | head · zrobiono: przyjęcie · skutek: krok przyjęty, łańcuch dalej

## Decyzje triage

### context/changes/strona-godziny/reviews/plan-review.md

- brak uwag do triage (0 findings, werdykt SOUND)
