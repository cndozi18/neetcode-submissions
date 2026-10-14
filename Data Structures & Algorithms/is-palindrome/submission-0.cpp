class Solution {
public:
    bool isPalindrome(string s) {
        string str;
        for (const auto& c : s) {
            if (isalnum(c)) {
                str += tolower(c);
            }
        }
        int i = 0;
        int j = str.length() - 1;
        while (j > i) {
            if (str[i] != str[j]) {
                return false;
            }
            i++, j--;
        }
        return true;
    }
};
