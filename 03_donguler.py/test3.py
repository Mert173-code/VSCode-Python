"""
sayi1 = int(input("Lütfen sayı girin: "))
sayi2 = int(input("Lütfen sayı girin: "))

ek, obeb = 0, 0

if sayi1 < sayi2 :
    ek = sayi1
else:
    ek = sayi2
for i in range(1, ek+1):
    if sayi1 % i == 0 :
        if sayi2 % i == 0 :
            obeb = i
print(f" {obeb} ")

"""


# sayi1 = int(input("Lütfen sayı girin: "))
# sayi2 = int(input("Lütfen sayı girin: "))

# obeb = 0
# for i in range(1, min(sayi1, sayi2)+1):
#     if sayi1 % i == 0 :
#         if sayi2 % i == 0 :
#             obeb = i
# print(f" {obeb} ")



#TAU sayısı 
"""
sayac = 0
sayi = int(input("Lütfen bir sayı giriniz : "))
for i in range(1, sayi+1):
    if sayi % i == 0:
        sayac += 1
if sayi % sayac == 0:
    print(f"{sayi} sayısı TAU'dur.")
else:
    print(f"{sayi} sayısı TAU değildir.")
"""

#Mükemmel sayi
"""
toplam=0
sayi=int(input("Lütfen sayı giriniz:\t"))
for i in range (1,sayi):
    if sayi % i==0:
        toplam+=i
if sayi==toplam:
    print(f"{sayi} sayısı mükemmel sayıdır")
else:
    print(f"{sayi} sayısı mükemmel sayı değildir.")
"""

















