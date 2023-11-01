# def combinationSum(candidates, target):
#     answer = []
#     output = []

#     def combination(idx, sum):
#         if sum >= target:
#             if sum == target:
#                 answer.append(output[:])
#             return
#         if idx >= len(candidates):
#             return

#         output.append(candidates[idx])
#         combination(idx, sum + candidates[idx])
#         output.pop()
#         combination(idx+1, sum)

#     combination(0, 0)
#     return answer

def combinationSum(candidates, target):
    answer = []

    def backtrack(idx, sums, path):
        if sums == target:
            answer.append(path[:])
            return
        if sums > target or idx >= len(candidates):
            return

        for i in range(idx, len(candidates)):
            path.append(candidates[i])
            backtrack(i, sums + candidates[i], path)
            path.pop()

    backtrack(0, 0, [])
    return answer
