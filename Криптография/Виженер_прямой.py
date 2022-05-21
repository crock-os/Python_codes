lang_en = [chr(i) for i in range(97, 123)]
lang_ru = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

def encoding_ru(X, key):
    x = [lang_ru.index(c) for c in X]
    k = [lang_ru.index(c) for c in key]
    k = k*(len(x)//len(k)) + k[:len(x)%len(k)]
    r = []
    
    for i in range(len(x)):
        r.append((x[i] + k[i])%33)
        
    print('x =', *x)
    print('k =', *k)
    print('r =', *r)
    res = [lang_ru[i] for i in r]
    print('Y = ', *res, sep='')
    
def encoding_en(X, key):
    x = [lang_en.index(c) for c in X]
    k = [lang_en.index(c) for c in key]
    k = k*(len(x)//len(k)) + k[:len(x)%len(k)]
    r = []
    
    for i in range(len(x)):
        r.append((x[i] + k[i])%26)
        
    print('x =', *x)
    print('k =', *k)
    print('r =', *r)
    res = [lang_en[i] for i in r]
   print('Y = ', *res, sep='')

def decoding_ru(Y, key):
    y = [lang_ru.index(c) for c in Y]
    k = [lang_ru.index(c) for c in key]
    k = k*(len(y)//len(k)) + k[:len(y)%len(k)]
    r = []
    
    for i in range(len(y)):
        r.append((y[i] - k[i])%33)
        
    print('y =', *y)
    print('k =', *k)
    print('r =', *r)
    res = [lang_ru[i] for i in r]
    print('X = ', *res, sep='')
    
def decoding_en(Y, key):
    y = [lang_en.index(c) for c in Y]
    k = [lang_en.index(c) for c in key]
    k = k*(len(y)//len(k)) + k[:len(y)%len(k)]
    r = []
    
    for i in range(len(y)):
        r.append((y[i] - k[i])%26)
        
    print('y =', *y)
    print('k =', *k)
    print('r =', *r)
    res = [lang_en[i] for i in r]
   print('X = ', *res, sep='')

type_w = input('Шифрование/Расшифровка(Ш/Р): ').lower()

lang = input('Язык(ру/en): ').lower()
key = list(input('Ключ: ').lower())

N = list(input('Слово: ').lower())

if type_w == 'ш' or type_w == 'i':
    if lang == 'ру':
        encoding_ru(N, key)
    else:
        encoding_en(N, key)
else:
    if lang == 'ру':
        decoding_ru(N, key)
    else:
        decoding_en(N, key)
    
