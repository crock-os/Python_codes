def p_to_ten(n, p):
    ln = list(n)
    
    a = ['A', 'B', 'C', 'D', 'E', 'F']
    r = 0
    
    for i in range(len(ln)):
        if ln[i] in a:
            r += (10 + a.index(ln[i]))*p**(len(ln)-i-1)
        else:
            r += int(ln[i])*p**(len(ln)-i-1)
    return r

def ten_to_p(n, p):
    a = ['A', 'B', 'C', 'D', 'E', 'F']
    n = int(n)
    ln = []
    r = ''
    
    while n > 0:
        s = n%p
        ln.append(s)
        n //= p
    
    for c in ln:
        if c < 10:
            r += str(c)
        else:
            r += a[c-10]
    return r[::-1]
    

q = input('Выберете метод (1) p->10 / (2) 10->p: ')

n = input('Введите число: ')
p = int(input('Введите порядок: '))

if q == '1':
    r = p_to_ten(n, p)
else:
    r = ten_to_p(n, p)
 
print(r)

