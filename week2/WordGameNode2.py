"""
Now we just have to finish the get_children method and we have just about solved the word game.
The first time a WordGameNode2 is created, it should initialise a list of valid words.
Then, when the get_children method is called, it should remove any invalid words from the list of mutated words.

These valid words which are just a one letter move away from the original word are called neighbours or children of the original word.

There are two small changes you need to make.
Well, actually only one, as I have made the first one.
You can see that the init method checks if the valid_words have been initialised and if not,
it initialises them by reading the dictionary. This means that the dictionary file is only read once.

So, you have to modify get_children so that only words which are in the dictionary are returned.
Also insert the code for get_path(self) from the previous exercise.

"""
from Node import Node
from string import ascii_lowercase
from readDictionary import read_dictionary

valid_words = None

class WordGameNode2(Node):
   def __init__(self, name, parent = None):
      # Ensure lowercase letters (no digits or special chars)
      for letter in name:
         assert letter in ascii_lowercase

      global valid_words
      if valid_words == None or len(valid_words) != len(name):
         # We only need to examine words which have the same length as our word (self.name)
         valid_words = read_dictionary(r"C:\Users\micha\code\advanced_alg\words.txt", len(name))
      self.name = name
      self.parent = parent

   def __str__(self):
      return self.name

   def get_children(self):
      #all one letter mutations of the word
      child_words = []
      name = self.name
      for i in range(len(name)):
         for letter in ascii_lowercase:
            child_words.append(name[:i] + letter + name[i+1:])
            #append all variations to child words
      children = [n for n in child_words if n != name]
      return [WordGameNode2(child) for child in children if child in valid_words]

   def get_path(self):
      # insert code here
      return path

def main():
   w = WordGameNode2("sun").get_children()
   print(w)

if __name__ == "__main__":
   main()
