class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            check = ''.join(sorted(word))
            if check not in seen.keys():
                seen[check] = [word]
            else:
                seen[check].append(word)
        return [x for x in seen.values()]