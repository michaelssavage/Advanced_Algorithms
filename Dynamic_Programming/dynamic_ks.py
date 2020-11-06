"""
In this exercise, you will solve the KnapSack Problem using bottom up dynamic programming. 
Use a list to store the smaller results.

Use a for loop to build up the memo where you store the results of the smaller problems

However, your program must return the memo that your program creates rather than the correct result.

Note that the length of the list will be the capacity + 1.

Example:

print(dp_knapsack(10, [Item(20, 5), Item(300, 11), Item(4, 2)]))

will print

[0, 0, 4, 4, 8, 20, 20, 24, 24, 28, 40]

Remember that the list contains the solutions for all capacities from 0 to 10 inclusive. 
For example, the solution when the capacity is 9 will be 24, that is one item of value 20 and another of value 4.
"""

import math

def dp_knapsack(initial_capacity, items):
   assert initial_capacity >= 0
   memo = [-math.inf] * (initial_capacity+1)    
   memo[0] = 0

   for i in range(1,len(memo)):
      for item in items:
         memo[i] = ks_greedy(i,items)
   
   return memo

def ks_greedy(initial_capacity, items):
   assert initial_capacity >= 0
   total_value = 0

   items.sort(key=getValue, reverse=True)

   for item in items:
      while initial_capacity >= item.weight:
         total_value += item.value
         initial_capacity -= item.weight

   return total_value


def getValue(item):
   return item.value/item.weight

def main():
    print(dp_knapsack(10, [Item(20, 5), Item(300, 11), Item(4, 2)]))

class Item:
    def __init__(self, x, y):
        self.value = x
        self.weight = y

if __name__ == "__main__":
    main()
