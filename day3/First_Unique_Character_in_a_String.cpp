class Solution {
public:
    int firstUniqChar(string s) {
        char tmp[s.length()];
        for (int i = 0; i < s.length(); ++i)
            tmp[i] = '_';
        int i = 0;
        int j;
        int flag;
        int count = 0;
        int some = 0;
        while (i < s.length()) {
            flag = 0;
            for (int k = 0; k < s.length() && tmp[k] != '_'; ++k) {
                if (s[i] == tmp[k]) {
                    flag = 1;
                    ++i;
                    break;
                }
            }
            if (flag == 1)
                continue;
            j = i + 1;
            while (j < s.length()) {
                if (s[i] == s[j]) {
                    tmp[some] = s[i];
                    ++count;
                    ++some;
                    break;
                }
                ++j;
            }
            if (count == 0)
                return i;
            else
                count = 0;
        }
        return -1;
    }
};
