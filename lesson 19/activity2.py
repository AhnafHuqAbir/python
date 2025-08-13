text = "ava"
if text[0] == text[-1]:
    print("The first and the last characters are same.", text)

words = ['did', 'not', 'xyx', 'nothing', 'noon']
results = []

for word in words:
    if word[0] == word[-1]:
        results.append(word)
print(f'the words that start and end with the same character are: {results}')