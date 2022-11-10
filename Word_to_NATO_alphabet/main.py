import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
student_data_frame = pandas.DataFrame(data)

nato_phonetic_alphabet = {row.letter: row.code for (num, row) in data.iterrows()}

word = input("Enter a word: ")
w = word.upper()
print(w)
word_as_list = []
for letter in w:
    if letter in nato_phonetic_alphabet:
        word_as_list.append(nato_phonetic_alphabet[letter])
print(" ".join(word_as_list))
