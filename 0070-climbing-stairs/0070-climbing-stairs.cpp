class Solution {
public:
    int climbStairs(int n) {
        if (n < 3) {
            return n;
        }
        
        int one = 1;
        int two = 2;
        int cur = 0;

        for (int i = 2; i < n; i++) {
            cur = one + two; 
            one = two;
            two = cur;
        }

        return cur;
    }
};