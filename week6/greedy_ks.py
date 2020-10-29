"""
In this exercise, you will solve the KnapSack Problem using a greedy algorithm.

The basic strategy is to just find the most valuable item per unit weight, 
place that in the knapsack and repeat the procedure until there is no room in the knapsack. 
Your method should return the total value of the items added.

For example, if the amount was 10 and there were three items:

item1 with value 20 and weight 5, item2 with value 300 and weight 11 and item 3 with value 4 and weight 2. 
Then the greedy algorithm will find the item with the largest value per unit weight that can fit in the knapsack.

item2 has the largest value per unit weight (300 / 11) but it is too heavy to fit in the knapsack and so is not considered. 
The next most valuable item per unit weight is item 1 (20 / 5) and so we keep adding that until we have no more room. 
That is, we add two of item1 for total value of 40. There is no more items that can fit and so the greedy search terminates.

However, the greedy algorithm will not always produce an optimal result. 
E.g. a knapsack with capacity 50 and two items: item1 has a value of 15 and a weight of 26 
whereas item2 has a value of 10 and a weight of 25. 
The best result would be to use two of item2 for a total value of 20, 
but the greedy algorithm sees that the first item is most valuable and so adds that to the knapsack, 
leaving no room for anything else and ends up with a value of 15.
"""
def ks_greedy(initial_capacity, items):
   assert initial_capacity >= 0
   total_value = 0

   items.sort(key=getValue, reverse=True)

   itemsUsed = [0 for n in items]
   i = 0

   for item in items:
      while initial_capacity >= item.weight:
         itemsUsed[i] = item.weight
         total_value += item.value
         initial_capacity -= item.weight
         i+=1

   return total_value, itemsUsed

def getValue(item):
   return item.value/item.weight

def main():
    capacity = 10
    items = [Item(20, 5), Item(300, 11), Item(4, 2)]
    mostVal, itemUsed = ks_greedy(capacity, items)
    print("Weighted items used ---> ", itemUsed)
    print("The total value is -->", mostVal)

class Item:
    def __init__(self, x, y):
        self.value = x
        self.weight = y

if __name__ == "__main__":
    main()