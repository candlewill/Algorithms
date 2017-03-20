import numpy as np
# 有一个n*m的矩阵，需要从坐上角(1,1)走到右下角(n,m)，只能向右和向下走。
# 矩阵中的每个方格有一个非负整数，问从左上角到右下角的所有路径中，数字之和最小的路径是哪一条，以及对应的总路程是多少。


def shortest_dist(m):
    nb_row = len(m)
    nb_col = len(m[0])
    dist= np.zeros((nb_row, nb_col))
    print(dist.shape)
    dist[0][0]=m[0][0]
    for i in range(1, nb_row):
        dist[i][0]=dist[i-1][0]+m[i][0]
    for j in range(1, nb_col):
        dist[0][j]=dist[0][j-1]+m[0][j]
    for i in range(1,nb_row):
        for j in range(1, nb_col):
            dist[i][j]=min(dist[i-1][j], dist[i][j-1])+m[i][j]
    print(dist)
    return dist[nb_row-1][nb_col-1]


m = [[1,2,3,4],[3,2,1,4],[6,5,4,3]]
for i in m:
    print(i)
print(shortest_dist(m))