# a=[
#     [1,2,3,4],
#     [2,4,6,8]
# ]

# for i in range(2): #0,1
#     for j in range(4): #0,1,2,3
#         print(a[i][j], end=" ")
#     print()    



# cihazListesi = [
#     [1, "Desktop_Test", 56, "chrome.exe"],
#     [2, "Guest101", 60, "excel.exe"],
#     [3, "Kat-1_Laptop", 90, "camtasia.exe, chrome.exe"]
# ]
# for i in range(len(cihazListesi)):
#     for j in range(len(cihazListesi[i])):
#         if j == 2:
#             print(f"%{cihazListesi[i][j]}", end=" ")
#         else:
#             print(cihazListesi[i][j], end=" ")
#     print()


# for i in range(8):
#     row=["piyon"for j in range(8)]
#     print(row)



# for i in range(8):
#     row = ["piyon" for j in range(8)]
#     print(row)



# row = [["piyon" for j in range(8)] for i in range(8)]
# print(row)

# row = [[f"{i}{j}" for j in range(24)] for i in range(7)]
# print(row[6][23])








while True:
     birler = ["","bir","iki","üç","dört","beş","alt","yedi","sekiz","dokuz"]
     onlar =  ["","on","yirmi","otuz","kırk","elli","atmış","yetmiş","seksen","doksan"]
     sayi=int(input("Lütfen sayi giriniz: "))

     s=str(sayi)
     
     print(onlar[int(s[0])],birler[int(s[1])])



iftaarListesi = []
for i in ogrenciler:
    if i[3] == 100:
        iftaarListesi.append(i)
print(iftaarListesi)
 