from pathlib import Path
from helper.tools import read_pdf, find_paterns

BASE_DIR = Path(__file__).resolve().parent
PDF_DIR = BASE_DIR / "pdf"

def main():

    found_prefixes = set()

    if not Path(BASE_DIR / "output.txt").exists():
        with open('./output.txt', 'w', encoding='utf-8') as f:
            pass

    with open('./output.txt', 'r', encoding='utf-8') as file:
        for f in file.readlines():
            found_prefixes.add(f.strip())

    if PDF_DIR.is_dir():
        for filepath in PDF_DIR.iterdir():
            if filepath.is_file() and filepath.suffix.lower() == '.pdf':
                text = read_pdf(str(filepath.absolute()))
                patterns = find_paterns(text)
                if not patterns == []:
                    for p in patterns:
                        found_prefixes.add(str(p))

    with open('./output.txt', 'w', encoding='utf-8') as writer:
        for p in found_prefixes:
            writer.write(f'{p}\n')



if __name__ == "__main__":
    main()
