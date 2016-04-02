# 最小编辑距离，两个字符串S、T，在任意位置上插入、删除、修改一个字符，得到新的字符串最少需要的编辑次数

import numpy as np

def min_edit_dist(s,t):
    s_len = len(s)
    t_len = len(t)
    dp = np.zeros((s_len, t_len))
    for i in range(s_len):
        dp[i][0]=i
    for j in range(t_len):
        dp[0][j]=j
    for i in range(1, s_len):
        for j in range(1, t_len):
            p1=dp[i-1][j]+1
            p2=dp[i][j-1]+1
            if s[i]==t[j]:
                same = 0
            else:
                same = 1
            p3 = same + dp[i-1][j-1]
            dp[i][j]=min(p1,p2,p3)
    print(dp)
    return dp[s_len-1][t_len-1]


s = 'fewifjawea'
t = 'fewifjeigafew'
print(min_edit_dist(s, t))