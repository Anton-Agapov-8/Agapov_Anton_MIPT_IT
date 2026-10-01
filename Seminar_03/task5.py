import numpy as np


def spiral_matrix(n, m):
    left, right, bottom, top = 0, m, n, 0
    res = np.zeros((n, m))
    num = 1
    while left < right and top < bottom:
        res[top, left:right] = np.arange(num, num + right - left)
        top += 1
        num += right - left

        if top < bottom:
            res[top:bottom, right - 1] = np.arange(num, num + bottom - top)
            right -= 1
            num += bottom - top
        else:
            break

        if left < right:
            res[bottom - 1, left:right][::-1] = np.arange(num, num + right - left)
            bottom -= 1
            num += right - left
        else:
            break

        if top < bottom:
            res[top:bottom, left][::-1] = np.arange(num, num + bottom - top)
            left += 1
            num += bottom - top
        else:
            break
    return res


print(spiral_matrix(6, 7))
