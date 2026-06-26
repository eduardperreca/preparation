class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        occ = {}
        for i, el in enumerate(nums):
            compl = target - el
            if compl in occ.keys():
                return [occ[compl], i]
            if el not in occ:
                occ[el] = i
        return []