

# def combine(n, k):
#     result = []

#     def dfs(elements, start, k):
#         if k == 0:
#             result.append(elements[:])

#         for i in range(start, n + 1):
#             elements.append(i)
#             dfs(elements, i + 1, k - 1)
#             elements.pop()

#     dfs([], 1, k)
#     return result


# print(combine(n, k))


def combine(n, k):
    combinations = []
    combi = []

    def dfs(k, start):
        if k == 0:
            combinations.append(combi.copy())
            return
        for i in range(start, n - k + 1):
            combi.append(i + 1)
            dfs(k - 1, i + 1)
            combi.pop()

    dfs(k, 0)
    return combinations


n = 4
k = 2

# solution = Solution()  # Solution 클래스의 인스턴스 생성
# result = solution.combine(n, k)  # combine 메서드 호출

# print(result)
