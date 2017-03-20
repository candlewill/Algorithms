# 在一个m行n列二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

def lookup(m, nb):
    nb_row, nb_col = len(m), len(m[0])
    print("nb_row, nb_col=%s, %s" %(nb_row, nb_col))
    # start point
    i, j = 0, nb_col-1
    print("start point: ", i,j)

    while(i<nb_row and j>=0):
        print("i=%s, nb_row=%s" %(i, nb_row))
        if m[i][j]==nb:
            return True
        elif(m[i][j]>nb):
            j-=1
        else:
            i+=1
        print("position: ", i, j)
    return False


m = [[1,2,3,4],[2,3,4,5],[6,7,8,9]]
print(lookup(m,1))