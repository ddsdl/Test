# nums = [1, 2, 3]


# def subsets(nums):
#     result = []

#     def dfs(idx, sub):
#         result.append(sub)

#         for i in range(idx, len(nums)):
#             dfs(i + 1, sub + [nums[i]])

#     dfs(0, [])
#     return result


# print(subsets(nums))

nums = [1, 2, 3]


def subsets(nums):
    result = []

    def dfs(idx, sub):
        result.append(sub.copy())
        for i in range(idx, len(nums)):
            new = sub + [nums[i]]
            dfs(i + 1, new)
    dfs(0, [])
    return result


print(subsets(nums))
