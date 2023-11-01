def trap(self, height: list[int]) -> int:
    water = 0
    lt = 0
    rt = len(height) - 1

    max_lt = height[lt]
    max_rt = height[rt]

    while lt < rt:
        if height[lt] < height[rt]:
            if height[lt] > max_lt:
                max_lt = height[lt]
            else:
                water += max_lt - height[lt]
                lt += 1
        else:
            if height[rt] > max_rt:
                max_rt = height[rt]
            else:
                water += max_rt - height[rt]
            rt -= 1
    return water
