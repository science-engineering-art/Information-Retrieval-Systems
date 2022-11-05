import re
from unidecode import unidecode


class Document:
    
    def __init__(self, path: str):
        # set title
        a = re.findall(r"[\w]+", path)
        self.title = a[len(a)-2]
         
        # load text
        with open(path, "r") as source:
            self.text = [ unidecode(word.lower()) for word in 
                re.findall(r"[\w']+",source.read()) ]
    
    def __str__(self):
        return f'{self.title}\n\n' + ' '.join(self.text)