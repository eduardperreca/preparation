public class Solution {
    public bool hasDuplicate(int[] nums) {
        Console.WriteLine(nums);
        var a = new HashSet<int>(nums);
        return nums.Length != a.Count;
    }
}