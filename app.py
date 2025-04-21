import json

    class Teacher:
    def __init__(self, filename="FlashCards.json"):
        self.filename = filename
        self.flashcards = self.load_flashcards()

