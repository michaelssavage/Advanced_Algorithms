"""
Produce the dynamic programming version of the coins problem, i.e., bottom-up-ify it.

This version builds up the memo array iteratively. 
It does not use recursion. You must write a dynamic programming solution to the coins problem.

However, rather than returning the smallest number of coins, 
you must return the memo that your program creates. 
Your memo should be a Python list and the length of the memo list will be one larger 
than the amount of money that you must produce, as the array indices will go from 0 to amount inclusive.

If a particular amount cannot be made, then that entry should be math.inf.
"""
import math

def dp_make_change(amount, coins):
   assert amount >= 0
   # Initialise memo to be infinity for each of amount + 1 values
   memo = [math.inf] * (amount+1)
   coins.reverse()
   memo[0] = 0

   for amount in range(1, len(memo)):
      for coin in coins:
         memo[amount] = min([memo[amount], memo[amount-coin] + 1])

   return memo

def main():
    d = dp_make_change(12, [5,2,1])
    print(d)

if __name__ == "__main__":
    main()
