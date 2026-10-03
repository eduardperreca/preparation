class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, j in enumerate(nums):
            complement = target - j
            if complement in seen.keys():
                return [seen[complement], i]
            else:
                seen[j] = i
        return []