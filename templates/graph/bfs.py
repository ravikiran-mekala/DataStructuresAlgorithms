from collections import deque


def BFS(G, S, D):
    N = len(G)
    vis = [False] * N
    q = deque()
    q.append(S)
    vis[S] = True

    while q:
        node = q.popleft()
        if node == D:
            return True
        for i in G[node]:
            if not vis[i]:
                vis[i] = True
                q.append(i)
    return False


if __name__ == '__main__':
    N = 8
    g = [[] for _ in range(N+1)]
    g[1].extend([2,3,4,5])
    g[3].extend([8])
    g[2].extend([6,7])
    source = 6
    destination = 4
    can_reach = BFS(g, source, destination)
    print(can_reach)
