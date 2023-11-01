def two_sum(nums, target) -> list[int]:
    # 투 포인터 기법을 이용해 개선한 방식

    # lt, rt 는 위치값
    lt = 0
    rt = len(nums) - 1

    while lt < rt:
        sum = nums[lt] + nums[rt]
        if sum < target:
            lt += 1
        elif sum > target:
            rt -= 1
        else:
            return [lt, rt]


# nums = [3, 2, 4]
nums = [2, 7, 11, 15]
target = 9
