"""
You are given a set of coins and you have to create an exact sum with those coins. 
You are to use the greedy algorithm starting with the largest coin which is less 
than the sum and continue adding coins until you reach the sum.

You are then to say how many of each coin that you used.

For example, assuming you are given a sum of 12, and three coins with values 5, 2 and 1, 
then you would use 2 coins with value 5 and 1 with value 2 and none with value 1 as 5+5+2 is 12.

You are to create a function which will read in a total and then a set of coin values 
and return a list of how many coins were used.

Specifically, you are to write a function which will take two parameters, 
a total and a list of coins and return a list indicating how many of each coin will be used. 
For the example above, the function call would be:

make_sum(12, [5,2,1])

The greedy algorithm will find two 5 euro coins and 1 two euro coin which totals 12 and so will return the list

[2,1,0]

Note that you are to use the greedy algorithm. 
It may not lead to the smallest number of coins being used. 
You may assume that the coins will be sorted in descending order of value.
"""

def make_sum(amount, coins):

    i = 0
    coinsUsed = [0 for n in coins]
    while amount != 0:
        if amount >= coins[i]:
            amount -= coins[i]
            coinsUsed[i] += 1
        else:
            i +=1
        
    return coinsUsed

def main():
    p = make_sum(12, [5,2,1])
    print(p)



if __name__ == "__main__":
    main()