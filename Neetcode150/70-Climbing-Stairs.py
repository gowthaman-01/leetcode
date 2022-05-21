def climbStairs(n):
    store = {0: 0, 1: 1, 2: 2}
    def helper(n):
        if n not in store:
            temp_sum = helper(n - 1) + helper(n - 2)
            store[n] = temp_sum 
            return temp_sum
        else:
            return store[n] 
    return helper(n)
    