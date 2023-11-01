# 주식 한 번의 거래로 최대 이익 산출
# URL : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# 풀이 시작 : 2023-10-26
# 풀이 완료 : 2023-10-26

# def max_profit(prices):
#     price = 0
#     for i in range(0, len(prices)-1):
#         for j in range(i+1, len(prices)):
#             price = max(prices[j] - prices[i], price)
#     return price


# prices = [7, 1, 5, 3, 6, 4]
# print(max_profit(prices))

# 개선된 방식

def max_profit(prices):
    max_profit = 0
    min_price = prices[0]

    for i in range(1, len(prices)):
        min_price = min(min_price, prices[i])
        max_profit = (max_profit, prices[i] - min_price)
        print(min_price)


max_profit([70, 30, 50, 10, 60, 40])
