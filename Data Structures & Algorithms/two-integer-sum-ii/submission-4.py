class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, v in enumerate(numbers):
            complement = target-v
            if complement in numbers:
                return [i+1, numbers.index(complement)+1]

        return [0, 0]