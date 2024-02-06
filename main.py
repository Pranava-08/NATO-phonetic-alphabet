import pandas

nato_data = pandas.read_csv('nato_phonetic_alphabet.csv')
ref_words = {word.letter:word.code for idx,word in nato_data.iterrows()}

word = input("Enter the word: ").upper()
print('The NATO phonetic alphabets are:',[ref_words[i] for i in word])

#can be reduced to a line using:
#print([{word.letter:word.code for idx,word in pandas.read_csv('nato_phonetic_alphabet.csv').iterrows()}[i] for i in input("Enter the word: ").upper()])