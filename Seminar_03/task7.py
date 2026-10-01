import numpy as np

n, m = map(int, input().split())
matrix = np.zeros((n, n))
matrix2 = np.zeros((n, 1))
for i in range(n):
    nums = list(map(np.float32, input().split()))
    nums1 = np.array(nums[:n])
    nums2 = np.array(nums[n:m])
    matrix[i] = nums1
    matrix2[i] = nums2
res = []
for i in range(n):
    matrix1 = matrix.copy()
    for j in range(n):
        matrix1[j][i] = matrix2[j][0]
    x = np.linalg.det(matrix1) / np.linalg.det(matrix)
    res.append(x)
for i in range(len(res)):
    print(f'x{i + 1} = {res[i]:.3f}')
