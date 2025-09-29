class StringReverser:
    def __init__(self, text):
        self.text = text

    def reverse_words(self):
        # Split text into words, reverse the list, then join back
        words = self.text.split()
        reversed_text = " ".join(reversed(words))
        return reversed_text


sentence = "Python is very powerful"
reverser = StringReverser(sentence)

print("Original Sentence:", sentence)
print("Reversed Word by Word:", reverser.reverse_words())
