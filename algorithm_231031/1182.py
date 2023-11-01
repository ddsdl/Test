def recursive_dfs(v, sum):
    global cnt
    if v >= N:
        return
    if sum + my_graph[v] == S:
        cnt += 1
    recursive_dfs(v+1, sum)
    recursive_dfs(v+1, sum + my_graph[v])


N, S = map(int, input().split())
my_graph = list(map(int, input().split()))
cnt = 0
recursive_dfs(0, 0)
print(cnt)
