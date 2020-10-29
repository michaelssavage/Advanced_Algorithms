"""
Given the problem of making change from a sequence of coins, 
the following recursive code finds the smallest required number of coins:

def make_sum(amount, coins):
   assert amount >= 0
   if amount == 0:
      return 0 # base case
   else:
      # Try every possibility
      return min([1 + make_sum(amount - coin, coins) for coin in coins if coin <= amount]) 

This finds the smallest number of coins that can make up a particular amount.

You are to memoize this code. 
That is, ensure that any particular value will only be calculated once by remembering it 
and reusing that value if required again. 
You should use a dictionary to remember the values and then return 
that dictionary containing the values when your function terminates.

You should add another function to the recursive function above, namely:

def testing(amount, coins):
   memo = {}
   number_of_coins =  make_sum(amount, coins, memo)
   return memo

That is, your recursive function will create the memo and that will be returned by your testing function. 
Your memo should have an entry for every value of amount that occurs during the execution of the recursive function.
"""

def find_number(amount, coins, memo={}):
   assert amount >= 0

   if amount in memo:
      return memo[amount]
   elif amount == 0:
      return 0 # base case
   else:
      # Try every possibility
      options = [1 + find_number(amount - coin, coins, memo) for coin in coins if coin <= amount]
      memo[amount] = min(options)
      return memo[amount]

def testing(amount, coins):
   memo = {}
   number_of_coins =  find_number(amount, coins, memo)
   return memo

def main():
    p = testing(12, [5,2,1])
    print(p)


if __name__ == "__main__":
    main()