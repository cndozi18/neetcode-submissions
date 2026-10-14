class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> map;
        vector<vector<int>> freq(nums.size() + 1);
        for (const auto& num : nums) {
            map[num]++;
        }
        for (const auto& pair : map) {
            freq[pair.second].push_back(pair.first);
        }
        vector<int> res;
        for (int i = freq.size() - 1; i > 0; i--){
            for (const auto& n : freq[i]) {
                res.push_back(n);
                if (res.size() == k) {
                    return res;
                }
            }
        }
    }
};
