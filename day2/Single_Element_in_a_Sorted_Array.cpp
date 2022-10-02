class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int count = 0;
        int num;
        for (int i = 0; i < nums.size(); ++i) {
            count = 0;
            if (nums[i] == num)
                continue;
            num = nums[i];
            for (int j = i + 1; j < nums.size(); ++j) {
                if ( nums[i] == nums[j])
                    count++;
                else
                    break;
            }
            if (count == 0)
                return nums[i];
        }
        return -1;
    }
};
