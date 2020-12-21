import pandas

# TODO 1. Create a dictionary:
phonetic_data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in
                 phonetic_data.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# User input:

print("")


def generate_phonetic():
    word = input("Enter a word: ").upper()

    try:
        code_list = [phonetic_dict[letter] for letter in word]

    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        print("")
        generate_phonetic()

    else:
        # codes in string:
        str_code = ", ".join(code_list)
        print(f'''{str_code}
''')

        restart = input("Restart? (y/n)").lower()
        if restart == "y":
            generate_phonetic()
        else:
            print("Good Bye!")


generate_phonetic()
