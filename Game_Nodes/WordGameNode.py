"""There is a search game where words are changed one letter at a time
(see http://www.yiannisgabriel.com/2013/09/turning-hate-into-love-wordgame.html and http://blog.wolfram.com/2012/01/11/the-longest-word-ladder-puzzle-ever/).

Naturally, you can consider each word to have neighbouring words which are one letter mutations.
E.g. dove is a one letter mutation of love.
These one letter mutations are the children of the start word in a search graph and
so exactly the same code can be used to find a solution of the LoveHate game.

The children of a word are any valid words which differ from the parent by one letter.
E.g. 'dove' is a child of 'love'. As the first part of a solution,
create a get_children() method in the WordGameNode class which just includes all one letter variations of a word.
For example, if the word was "SUN" then the variations would be "AUN", "BUN", ... "ZUN", "SAN", "SBN", "SCN" ... "SZN", "SUA", "SUB" ... "SUZ".
There should be 25*3 in all. That is for the first position, there would be 25 letters that would result in a one letter mutation,
same for the second position and same for the third.

Naturally, for the actual game, you will want to remove all words which are not in the dictionary. That will be the next exercise.

You are to write a get_children() method for the WordGameNode class which returns all one letter variations of the word.

"""

from Node import Node
from string import ascii_lowercase

class WordGameNode(Node):
   def __init__(self, name, parent = None):
      # Ensure lowercase letters (no digits or special chars)
      for letter in name:
         assert letter in ascii_lowercase
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
      #filter out name, which happens len(name) times.
      return [WordGameNode(child) for child in children]

   def get_path(self):
      # insert code here
      return path


def main():
   w = WordGameNode("sun").get_children()
   print(w)

if __name__ == "__main__":
   main()
