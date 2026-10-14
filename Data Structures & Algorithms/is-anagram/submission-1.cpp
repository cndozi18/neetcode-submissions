class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> map_s;
        unordered_map<char, int> map_t;
        for (char c : s) {
            if (map_s.find(c) == map_s.end()) {
                map_s.insert({c, 1});
            } else {
                map_s.at(c)++;
            }
        }
        for (char c : t) {
            if (map_t.find(c) == map_t.end()) {
                map_t.insert({c, 1});
            } else {
                map_t.at(c)++;
            }
        }
        return (map_t == map_s);
    }
};
