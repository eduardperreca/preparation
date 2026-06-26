class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for s in strs:
            ord_s = ''.join(sorted(s))
            if ord_s not in seen.keys():
                seen[ord_s] = []
            seen[ord_s].append(s)
        return seen.values()