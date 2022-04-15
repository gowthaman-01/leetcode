#include <iostream>
#include <string>
#include <ctype.h>

typedef long long ll;

bool ValidPalindrome(std::string s){
    ll r = s.length() - 1; ll l = 0;
    while(r >= l) {
        if(!isalnum(s.at(r))){
            r -= 1; 
            continue;
        }
        else if (!isalnum(s.at(l))){
            l += 1; 
            continue;
        }
        if (isdigit(s.at(r))){
            if (s.at(r) != s.at(l)){
                return false;
            }
        }
        if (tolower(s.at(r)) != tolower(s.at(l))){
            return false;
        }
        l++; r--;
    }
    return true;
}

int main(){
    std::cout << ValidPalindrome("race a car");
    return 0;
}