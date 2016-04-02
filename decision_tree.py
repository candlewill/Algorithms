import numpy as np


def entropy(distribution):
    if np.sum(distribution)!=1:
        print('The distribution probability is wrong.')
        return False
    ent = 0
    for p in distribution:
        ent += p*np.log2(p)
    return -ent

if __name__=='__main__':
    distribution = [12/17, 5/17]
    print(entropy(distribution))