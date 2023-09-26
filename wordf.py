import random

class WordFinder:
  

    def __init__(self, filepath: str):
       
        with open(filepath, 'r') as file:
            self.words = self._parse_words(file)
        
        print(f"{len(self.words)} words read")

    def _parse_words(self, file) -> list:
       
        return [word.strip() for word in file if word.strip() and not word.startswith("#")]

    def random(self) -> str:
       
        return random.choice(self.words)
