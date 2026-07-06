public class Solution {
    public bool hasDuplicate(int[] nums) {
        Console.WriteLine(nums);
        return nums.Length != new HashSet<int>(nums).Count;
    }
}