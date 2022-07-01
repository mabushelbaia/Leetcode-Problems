//https://www.youtube.com/watch?v=H9bfqozjoqs&ab_channel=NeetCode
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int dp[amount+1];
        std::fill_n(dp, amount+1, amount+1);
        dp[0] = 0;
        for (int i=0; i < amount+1 ; i++) {
            for (int coin : coins) {
                if (i - coin >= 0){
                    dp[i] = min(dp[i], 1 + dp[i - coin]);
                }
            }
        }
        return dp[amount] == amount+1? -1 : dp[amount];
    }
};