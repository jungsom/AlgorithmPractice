class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0              # 이익 변수 생성
        for i in range(1, len(prices)):     
            if prices[i] > prices[i-1]: # 이익이 있다고 판단되면 주식을 판매함
                profit += prices[i]-prices[i-1]
        return profit