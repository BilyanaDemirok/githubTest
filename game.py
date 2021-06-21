import random

gizli_sayi = random.randrange(1,20)
# print(gizli_sayi)

tahmin = 0
Deneme = 0
while tahmin != gizli_sayi:
    tahmin = int(input('1 den 20 ye kadar bir sayi yaz:'))
    Deneme = Deneme + 1

    if tahmin < gizli_sayi:
        print('Yukari')
    elif tahmin > gizli_sayi:
        print('Asagi')
    else:
        print('Bildin!')

print('Deneme Sayisi: ', Deneme)

