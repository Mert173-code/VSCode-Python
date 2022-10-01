
"""
yil = 2022
toplam = 0
while True:
    yillikGelir = int(input(f"{yil} yılı geliriniz?"))
    yil += 1
    if yillikGelir == 0:
        print("bb")
        break
    if yillikGelir < 32000:
        vergiOrani = 0.15
    elif yillikGelir >= 32000 or yillikGelir < 70000:
        vergiOrani = 0.20
    elif yillikGelir >= 70000 or yillikGelir < 250000:
        vergiOrani = 0.27
    elif yillikGelir >= 250000 or yillikGelir < 880000:
        vergiOrani = 0.35
    else:
        vergiOrani = 0.40
    if yil == 2027:
        break
    # print(f"Verginiz {yillikGelir*vergiOrani} TL'dir.")
    toplam += (yillikGelir*vergiOrani)
print(f"5 yıllık ödediğiniz gelirler vergisi toplamınız {toplam} TL'dir. ")

"""

#Vücüt kitle indeksi
#vki = kg/m*m
while True:
    kilo= float(input("Lütfen kilonuzu giriniz \t:"))
    boy=float(input("Lütfen boyunuzu giriniz \t: "))
    vci = kilo / ( boy**2 )

    if vci <18.5:
        print("vücüt kitle indeksi zayıf")
    elif vci>18.5 and vci<24.9:
        print("ideal")
    elif vci >25 and vci<29.9:
        print("şişman")   
    elif vci>34.9 and vci<30:
        print("obez")





















































