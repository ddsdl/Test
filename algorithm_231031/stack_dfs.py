my_graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}


def stack_dfs(start_v):
    discovered = []  # 결과 리스트 생성
    stack = [start_v]  # 스택 생성
    while stack:    # 스택이 비어질 때 까지 반복
        v = stack.pop()  # 스택에서 노드 추출
        if v not in discovered:  # 노드가 결과에 없는경우에만 수행
            discovered.append(v)    # 발견된 노드로 표시
            for w in my_graph[v]:   # 노드에 연결된 인접 노드를 확인
                stack.append(w)  # 인접노드 w 를 스택에 추가
    return discovered


print(stack_dfs(1))
