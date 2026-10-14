class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> res(nums.size());
        int pre = 1;
        int post = 1;
        for (int i = 0; i < nums.size(); i++) {
            if (i == 0) {
                res[i] = pre;
                continue;
            }
            pre *= nums[i - 1];
            res[i] = pre;
        }
        for (int i = nums.size() - 1; i >= 0; i--) {
            if (i == nums.size() - 1) {
                res[i] *= post;
                continue;
            }
            post *= nums[i + 1];
            res[i] *= post;
        }
        return res;
    }
};
