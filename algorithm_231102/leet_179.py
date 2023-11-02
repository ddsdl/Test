class Solution:
    def largestNumber(self, nums):
        n = len(nums)
        nums = [str(i) for i in nums]

        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] < nums[j] + nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]

        if nums[0] == '0':
            return '0'
        return ''.join(nums)


solution = Solution()

nums = [3, 30, 34, 5, 9]

result = solution.largestNumber(nums)

print(result)
