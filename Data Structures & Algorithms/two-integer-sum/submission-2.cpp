class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        int i = 0;
        for (int num: nums) {
            int diff = target - num;
            if(map.find(num) == map.end()) {
                map.insert({diff, i});
            } else {
                return {map[num], i};
            }
            i++;
        }
        return {0};
    }
};
