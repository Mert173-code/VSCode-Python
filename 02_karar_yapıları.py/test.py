"""
Kargo Bedeli 7.5 TL.’dir
Satın Alınan Ürünlerin Toplam Fiyatı 250 TL üzeri olduğunda kargo bedavadır.
Kullanıcıdan fiyat bilgisi alıp ekrana ödenecek tutarı yazan prog.?
"""


"""
kargo_bedeli = 7.5
urun_tutar=float(int("Lütfen ürünlerin fiyatını giriniz: "))
if urun_tutar >250 :
    print("Kargo ücretsizdir")
if 250 < urun_tutar :
    print("f {urun_tutar} tutarında alışveriş yaptınız için kargo bedeli {kargo_bedeli} TL'dir. ")    
"""

"""
bakiye = 10000
bankaKodu = int(input("Lütfen banka kodunu giriniz\t: "))
transferBanka = int(input("Lütfen transfer edilecek banka kodunu giriniz\t:"))
transferToplamTutar = int(input("Lütfen transfer miktarını giriniz\t: "))
kesinti = "%5"


if bankaKodu == transferBanka:
    bakiye -= transferToplamTutar
    print(f"Bankamız bu işlem için sizden ücret almayacaktır. Yeni bakiyeniz {bakiye} TL dir.")
if bankaKodu != transferBanka:
    bakiye = bakiye - (transferToplamTutar*0.05) - transferToplamTutar
    print(f"Bakmanız bu işlem için sizden {kesinti} ücret alacaktır. Yeni bakiyeniz {bakiye} TL dir.")
"""


"""
Y.İçi Uçuşlarda KDV %18'dir.
Kontuar Görevlisi Fiyat Girecek.
Bavul Ağırlığı 15kg. üzerinde her bir ağırlık için bilet fiyatına 5 TL. ek ücret güncellemesi yapacak.
Günün sonunda güncel fiyat ekrana yazılacak.
"""

"""
bilet_fiyati = int(input("Bilet fiyatını giriniz : "))
bavul_agirligi = int(input("Bavul Ağırlıgını giriniz : "))

if bavul_agirligi > 15:
    fark = bavul_agirligi-15
    bilet_fiyati += fark*5
 
print(f"Güncel fiyat roundP{bilet_fiyati*1.18} .") 
"""


"""
L. 1. Sınav Notu Giriniz    : 90
L. 2. Sınav Notu Giriniz    : 100
Yıl Sonu Notunuz 95, Başarı Durumu Pekiye
"""
"""
sınav1,sınav2=int(input("1. Sınav Notunuz giriniz : ")) ,int(input("2.Sınav Notunu giriniz "))
ort=(sınav1+sınav2)/2

if ort>=85 :
    print(f"Yıl Sonu Notunuz {ort} , Başarı Durumu Pekiye")
elif ort>=70 :
    print(f"Yıl Sonu Notunuz {ort} , Başarı Durumu iyi")

elif ort>=55:
    print(f"Yıl Sonu Notunuz {ort} , Başarı Durumu orta")

elif ort>=45:
    print(f"Yıl Sonu Notunuz {ort} , Başarı Durumu geçer")

else :
   print(f"Yıl Sonu Notunuz {ort} , Başarı Durumu kötü")
   
"""


"""
id="admin"
pw="123"

keyid=input("TCKN veya e-posta adresinizi giriniz:\t→")
keypw=input("Lütfen parolanızı giriniz:\t→")

if id == keyid:
    if pw == keypw:
        print("Login Başarılı")
    else:
        print("Parola Hatalı, Lütfen Tekrar Deneyin")
else:
    print("Kullanıcı Adı Hatalı, Lütfen Tekrar Deneyin")
"""


"""
Lütfen 1. Sayı Giriniz  : 63
Lütfen 2. Sayı Giriniz  : 2
Lütfen 3. Sayı Giriniz  : 25
63 > 25 > 2
"""

"""
s1=int(input("Lütfen 1. Sayı Giriniz  :"))
s2=int(input("Lütfen 2. Sayı Giriniz  :"))
s3=int(input("Lütfen 3. Sayı Giriniz  :"))

#s1,s2 = s2 ,s1


if s1<s2 :
    s1,s2 = s2, s1 

if  s2<s3 :
    s2,s3=s3,s2

if  s1< s3 :
    s1 ,s3 =s3 ,s1

    print(f"Sıralama : {s1} > {s2} > {s3}  ")

"""


"""
aKenari = int(input("Lütfen A Kenarını Giriniz\t: "))
bKenari = int(input("Lütfen B Kenarını Giriniz\t: "))

if aKenari == bKenari:
    print(f"Karenin alanı {aKenari*bKenari} metre karedir")
else:
    print(f"Diktörgenin alanı {aKenari * bKenari} metre karedir")
"""


"""
Lütfen Kısa Kenarı Giriniz : 25
Lütfen Uzun Kenarı Giriniz : 15
Uzun Kenar, Kısa Girilemez
"""
"""
uzunKenar = int(input("Lütfen uzun kenarı giriniz: "))
kısaKenar = int(input("Lütfen kısa kenarı giriniz: "))

if uzunKenar < kısaKenar:
    print("Uzun Kenar, Kısa Girilemez")
else:
    cevre = 2*(uzunKenar+kısaKenar)
    print(f"Şeklin çevresi {cevre} ")
"""