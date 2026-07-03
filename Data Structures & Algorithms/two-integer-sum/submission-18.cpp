class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> m; 
        for (int i = 0; i< nums.size(); i++){
            int complement = target - nums[i];
            if (m.contains(target-nums[i])) return {m[complement], i};
            else m[nums[i]] =  i;
        }
        return {};
    }
};
