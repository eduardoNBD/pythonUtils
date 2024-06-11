from autocorrect import Speller
import requests
from bs4 import BeautifulSoup

def orthographyCorrector(text,lang = "es"):
    textCorre = "Corrección" if lang == "es" else "Correction"
    corrector = Speller(lang)
    text      = text.split(" ")
    errors    = []

    for word in text:
        
        if not corrector(word) == word:
            errors.append("Error: *"+word.strip()+"*  | "+textCorre+" "+(corrector(word.strip())))

    return errors

if __name__ == "__main__":
    url = "https://eduardodev.vercel.app/contact"
    tags = ["p", "h1", "h2", "h3", "div", "span", "button", "a", "label"]
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser') 

    for tag in tags:
        contents = soup.find_all(tag)

        for content in contents:
            if(content.get_text() != ""):
                errors = orthographyCorrector(content.get_text())
    
                for error in errors:
                    print(error)
