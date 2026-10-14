class Solution {
public:

    string encode(vector<string>& strs) {
        string res;
        for (const auto& s : strs) {
            string len = to_string(s.length());
            res += len + "#" + s;
        }
        return res;
    }

    vector<string> decode(string s) {
        vector<string> res;
        string len;
        int count = 0;
        string word;
        for (const auto& c : s) {
            if (c == '#' && count == 0) {
                count = stoi(len);
                len = "";
                if (count == 0) {
                    res.push_back("");
                }
                continue;
            }
            if (count != 0) {
                word += c;
                count--;
                if (count == 0 && word != "") {
                res.push_back(word);
                word = "";
            }
                continue;
            }
            
            len += c;
        }
        return res;
    }
};
