"""
Eklenecek Film Adı Giriniz. Çıkmak İçin -1  : yeşil yol
Eklenecek Film Adı Giriniz. Çıkmak İçin -1  : titanik
Eklenecek Film Adı Giriniz. Çıkmak İçin -1  : rocky
Eklenecek Film Adı Giriniz. Çıkmak İçin -1  : yüzüklerin efendisi
Eklenecek Film Adı Giriniz. Çıkmak İçin -1  : -1
yeşil yol, titanik, rocky, yüzüklerin efendisi
"""

# print("""
#         1-Ekle     
#         2-Cıkart 
#         3-Listele
#         4-cıkamak 

#               """)



# favoriFilm=[] 
    #while True:
    # x=int(input("Lütfen seçimizi yapınız: "))
    # if x==4:
    #     break
    # elif x==1:
    #     film=input("Eklenecek Film Adı Girin : ")
    #     favoriFilm.append(film)
    # elif x==2:
    #     film=input("Cıkarılcak film adı giriniz: ")
    #     favoriFilm.remove(film)
    # elif x==3:
    #     for i in range(0,len(favoriFilm)):
    #         print(f"{i+1}. filmin adı {favoriFilm[i] } ")
    # else: 
    #     print("Hatalı seçim")    

   
# print(favoriFilm)    

#ctrl + c donguyu kır


# ogrenciListesi = ["furkan", "ahmet", "sena", "eda", "mert", "şakir", "ayşe"]
# x = 1
# for i in ogrenciListesi:
#     print(f"{x}. {i}")
#     x+=1
# print("-"*50)
# for i in range(0, len(ogrenciListesi)):
#     print(f"{i+1}. {ogrenciListesi[i]}")


"""
notlar=[]
while True:
    oAdSoyad = input("Ad-Soyad Girin, Çıkmak İçin -1\t: ")
    if oAdSoyad=="-1":
        break
    n1 = int(input(f"{oAdSoyad} isimli öğrencinin 1.Notu : "))
    n2 = int(input(f"{oAdSoyad} isimli öğrencinin 2.Notu : "))
    ort = (n1+n2)/2
    notlar.append(ort)
notlar.sort()
for i in notlar:
    print(i)
print(f"en düşük not {min(notlar)}- en yüksek not {max(notlar)}")

"""

#CÜMLE KESME
"""
aciklama = "Word, belgenizin profesyonelce üretilmiş görünmesini sağlamak için birbirini tamamlayan üst bilgi, alt bilgi, kapak sayfası ve metin kutusu tasarımları sağlar. Örneğin, birbiriyle uyumlu bir kapak sayfası, başlık ve kenar çubuğu ekleyebilirsiniz. Ekle'ye tıklayın ve ardından farklı galerilerden eklemek istediğiniz öğeleri seçin."
# print(len(aciklama))
yeni = ""
x = 0
if len(aciklama) > 30:
    for i in aciklama:
        yeni += i
        x += 1
        if x==30:
            break
print(f"{yeni}...")

"""


























