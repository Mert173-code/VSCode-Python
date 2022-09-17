
"""
rakam = int(input("lütfen 0-9 arası rakam giriniz: "))
print("girdiğiniz rakamın 1 fazlası" + str((rakam+1)))
"""


# print("girdıgınız rakamın 1 fazlası  {}" . format(rakam+1))



# a=5
# b=10
# c=a+b
# print(f"girilan {a} ve {b} değerleri toplamı {c}")




# kilo = int(input("lütfen kilonuzu giriniz : "))
# boy = float(input("lütfen boyunuzu giriniz : "))
# vki=kilo/boy**2

# print(f"boyu {boy} mt kilosu {kilo} kg olan nisa'nın vki değeri, {round(vki,2)} ")



"""
Lütfen 1. Sayı Giriniz  : 5
Lütfen 2. Sayı Giriniz  : 10
Lütfen 3. Sayı Giriniz  : 45
Girilen 5, 10, 45 sayılarının ortalaması 20.0
"""


# sayi1=int(input("Lütfen 1. Sayı Giriniz :"))
# sayi2=int(input("Lütfen 2. Sayı Giriniz :"))
# sayi3=int(input("Lütfen 3. Sayı Giriniz :"))
# ort=(sayi1+sayi2+sayi3)/3 
# print(f"Girilen {sayi1} ,{sayi2} ,{sayi3} sayılarının ortalaması ,{ort} ")



# boy = 168
# m = boy//100
# cm= boy%100
# print(m, "metre", cm, "santim.")


# boy=int(input("Lütfen boyunuzu giriniz :"))
# m = boy//100
# cm= boy%100
# print(f" {m} metre {cm} santim")







"""
Yarı Çap Bilgisi Giriniz : 10
10 cm. yarıçap değerine sahip dairenin alanı ... cm kare, çevresi cm dir.
"""



# yariCap=int(input("Yarı Çap Bilgisi Giriniz: "))
# alan=3.14*(yariCap)**2
# cevre=2*3.14*yariCap
# print(f"{yariCap}cm.  yaricap değerine sahip dairenin alanı {alan} cm kare , çevresi {cevre}dir. ")




"""
saat = 2
ekrandaki 2 saat değerinin saniye karşılığı 7200 sn.
"""

# saat=int(input("Saat="))
# print(f"ekrandaki {saat} saat değerini saniye karşılıgı {saat*3600} sn.")

# saat = int(input("Bir saat giriniz : "))
# saniye = (60**2)*saat

# print(f"ekrandaki {saat} saat değerinin saniye karşılığı {saniye} sn.")




s = int(input("lütfen sayı giriniz\t: "))
kalan = s % 10
birler = kalan//1
kalan = s % 100
onlar = kalan//10
kalan = s % 1000
yuzler = kalan//100
print(f"basamakları {yuzler} {onlar} {birler} sayının haneleri toplamı {yuzler+onlar+birler}")





















