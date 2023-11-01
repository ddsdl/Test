from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        pmt = []

        def dfs(elements):
            if len(elements) == 0:
                results.append(pmt[:])

            for e in elements:
                new_nums = elements[:]
                new_nums.remove(e)

                pmt.append(e)
                dfs(new_nums)
                pmt.pop()

        dfs(nums)
        return results
