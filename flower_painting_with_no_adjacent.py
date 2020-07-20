def gardenNoAdj(N, paths):
    res = [0] * N
    G = [[] for i in range(N)]
    for x, y in paths:
        G[x - 1].append(y - 1)
        G[y - 1].append(x - 1)
    for i in range(N):
        res[i] = ({1, 2, 3, 4} - {res[j] for j in G[i]}).pop()
    return res


print(gardenNoAdj(N=4, paths=[[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]]))
print(gardenNoAdj(N=4, paths=[[1, 2], [3, 4]]))
