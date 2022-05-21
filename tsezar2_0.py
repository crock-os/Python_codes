lg_en = [chr(i) for i in range(97, 123)]
u_lg_en = [chr(i) for i in range(65, 91)]
global rz

if True:
    lg_ru = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    u_lg_ru = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
    rz = 33
else:
    lg_ru = [chr(i) for i in range(1072, 1104)]
    u_lg_ru = [chr(i) for i in range(1040, 1072)]
    rz = 32 

def encription(lang, q, k):
    r = []
    if lang == 'ру':
        z = rz
        for c in q:
            if c.isdigit() or c in ('.\'",?! -'):
                a = c
                r.append(a)
            else:
                if c in lg_ru:
                    a = lg_ru.index(c)
                    r.append(lg_ru[(a+k)%z])
                else:
                    a = u_lg_ru.index(c)
                    r.append(u_lg_ru[(a+k)%z])    
    else:
        z = 26
        for c in q:
            if c.isdigit() or c in ('.\'",?! -'):
                a = c
                r.append(a)
            else:
                if c in lg_en:
                    a = lg_en.index(c)
                    r.append(lg_en[(a+k)%z])
                else:
                    a = u_lg_en.index(c)
                    r.append(u_lg_en[(a+k)%z])  
    return r

def decription(lang, q, k):
    r = []
    if lang == 'ру':
        z = rz
        for c in q:
            if c.isdigit() or c in ('.\'",?! -'):
                a = c
                r.append(a)
            else:
                if c in lg_ru:
                    a = lg_ru.index(c)
                    r.append(lg_ru[(a-k)%z])
                else:
                    a = u_lg_ru.index(c)
                    r.append(u_lg_ru[(a-k)%z])   
    else:
        z = 26
        for c in q:
            if c.isdigit() or c in ('.\'",?! -'):
                a = c
                r.append(a)
            else:
                if c in lg_en:
                    a = lg_en.index(c)
                    r.append(lg_en[(a-k)%z])
                else:
                    a = u_lg_en.index(c)
                    r.append(u_lg_en[(a-k)%z])  
    return r
    
s = input('Шифрование, расшифровка или взлом(Ш/Р/В): ')
    
lang = input('Язык:(ру/en) ')

n = input('Фраза: ')

q = []

for c in n:
    q.append(c)

if s.lower() == 'ш':
    k = int(input('Сдвиг: '))
    r = encription(lang, q, k)
    print(*r, sep='')
elif s.lower() == 'р':
    k = int(input('Сдвиг: '))
    r = decription(lang, q, k)
    print(*r, sep='')
elif s.lower() == 'в':
    if lang == 'ру':
        for i in range(rz):
            r = decription(lang, q, i)
            print('Шаг: ', i, ' - ', *r, sep='')
    elif lang == 'en':
        for i in range(26):
            r = decription(lang, q, i)
            print(*r, sep='')
    
