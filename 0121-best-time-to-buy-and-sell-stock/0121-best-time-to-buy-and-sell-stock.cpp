class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy = 0, sell = 1, max_profit = 0;

        while (sell < prices.size()) {
            if (prices[sell] < prices[buy]) {
                buy = sell;
            } else {
                max_profit = std::max(max_profit, prices[sell] - prices[buy]);
            }
            sell++;
        }
        
        return max_profit;
    }
};