class Solution {
public:
    int tribonacci(int n) {
        int a = 0; int b = 1; int c = 1;
        if (n == 0) return a; 
        if (n < 3) return b; 
        for (int i = 2; i < n; i++) {
            int nc = a + b + c; 
            a = b; 
            b = c; 
            c = nc;      
        }
        return c;
    }
};