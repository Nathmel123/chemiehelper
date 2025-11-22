from PyPDF2 import PdfReader
from re import findall

PATTERN = '(GHS\d{2}|[HP]\d{3}(?:\+\d{3})*)'

def read_pdf(path):

    output = ""

    try:
        with open(path, 'rb') as file:

            reader = PdfReader(file)

            for page in reader.pages:

                text = page.extract_text()

                if text:
                    output += f'{text}\n'
            
        return output

    except Exception as e:

        print(f'Fehler: {e}')
        exit(-1)
        
    return None

def find_paterns(text):
    output = findall(PATTERN, text)
    if output:
        return output
    return []