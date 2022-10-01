"""
i=1
while i<11:
    if i==5:
        break
    print(f"{i}.döngü")
    i+=1
"""


"""
eb = -9999999999999
while True:
    sayi = int(input("lütfen sayı giriniz, durmak için -1 yazın : "))
    if sayi==-1:
        break
    if sayi >eb:
        eb=sayi
print(f"en büyük sayı {eb}")
"""

"""
eb = -9999999999999
say=0
while True:
    sayi = int(input("lütfen sayı giriniz, durmak için -1 yazın : "))
    if sayi==-1:
        break
    say+=1
    if sayi >eb:
        eb=sayi
if say==0:
    print("Hiç bir sayı girmediniz.")
else: 
    print(f"en büyük sayı {eb}")
"""

"""
sayi = 33
birler = sayi % 10
onlar = sayi // 10
if birler>4:
    onlar += 1
    print(f"{onlar}0")
else:
    print(f"{onlar}0")
"""

# x = """
#     [1]     km  → mil
#     [2]     mil → km
#     [3]     çık
# """

# # menu = "[1]     km  → mil\n[2]     mil → km\n[3]     çık"
# while True:
#     print(x)
#     secim = input("Lütfen seçim yapınız: ")
#     if secim == "1":
#         km = int(input("Lütfen km bilgisini giriniz: "))
#         mil = km * 0.62137
#         print(mil)
#     elif secim == "2":
#         mil = int(input("Lütfen mil bilgisini giriniz: "))
#         km = mil / 0.62137
#         print(round(km, 2))
#     elif secim == "3":
#         print("Çıkış yapıldı!")
#         break
#     else:
#         print("Hatalı tuşlama yaptınız!")






























