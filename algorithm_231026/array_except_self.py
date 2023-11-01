# 자신을 제외한 배열의 곱
# URL : https://leetcode.com/problems/product-of-array-except-self/
# 풀이 시작 : 2023-10-26
# 풀이 완료 : 2023-10-26
def product_except_self(nums: list[int]) -> list[int]:
    result = []
    product = 1
    for i in range(len(nums)):
        product *= nums[i]
        result *= product
    for i in range(len(nums)-1, 0, -1):
        product *= nums[i]
        result *= product

    return result


sums = [1, 2, 3, 4]
print(product_except_self(sums))

# def product_except_self(nums):
#     result = []

#     for i in range(len(nums)):
#         product = 1

#         for j in range(len(nums)):
#             if i != j:
#                 product *= nums[j]
#         result.append(product)

#     return result


# nums = list(int, input())
# print(product_except_self(nums))
