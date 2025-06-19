import argparse
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
    parser = argparse.ArgumentParser(description='Autocorrector')
    parser.add_argument('url', help='La URL en la que se desea obtener texto')  

    args = parser.parse_args() 
     
    tags = ["p", "h1", "h2", "h3", "div", "span", "button", "a", "label"]
    response = requests.get(args.url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser') 

    for tag in tags:
        contents = soup.find_all(tag)

        for content in contents:
            if(content.get_text() != ""):
                errors = orthographyCorrector(content.get_text())
    
                for error in errors:
                    print(error)
