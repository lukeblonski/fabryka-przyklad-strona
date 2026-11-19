#!/usr/bin/env bash
# Cofnięcie publikacji strony (pole „cofnięcie” w ## Wdrożenie w CLAUDE.md), bez argumentów: ponawia ostatni udany
# przebieg workflow publikacja.yml na gałęzi master dla commitu innego niż HEAD (poprzedniej wersji strony) i czeka
# na jego koniec. Kod 0 tylko po udanym ponowieniu.
set -euo pipefail

teraz="$(git rev-parse HEAD)"
id="$(gh run list --workflow publikacja.yml --branch master --status success --limit 50 \
  --json databaseId,headSha --jq "[.[] | select(.headSha != \"$teraz\")][0].databaseId // empty")"
if [ -z "$id" ]; then
  echo "cofnięcie: brak udanej publikacji poprzedniej wersji (commit inny niż $teraz)" >&2
  exit 1
fi
echo "cofnięcie: ponawiam udany przebieg publikacji $id poprzedniej wersji"
gh run rerun "$id"
# Ponowiony przebieg zaczyna się po chwili; do tego czasu ma jeszcze stan starego przebiegu.
for _ in $(seq 1 30); do
  [ "$(gh run view "$id" --json status --jq .status)" = completed ] || break
  sleep 5
done
gh run watch "$id" --exit-status
