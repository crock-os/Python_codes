import numpy as np

k = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# K = np.matrix(k).reshape(5,5)

def encoding(x, K):
    if len(x)%2 == 1:
        x.append('a')
    r = []
    
    for i in range(len(x)):
        if x[i] == 'j':
            x[i] = 'i'
    
    while len(x) > 0:
        q = x[:2]
        
        i = k.index(q[0])//5
        j = k.index(q[0])%5
    
        s = k.index(q[1])//5
        m = k.index(q[1])%5
    
        if i == s:
            r.append(K[i, (j+1)%5])
            r.append(K[s, (m+1)%5])
        elif j == m:
            r.append(K[(i+1)%5, j])
            r.append(K[(s+1)%5, m])
        else:
            r.append(K[i, m])
            r.append((K[s, j]))
            
        x = x[2:]
        
    print('y = ', *r, sep='')
    
def decoding(y, K, Km):
    r = []
    
    # for i in range(len(y)):
    #     if y[i] == 'j':
    #         y[i] = 'i'
    
    while len(y) > 0:
        q = y[:2]
        
        i = K.index(q[0])//5
        j = K.index(q[0])%5
    
        s = K.index(q[1])//5
        m = K.index(q[1])%5
    
        if i == s:
            r.append(Km[i, (j-1)%5])
            r.append(Km[s, (m-1)%5])
        elif j == m:
            r.append(Km[(i-1)%5, j])
            r.append(Km[(s-1)%5, m])
        else:
            r.append(Km[i, m])
            r.append((Km[s, j]))
            
        y = y[2:]
        
    print('x = ', *r, sep='')

# X = list('juicer'.lower())
# Y = list('kthdbu'.lower())

# X = list('Helloy'.lower())
# Y = list('kcmmtd'.lower())

# X = list('manufacturing'.lower())
# Y = list('lbpslfdsqshofb'.lower())

type_w = input('Шифрование/Расшифровка(Ш/Р): ').lower()

N = list(input('Слово: ').lower())

K = list(input('Ключ: ').lower())


for c in k:
    if c not in K:
        K.append(c)
        
Km = np.matrix(K).reshape(5,5)

if type_w == 'ш' or type_w == 'i':
    encoding(N, K)
else:
    decoding(N, K, Km)

