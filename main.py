import pandas
# with open("nato_phonetic_alphabet.csv") as nato_file:
#     nato_file_data = nato_file.readlines()
# nato_dictionary = pandas.DataFrame(nato_file_data)
# print(nato_dictionary)
data = pandas.read_csv("nato_phonetic_alphabet.csv")
#print(data.to_dict())

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input(f"Please enter a word to translate to phonetic code\n").upper()
phonetic_word = [phonetic_dict[letter] for letter in word]
print(phonetic_word)