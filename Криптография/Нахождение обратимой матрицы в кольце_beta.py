from random import *

import numpy as np

def inv_matrix(A, p):
    Ad = []
    k = len(A)
    
    for i in range(len(A)):
        for j in range(len(A)):
            temp = A.copy()
            temp = np.delete(temp, i, 0)
            temp = np.delete(temp, j, 1)
            M = np.linalg.det(temp)*(-1)**(i+j)
            Ad.append(int(M + (0.5 if M > 0 else -0.5))%p)
            
    Ad = np.matrix(Ad).reshape(k,k)
    Ad = Ad.T
    
    det_A = int(np.linalg.det(A))
    inv_det_A = 0
    for i in range(p):
        if (i*det_A)%p == 1:
            inv_det_A = i
            
    A_inv = (Ad*inv_det_A)%p
    
    return A_inv
k = 5
# a = [randint(0, 26) for _ in range(16)]
# a = [int(c) for c in '15 3 7 13 7 25 16 8 1 21 14 25 7 22 4 1'.split()]
# a = [int(c) for c in '17 1 3 8 2 7 0 2 1'.split()]
# a = [int(c) for c in '10 3 5 2'.split()]

# A = np.matrix(a).reshape(k, k)
p = 33

# det = np.linalg.det(A)
# det_A = int(det + (0.5 if det > 0 else -0.5))%26
# # det_A = (int(D + (0.5 if D > 0 else -0.5)))%p

# inv_det_A = 0
# for i in range(p):
#     if (i*det_A)%p == 1:
#         inv_det_A = i
            
# if inv_det_A != 0:
#     print('A =', *a)



# A_inv = inv_matrix(A, p)

# T = []
# for i in range(k):
#     for j in range(k):
#         T.append(A_inv[i,j])

# print('A_inv =', *T)

while True:
    a = [randint(0, p) for _ in range(k**2)]
    A = np.matrix(a).reshape(k, k)
    det = np.linalg.det(A)
    det_A = int(det + (0.5 if det > 0 else -0.5))%p
    
    inv_det_A = 0
    for i in range(p):
        if (i*det_A)%p == 1:
            inv_det_A = i
    
    A_inv = inv_matrix(A, p)
    
    T = []
    
    for i in range(k):
        for j in range(k):
            T.append(A_inv[i,j])
    
    if inv_det_A != 0:
        print('A =', *a)
        print('A_inv =', *T)
        break


# 20 5 11 5 7 3 3 22 9 23 5 18 6 24 5 9
# inv 20 25 7 12 4 22 18 12 20 5 3 14 14 23 15 8

# A = 9 21 25 3 5 4 1 2 14
# A_inv = 6 20 17 24 19 13 11 7 10
