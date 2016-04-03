# Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.


def sort_color(a):
    i, j = 0, len(a) - 1
    for k in range(0, j):
        if a[k] == 0:
            a[i], a[k] = a[k], a[i]
            i += 1
        elif a[k] == 2:
            a[k], a[j] = a[j], a[k]
            j -= 1
            k -= 1

    return a


a = [0, 1, 2, 0, 1, 2, 1, 2, 0]
print(sort_color(a))
