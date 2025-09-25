def DFS(G, S, D, vis):
    if S == D:
        return True
    vis[S] = True
    for node in G[S]:
        if vis[node] is False:
            if DFS(G, node, D, vis) is True:
                return True
    return False


if __name__ == '__main__':
    N = 8
    g = [[] for _ in range(N+1)]
    g[1].extend([2,3,4,5])
    g[3].extend([8])
    g[2].extend([6,7])
    source = 1
    destination = 4
    vis = [False] * (N+1)
    can_reach = DFS(g, source, destination, vis)
    print(can_reach)
