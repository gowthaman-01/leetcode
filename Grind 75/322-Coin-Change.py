class Solution:
    def helper(self, coins, amount, store):
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        if amount in store:
            return store[amount]
        count = None
        for coin in coins:
            possible = self.helper(coins, amount - coin, store)
            if possible != -1:
                possible += 1
                if count == None or possible < count:
                    count = possible
        if count == None:
            store[amount] = -1
            return store[amount]
        store[amount] = count
        return store[amount]

    def coinChange(self, coins, amount):
        store = {}
        return self.helper(coins, amount, store)
