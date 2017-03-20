# 最大子数组和问题
import numpy as np

def max_sublist(a):
    size = len(a)
    dp = [0]*size
    dp[0]=a[0]
    for i in range(1, size):
        # if a[i]<0:
        #     dp[i]=a[i]
        # else:
        #     dp[i]=dp[i-1]+a[i]

        dp[i]=max(dp[i-1]+a[i],a[i])
    print(dp)
    return np.max(dp)

import random
data = [random.randrange(-100, 100) for i in range(20)]
print(data)
print(max_sublist(data))