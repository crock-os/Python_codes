lang_en = [chr(i) for i in range(97, 123)]
lang_ru = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

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
            Ad.append(int(M + (0.5 if M > 0 else -0.5)))
            
    Ad = np.matrix(Ad).reshape(k,k)
    Ad = Ad.T
    
    det_A = int(np.linalg.det(A))
    inv_det_A = 0
    for i in range(p):
        if (i*det_A)%p == 1:
            inv_det_A = i
            
    A_inv = (Ad*inv_det_A)%p
    
    return A_inv
            

def encoding_en(X, A, B, k):
    x = [lang_en.index(c) for c in X]
    print('x = ', *x)
    R = []
    
    while len(x) > 0:
        q = np.matrix(x[:k]).reshape(k,1)      
        r = (A*q + B)%26
                
        for i in range(k):
            R.append(r[i,0])
            
        print('r = ', end='')
        print(*r, sep='')
        x = x[k:]
    res = [lang_en[i] for i in R]
    return res

def encoding_ru(X, A, B, k):
    x = [lang_ru.index(c) for c in X]
    print('x = ', *x)
    R = []
    
    while len(x) > 0:
        q = np.matrix(x[:k]).reshape(k,1)      
        r = (A*q + B)%33
                
        for i in range(k):
            R.append(r[i,0])
            
        print('r = ', end='')
        print(*r, sep='')
        x = x[k:]
    res = [lang_ru[i] for i in R]
    return res

def decoding_en(Y, A, B, k):
    y = [lang_en.index(c) for c in Y]
    print('y = ', *y)
    R = []
    
    A_inv = inv_matrix(A, 26)
    print('A_inv:')
    print(*A_inv, sep='\n')
    
    while len(y) > 0:
        q = np.matrix(y[:k]).reshape(k,1)      
        r = A_inv*(q - B)%26
                
        for i in range(k):
            R.append(r[i,0])
            
        print('r = ', end='')
        print(*r, sep='')
        y = y[k:]
    res = [lang_en[i] for i in R]
    return res

def decoding_ru(Y, A, B, k):
    y = [lang_ru.index(c) for c in Y]
    print('y = ', *y)
    R = []
    
    A_inv = inv_matrix(A, 33)
    
    while len(y) > 0:
        q = np.matrix(y[:k]).reshape(k,1)      
        r = A_inv*(q - B)%33
                
        for i in range(k):
            R.append(r[i,0])
            
        print('r = ', end='')
        print(*r, sep='')
        y = y[k:]
    res = [lang_ru[i] for i in R]
    return res

type_w = input('Шифрование/Расшифровка(Ш/Р): ').lower()

lang = input('Язык(ру/en): ').lower()
k = int(input('Порядок матрицы: '))
a = [int(c) for c in input('Ключ A: ').lower().split()]
b = [int(c) for c in input('Ключ B: ').lower().split()]

N = input('Слово: ').lower()

A = np.matrix(a).reshape(k, k)
B = np.matrix(b).reshape(k,1)

if type_w == 'ш' or type_w == 'i':
    if lang == 'ру':
        res = encoding_ru(N, A, B, k)
    else:
        res = encoding_en(N, A, B, k)
else:
    if lang == 'ру':
        res = decoding_ru(N, A, B, k)
    else:
        res = decoding_en(N, A, B, k)
        
print(*res, sep='')

# X = 'otemporaomoresaa'

# Y = 'qekdmdtarfisaaqm'

# A = 12 15 26 2 25 7 1 5 15 24 16 8 4 15 18 21
# A_inv = 8 2 1 12 5 2 24 6 8 7 9 9 19 12 22 13
# otemporaomoresaa -> jbupawbesnangsya