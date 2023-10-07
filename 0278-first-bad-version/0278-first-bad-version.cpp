// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

typedef long long ll; 
class Solution {
public:
    int firstBadVersion(int n) {
        ll l = 0; ll r = n; ll pot = 0;
        while (l <= r) {
            ll m = (l + r) / 2;
            if (isBadVersion(m)) {
                pot = pot ? min(pot, m) : m;
                r = m - 1;
            } else {
                l = m + 1;
            } 
        }
        return pot;
    }
};