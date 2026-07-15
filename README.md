# Chemiehelper (nur für mac-os und Linux)

Dieses Python-Skript dient der automatisierten Extraktion von Gefahrstoff-Kennzeichnungen (GHS-Piktogramme, H- und P-Sätze) aus textbasierten PDF-Dokumenten, wie beispielsweise Sicherheitsdatenblättern oder technischen Spezifikationen.

## Installation

UV installieren
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```
Wichtig: [git muss installiert sein](https://git-scm.com/book/de/v2/Erste-Schritte-Git-installieren). Alle Befehle müssen in einem
Terminalfenster ausgeführt werden und nacheinander mit enter bestätigt werden.
Alle pdf Dateien müssen in den pdf ordner gelegt werden.

```
git clone https://github.com/Nathme123/chemiehelper.git
cd chemiehelper/
uv sync
```

# Programm ausführen
```
uv run main.py
```

Die Einträge werden sortiert und in die Datei output.txt geschrieben.
