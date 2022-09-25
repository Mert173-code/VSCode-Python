"""
i = 0
x = 0
while i < 100:
    if i % 2 != 0:
        if i==49:
            print(".." ,end=" ")
        else:
            print(i,end=" ")

        x+=1
        if x==10 :
            print()
            x=0
"""

"""
sayi=int(input("1 ve 9 arası rakam giriniz:\t"))
i=1
while i<=sayi:
    print(f"{sayi}x {i} = {sayi*i}" , end="\n")
    i+=1
"""

"""
sayi = int(input("Lütfen Sayı Giriniz [1-9]: "))
i = 1
if sayi<1:
    print("lütfen 1-9 arası rakam giriniz")
elif sayi>9:
    print("lütfen 1-9 arası rakam giriniz")
else:
    while i <= sayi:
        print(f"{sayi}x{i} = {sayi*i}")
        i += 1
"""




"""
i = 1
sonuc = 1
while i <=5 :
    sonuc *= i
    print(f" {i},{sonuc} "  )
    i += 1
"""


""" 
Lutfen bir rakam giriniz : 7
7 14 21
7 ye tam bolenlerinin adedi 8

"""



"""
i = 1
counter=0
sayi=int(input("Lütfen bir rakam giriniz :"))

while i < 100:
    if i % sayi == 0:
        print(i, end=" ")
        counter +=1
    i+=1

print(f"\n{sayi} ya tam bolunenlerin adedi {counter}")
"""




























