def climbStairs(n):
    h = {1: 1, 2: 2} 
    def dp(n):
        if n not in h:
            h[n] = dp(n - 1) + dp(n - 2)
        return h[n]
    return dp(n)
        