#include <iostream>
#include <unordered_map>
#include <vector>

typedef unsigned long long ll;

std::vector<ll> TwoSum(std::vector<ll> array, ll target){
    std::unordered_map<ll, ll> numDict; 
    for(size_t i = 0; i < array.size(); ++i){
        int current = array.at(i);
        if (numDict.find(target - current) != numDict.end()){
            return {i, numDict.at(target - current)};
        }
        numDict[current] = i;
    }
    return {};
}