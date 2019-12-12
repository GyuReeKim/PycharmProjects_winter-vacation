def dfs(v):
    # 초기화하는 단계
    s = []
    s.append(v)
    # 스택이 비어있지 않는 동안 탐색한다.
    while s:
        print(s)
        v = s.pop(-1)
        # 방문하지 않은 곳이면
        if not visited[v]:
            # 방문 표시
            visited[v] = 1
            print(v, end=' ')
            for w in G[v]:
                # 나중에 갈 곳을 저장
                if not visited[w]:
                    s.append(w)

# 인접리스트
# G index 번호의 노드에 어떤 노드가 연결되어있는지 표시
# ex) 1번 노드에는 2, 3 노드가 연결되어있다.
G = [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [3, 6]]
visited = [0] * 8

dfs(1)