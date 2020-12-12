import pandas

# TODO 1. Create a dictionary:

phonetic_data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in phonetic_data.iterrows()}

# Another solution using DataFrame:
# phonetic_dict= {letter: code for (letter, code) in phonetic_data.items()}
# phonetic_data_frame = pandas.DataFrame(phonetic_dict)
#
# nato_dict = {}
# for (index, row) in phonetic_data_frame.iterrows():
#     nato_dict[row.letter] = row.code

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# User input:
word = input("Enter a word: ").upper()
code_list = [phonetic_dict[letter] for letter in word]
print(code_list)

