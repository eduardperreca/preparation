class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(set(nums))  # rimuove duplicati e ordina
        curr_max = 1
        partial_max = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                partial_max += 1
            else:
                curr_max = max(curr_max, partial_max)
                partial_max = 1  # reset per nuova sequenza

        return max(curr_max, partial_max)