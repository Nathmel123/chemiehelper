# Chemiehelper (nur für mac-os und Linux)

Dieses Python-Skript dient der automatisierten Extraktion von Gefahrstoff-Kennzeichnungen (GHS-Piktogramme, H- und P-Sätze) aus textbasierten PDF-Dokumenten, wie beispielsweise Sicherheitsdatenblättern oder technischen Spezifikationen.

## Installation

UV installieren
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```
Wichtig: [git muss installiert sein](https://git-scm.com/book/de/v2/Erste-Schritte-Git-installieren).

```
git clone http://46.224.43.169/nquadrat/chemiehelper.git
cd chemiehelper/
mkdir pdf/
uv sync
```

# Programm ausführen
```
uv run main.py
```