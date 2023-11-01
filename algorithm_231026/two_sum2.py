# Two Sum
# URL : https://leetcode.com/problems/two-sum/
# 풀이 시작 : 2023-10-26
# 풀이 완료 : 2023-10-26

def two_sum(nums, target) -> list[int]:
    # 1차 개선된 방식
    for i in range(len(nums)):  # nums의 0번째 2
        gap = target - nums[i]  # gap = 7
        if gap in nums[i+1:]:  # nums 의 1번째부터 끝까지에서 7을 탐색
            return [i, nums[i+1:].index(gap) + (i + 1)]


nums = [2, 7, 11, 15]
target = 9
