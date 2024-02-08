class Solution {
public:
    int numSquares(int n) {
        vector<int> squares = getSquares(n);
        vector<int> dp(n + 1, -1);
        dp[n] = 0;
        for (int i = n; i >= 0; i--) {
            if (dp[i] == -1) {
                continue;
            }
            for (int s: squares) {
                if (i - s < 0) {
                    continue;
                }
                if (dp[i - s] == -1) {
                    dp[i - s] = dp[i] + 1;
                } else { 
                    dp[i - s] = min(dp[i - s], dp[i] + 1);
                }
            }
        }
        return dp[0];
    }
    
    // Returns list of perfect squares that are lesser than n.
    vector<int> getSquares(int n) {
        int a = 1;
        vector<int> squares; 
        while (a * a <= n) {
            squares.push_back(a * a);
            a++;
        } 
        return squares;
    }
};

    