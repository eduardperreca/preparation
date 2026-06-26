class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for n in nums:
            seen[n] = seen.get(n, 0) + 1
            
        sorted_items = sorted(seen.items(), key=lambda item: item[1], reverse=True)
        return [item[0] for item in sorted_items[:k]]