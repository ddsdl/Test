class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2
        nums_sum = sum(nums)
        return total - nums_sum


# class Solution:
#     def missingNumber(self, nums: list[int]) -> int:
#         n = len(nums) + 1
#         for i in range(n):
#             if i not in nums:
#                 return i
