lg_en = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lg_ru = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

def encription(lang, q, k):
    r = []
    if lang == 'ру':
        z = 33
        for c in q:
            a = lg_ru.index(c)
            r.append(lg_ru[(a+k)%z])
    else:
        z = 26
        for c in q:
            a = lg_en.index(c)
            r.append(lg_en[(a+k)%z])
    return r

def decription(lang, q, k):
    r = []
    if lang == 'ру':
        z = 33
        for c in q:
            a = lg_ru.index(c)
            r.append(lg_ru[(a-k)%z])
    else:
        z = 26
        for c in q:
            a = lg_en.index(c)
            r.append(lg_en[(a-k)%z])
    return r
    
s = input('Шифрование или расшифровка(Ш/Р): ')
    
lang = input('Язык:(ру/en) ')

n = input('Фраза: ')

q = []

for c in n:
    if c not in ('.,?! -'):
        q.append(c.lower())
        
k = int(input('Сдвиг: '))

if s.lower() == 'ш':
    r = encription(lang, q, k)
    print(*r, sep='')
elif s.lower() == 'р':
    r = decription(lang, q, k)
    print(*r, sep='')
