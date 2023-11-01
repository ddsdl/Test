import itertools


class Solution:
    def permute(self, nums: list[int]):
        return list(map(list, itertools.permutations(nums)))
        #    [list(i) for i in itertools.permutations(nums)]
