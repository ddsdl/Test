my_graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}


def recursive_dfs(v, discovered=[]):
    discovered.append(v)  # 발견된 노드 기록
    for w in my_graph[v]:  # v 와 연결된 모든 인접 노드 w 에 대해 반복
        if not w in discovered:  # w가 결과에 없는 경우에만 실행
            # 재귀적으로 recursive_dfs 함수를 호출하여
            discovered = recursive_dfs(w, discovered)
            # w를 시작 노드로 설정하고, discovered 리스트를 업데이트합니다.
            # 이렇게 하면 현재 노드 v의 인접 노드 w를 탐색
    return discovered  # 결과 반환


print(recursive_dfs(1))
