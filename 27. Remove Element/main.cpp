class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int n = nums.size();
        int index = 0;
        for(int x : nums){
            if(x != val){
                nums[index] = x;
                ++index;
            }
        }
        return index;
    }
        
};