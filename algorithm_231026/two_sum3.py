# Two Sum
# URL : https://leetcode.com/problems/two-sum/
# 풀이 시작 : 2023-10-26
# 풀이 완료 : 2023-10-26

def two_sum(nums, target) -> list[int]:
    # 2차 개선된 방식
    d_nums = {}
    for i, n in enumerate(nums):
        d_nums[n] = i

    # {2: 0, 7: 1, 11: 2, 15: 3}

    for i, n in enumerate(nums):
        gap = target - n
        if gap in d_nums and i != d_nums[gap]:
            return [i, d_nums[gap]]


nums = [2, 7, 11, 15]
target = 9
two_sum(nums, target)
