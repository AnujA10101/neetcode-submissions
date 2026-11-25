class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::set<int> sets;
        for (int i = 0; i < nums.size(); ++i) {
            if (sets.count(nums[i]) == 1) {
                return true;
            }
            sets.insert(nums[i]);
        }
        return false;

    }
};