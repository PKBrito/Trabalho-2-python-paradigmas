def converta(h, m):
    if 0 < h < 12 and 0 <= m < 60:
        print(f'{h}:{m} AM')
        
    elif 12 <= h and 0 <= m < 60:
        h= h - 12
        print(f'{h}:{m} PM')
        
    elif 0 == h and m == 0 :
        
        print(f'{h + 12}:{m} AM')
        
    else:
        print('Valor inválido')

while True:
    h = int(input('Hora: '))
    if h <= -1: break
    m = int(input('Minuto: '))
    converta(h,m)
    print('='*12)