class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        std::vector<int> tmp;
        int i = 0, j = 0;
        int er = 0;
        while (i < nums1.size() && j < nums2.size()){
            if (nums1[i] == nums2[j]) {
                tmp.insert(tmp.begin()+er, nums1[i]);
                ++er;
            }
            ++i;
            ++j;
        }
        return tmp;
    }
};
