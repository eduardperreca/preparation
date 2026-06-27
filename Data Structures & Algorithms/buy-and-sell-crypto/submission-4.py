class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # questo é troppo semplice, te lo faccio in one line, cit. 15 anni di esperienza
        # return abs(max(prices) - min(prices)) -> LOOOOL
        max_total, curr_total = 0, 0
        l, r = 0, 1

        while r < len(prices):
            curr_total = prices[r] - prices[l]
            if prices[l] < prices[r]:
                max_total = max(max_total, curr_total)
            else:
                l = r
            r += 1
        return max_total