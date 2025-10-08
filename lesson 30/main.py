class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
        def __str__(self):
            return self.word + ' ( ' +self.meaning+ ' ) '
        
flash = []
print("Welcome to my Flashcard Application")

while True:
    word = input("Enter the name you want to add to the falshcard : ")
    meaning = input("Enter the of the entered word : ")

    flash.append(flashcard(word, meaning))
    option = int(input("enter 0 , if you want to add another flashcards otherwise enter 1 to exit : "))

    if option == 1:
        break
print("Your flashcards are : ")
for a in flash:
    print("--->", a) 

# saiyaara = lonely star among the stars