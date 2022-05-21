lang_en = [chr(i) for i in range(97, 123)]
lang_ru = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

def encoding_ru(X, k):
    x = [lang_ru.index(c) for c in X]
    r = []
    
    for i in range(len(x)):
        r.append((x[i] + k)%33)
        
    print('x =', *x)
    print('r =', *r)
    res = [lang_ru[i] for i in r]
    print('Y = ', *res, sep='')
    
def encoding_en(X, k):
    x = [lang_en.index(c) for c in X]
    r = []
    
    for i in range(len(x)):
        r.append((x[i] + k)%26)
        
    print('x =', *x)
    print('r =', *r)
    res = [lang_en[i] for i in r]
    print('Y = ', *res, sep='')
    
def decoding_ru(Y, k):
    y = [lang_ru.index(c) for c in Y]
    r = []
    
    for i in range(len(y)):
        r.append((y[i] - k)%33)
        
    print('y =', *y)
    print('r =', *r)
    res = [lang_ru[i] for i in r]
    print('X = ', *res, sep='')
    
def decoding_en(Y, k):
    y = [lang_en.index(c) for c in Y]
    r = []
    
    for i in range(len(y)):
        r.append((y[i] - k)%26)
        
    print('k = ', k, 'r =', r, ' ', end='')
    # print('y =', *y)
    # print('r =', *r)
    res = [lang_en[i] for i in r]
    print('X = ', *res, sep='')
    
type_w = input('Шифрование/Расшифровка/Взлом(Ш/Р/В): ').lower()

lang = input('Язык(ру/en): ').lower()
k = int(input('Сдвиг: ').lower())

N = list(input('Слово: ').lower())

if type_w == 'ш' or type_w == 'i':
    if lang == 'ру':
        encoding_ru(N, k)
    else:
        encoding_en(N, k)
elif type_w == 'р' or type_w == 'h':
    if lang == 'ру':
        decoding_ru(N, k)
    else:
        decoding_en(N, k)
else:
    for i in range(26):
        decoding_en(N, i)
        
        