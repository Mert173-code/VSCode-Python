

"""
eb = -9999999999999
i = 0
while i<5:
    sayi = int(input("lütfen sayı giriniz : "))
    if sayi >eb:
        eb=sayi
    i += 1
print(f"en büyük sayı {eb}")
"""

# region giris
# loop
# loop ne zaman kullanılır?
# loop → sürekli tekrarlayan işlemlerin yapılmasını sağlayan komutlardır
"""
print("24 saatte kargoda")
print("24 saatte kargoda")
print("24 saatte kargoda")
i = 0
while i<1000:
    i +=1
    print("12 saatte kargoda")
"""
# endregion

# region aman_dikkat
"""
while True:
    print("şu an while döngüsü içindeyim")
"""
# endregion

#region while_yazim_kurallari
"""
1 → BAŞLANGIÇ
2 → BİTİŞ
3 → ARTIŞ MİKTARI
 
i = 0
print("a")
while i<=3:
    i +=1
    print("b")
print("c")
""" 
#endregion

# region dikkat_edilmesi_gereken_kurallar
"""
i = 1
while i<3:   # i büyük 3 olduğu sürece DÖN   
    print("sponsorlu ürün")
"""    
# endregion

# region ornek_1
"""
i = 1
print("a")
while i<=3:
    print("b")
    i += 1
print("c")
"""
# endregion

# region ornek_2
"""
sayac = 1
while sayac<=5:
    print(sayac)
    sayac += 1
"""
# endregion

# region ornek_3
"""
sayac = 5
while sayac:       #yada sayac != 0:
    print(sayac)
    sayac -= 1
# def. da siz koşulu int bir tam sayıya bağlı olarak yazarsanız
# tam sayı 0 olduğunda döngü kırılır
"""

"""
sayac = 5
devamMi = True
while devamMi: 
    print(sayac)
    if sayac==2:
        devamMi=False
    sayac -= 1
"""

# endregion




"""
lütfen sayı giriniz, çıkmak için 0... : 3
lütfen sayı giriniz, çıkmak için 0... : 6
lütfen sayı giriniz, çıkmak için 0... : 12
lütfen sayı giriniz, çıkmak için 0... : 10
lütfen sayı giriniz, çıkmak için 0... : 11
lütfen sayı giriniz, çıkmak için 0... : 0
girdiğiniz tek sayıların toplamı 14
"""


#tek_sayilar_top = 0
# sayi = int(input("Lütfen bir sayı giriniz, çıkmak için 0 yazın: "))
# while sayi != 0 :
#     if sayi % 2 == 1 :
#         tek_sayilar_top += sayi
#     sayi = int(input("Lütfen bir sayı giriniz, çıkmak için 0 yazın: "))       
# print(f"Girdiğiniz sayıların toplamı: {tek_sayilar_top} ")
      

"""
tekSayiAdeti=0
ciftSayiAdeti=0
sayi=int(input("Lütfen sayı giriniz, çıkmak için 0 yazınız.."))
while sayi !=0:
    if sayi % 2 ==1:
        tekSayiAdeti+=1
    else:
        ciftSayiAdeti+=1
    sayi=int(input("Lütfen sayı giriniz, çıkmak için 0 yazınız.."))
print(f"{tekSayiAdeti} adet tek sayı vardır. {ciftSayiAdeti} adet çift sayı vardır.")
"""


"""
secret = "susam"

answer = input("açıl ... açıl, Lütfen boşluğu doldurun: ")
deneme = 0
while answer != secret:
    print("heheheheeh ne oldu çıkamıyor musun : -)")
    answer = input("açıl ... açıl, Lütfen boşluğu doldurun: ")
    deneme += 1
print(f"{deneme} kez denediniz!")

"""







































