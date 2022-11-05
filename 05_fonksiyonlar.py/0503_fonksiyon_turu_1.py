# region fonksiyon_turu_1_parametre_almayan_deger_dondurmeyen
"""
Fonksiyon tanımlama anında argüman almaz, değer döndürmez

def kullaniciGiris():
    kAd = input("Kullanıcı Adınız : ")
    print(f"hoşgeldiniz {kAd}")
kullaniciGiris()
"""

#a.isdigit(): true or false

#region toplama fonks
# def toplam():
#     deger1=int(input("Lütfen sayi giriniz: "))
#     deger2=int(input("Lütfen sayi giriniz: "))
#     print(f"sayiların toplamı {deger1+deger2}")

# toplam()
#endregion

#region askerlik
# def isValid(dTarihi):
#     yas=2022-dTarihi
#     if yas>=19:
#         print("askere gidebilirsin")
#     else:
#         print("12 yıllık kesintisiz eğtimine devam et")

# isValid(2020)            
# endregion

# region askerlik2
# def isValid(dTarihi):
#     if str(dTarihi).isdigit():
#         yas = 2022-int(dTarihi)
#         if yas>=19:
#             print("askere gidebilirsin")
#         else:
#             print("12 yıllık kesintisiz eğitimine devam et, askerlik senin için biraz beklesin")
#     else:
#         hataKodu100()



# def hataKodu100():
#     print("lütfen sayısal değer giriniz")

# isValid("ağustos")
#endregion

#region saat
# def selamlama(ad:str):
#     import datetime
#     saat = datetime.datetime.now().hour
#     if saat < 12:
#         print(f"Günaydın {ad}")
#     else:
#         print(f"Merhaba {ad}")

# selamlama("İbrahim")
#endregion





