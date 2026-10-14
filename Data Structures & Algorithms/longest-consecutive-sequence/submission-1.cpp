class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> set(nums.begin(), nums.end());
        int longest = 0;
        for (const auto& num : set) {
            if (set.count(num - 1)) {
                continue;
            }
            int length = 0;
            while (set.count(num + length)) {
                length++;
            }
            longest = max(length, longest);
        }
        return longest;
    }
};
