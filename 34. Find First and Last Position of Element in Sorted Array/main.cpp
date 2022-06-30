class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> ans = {-1,-1};
        int n = nums.size();
        int left = 0, right = n-1;
        while(left<=right){
            int mid = left +(right - left)/2;
            int x = nums[mid];
            if(x < target){
                left = mid + 1;
            }else if(x > target){
                right = mid - 1;
            }else{
                ans[0] = mid;
                right = mid - 1;
            }
        }
        left = 0, right = n-1;
        while(left<=right){
            int mid = left +(right - left)/2;
            int x = nums[mid];
            if(x < target){
                left = mid + 1;
            }else if(x > target){
                right = mid - 1;
            }else{
                ans[1] = mid;
                left = mid + 1;
            }

        }
        return ans;
    }
};