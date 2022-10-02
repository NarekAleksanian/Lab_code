class Solution {
public:
    bool isPalindrome(string s) {
        std::cout.setf(std::ios::boolalpha);
        std::string e = "";
        for (int i = 0; i < s.length(); ++i) {
            if ((int(tolower(s[i])) > 96 && int(tolower(s[i])) < 123) || (int(s[i]) > 47 && int(s[i]) < 58)) {
                e += tolower(s[i]);
            }
        }
        int i = 0;
        int j = e.length() - 1;
        while (i < e.length() / 2) {
            while (j > -1) {
                if (e[i] != e[j])
                    return false;
                else
                    break;
            }
            --j;
            ++i;
        }
        return true;
    }
};
