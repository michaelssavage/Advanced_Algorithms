"""
It's all well and good to create a list of mutated words, but we only want real words,
i.e. words that appear in a dictionary. Many operating systems have a file which contains a list of words.
On Ubuntu Linux, that file is "/etc/dictionaries-common/words". Each word is on a line of its own.
Create a function which takes a file name and reads the lines and creates a list of words.
You should remove any words which do not contain only lowercase letters.
Also, you should only return words of the correct length - you don't need any other words.

Your function should be called read_dictionary.
It will take two parameters, the name of the dictionary file and the length of the word and return a list of all relevant words in the dictionary.

"""
def read_dictionary(filename, length):
    words = []
    for line in open(filename):
        word = line.strip()
        if is_valid(word) and length == len(word):
            words.append(word)

    return words

def is_valid(word):
    return word.islower() and word.isalpha()

def main():
   r = read_dictionary(r"C:\Users\micha\code\advanced_alg\words.txt", 3)
   print(r)

if __name__ == "__main__":
   main()
