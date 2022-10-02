class Solution {
public:
    int myAtoi(string s) {
        int flag = 0;
        int i = 0;
        while (i < s.length()) {
            if (int(s[i]) == 43 || int(s[i]) == 45) {
                ++i;
                continue;
            }
            if (int(s[i]) > 48 && int(s[i]) < 58){
                flag = 1;
            }
            if (int(s[i]) > 47 && int(s[i]) < 58) {
                if (flag == 1) {
                    ++i;
                    continue;
                }
                else {
                    s.erase(s.begin() + i);
                    continue;
                }
            } else {
                s.erase(s.begin() + i);
                continue;
            }
        }
    if (flag == 0)
        return 0;
    return int(std::stoi(s));
    }
};
