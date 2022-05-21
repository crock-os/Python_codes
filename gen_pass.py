from random import sample

l_u = [chr(i) for i in range(65,91)]
l_s = [chr(i) for i in range(97, 123)]
l_d = range(10)
l_r = ('!#$%&*+-=?@^_.')

global l, u, s, d, n, r

l = input('Введите длину пароля: ')
while True:
    if not l.isdigit():
        print('Нужно ввести число!')
        l = input('Введите длину пароля: ')
    else:
        l = int(l)
        break

u = input('Включать заглавные буквы?(Д/Н) \n')
while True:
    if u.lower() != 'д' and u.lower() != 'н':
        print('Некорректный ввод!')
        u = input('Включать заглавные буквы?(Д/Н) \n')
    else:
        break
    
s = input('Включать строчные буквы?(Д/Н) \n')
while True:
    if s.lower() != 'д' and s.lower() != 'н':
        print('Некорректный ввод!')
        s = input('Включать строчные буквы?(Д/Н) \n')
    else:
        break
        
d = input('Включать цифры?(Д/Н) \n')
while True:
    if d.lower() != 'д' and d.lower() != 'н':
        print('Некорректный ввод!')
        d = input('Включать цифры?(Д/Н) \n')
    else:
        break
    
r = input('Включать знаки препинания?(Д/Н) \n')
while True:
    if r.lower() != 'д' and r.lower() != 'н':
        print('Некорректный ввод!')
        r = input('Включать знаки препинания?(Д/Н) \n')
    else:
        break
    
p = []

if u == 'д':
    p.extend(l_u)
    
if s == 'д':
    p.extend(l_s)
    
if d == 'д':
    p.extend(l_d)
    
if r == 'д':
    p.extend(l_r) 
    
    
n = input('Сколько паролей надо сгенерировать? \n')
while True:
    if not n.isdigit():
        print('Нужно ввести число!')
        n = input('Сколько паролей надо сгенерировать? ')
    else:
        n = int(n)
        break
      
print('Итоговая последовательность - ', *p, sep='')
        
for i in range(n):
    P = sample(p, l)
    print(*P, sep='')