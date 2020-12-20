import pandas

# TODO 1. Create a dictionary:
phonetic_data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in phonetic_data.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# User input:

bad_word = True
while bad_word:
    word = input("Enter a word: ").upper()

    try:
        code_list = [phonetic_dict[letter] for letter in word]

    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        bad_word = True

    else:
        bad_word = False
        # codes in string:
        str_code = ", ".join(code_list)
        print(str_code)














# Another solution using DataFrame:
# phonetic_dict= {letter: code for (letter, code) in phonetic_data.items()}
# phonetic_data_frame = pandas.DataFrame(phonetic_dict)
#
# nato_dict = {}
# for (index, row) in phonetic_data_frame.iterrows():
#     nato_dict[row.letter] = row.code
