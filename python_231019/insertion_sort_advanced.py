nums = [int(i) for i in input().split()]


def insertion_sort(nums):
    length = len(nums)
    for x in range(1, length):
        key = nums[x]
        y = x - 1
        while y >= 0 and nums[y] > key:
            nums[y + 1] = nums[y]
            y -= 1
        nums[y + 1] = key
    return nums


print(insertion_sort(nums))
