class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> a;
        for (int el: nums) a.insert(el);
        return nums.size() != a.size();
    }
};