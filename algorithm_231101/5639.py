import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이를 늘려줘서 런타임 에러를 방지
tree = []

while True:
    try:
        tree.append(int(sys.stdin.readline()))
    except:
        break


def postorder(s_idx, e_idx):
    if s_idx > e_idx:
        return
    d_idx = e_idx + 1
    for i in range(s_idx+1, e_idx+1):
        if tree[s_idx] < tree[i]:
            d_idx = i
            break

    postorder(s_idx+1, d_idx-1)
    postorder(d_idx, e_idx)
    print(tree[s_idx])


postorder(0, len(tree)-1)
