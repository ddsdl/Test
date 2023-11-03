def num_islands(grid: list[list[str]]) -> int:
    count = 0

    def dfs(i, j):
        pass
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                grid[i][j] = "0":
                dfs(i, j)
                count += 1
    print(count)


num_islands(grid)
