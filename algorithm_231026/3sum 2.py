# 3Sum
# URL : https://leetcode.com/problems/3sum
# 풀이 시작 : 2023-10-26
# 풀이 완료 : 2023-10-26
def three_sum(nums: list[int]) -> list[list[int]]:
    result = []
    nums.sort()  # [-4, -1, -1, 0, 1, 2]

    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        for j in range(i+1, len(nums)-1):
            if j > i + 1 and nums[j] == nums[j-1]:
                continue

            for k in range(j+1, len(nums)):
                if k > j + 1 and nums[k] == nums[k-1]:
                    continue

                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])
    return result


print('=================')
nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))
