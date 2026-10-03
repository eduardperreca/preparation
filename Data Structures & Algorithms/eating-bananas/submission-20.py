class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left <= right:
            mid = (left + right) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p/mid)
            print(hours)
            if hours <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return left