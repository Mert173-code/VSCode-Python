# random
# built-in
"""
#Random çağirma 
import random
print(random.random())

"""
# Random çagirma2
"""
import random as rnd
# print(rnd.random())

for i in range(5):
    print(rnd.random(), end=",")
 
"""
# region randrange
# from random import randrange
# print(randrange(3)) #min<=x < max 0,1,2
# print(randrange(3,6)) #min<=x < max 3,4,5

# for i in range(25):
#     print(randrange(3, 6+1), end=",")

# from random import randrange
# print(randrange(10,50,10))
# endregion

# from random import randrange, randint
# for i in range(10):
#     print(randint(3,6), end=",")

# region seed

# import random
# random.seed("araba")
# print(f"1.Sayı {random.randint(25,75)}")
# random.seed("araba")
# print(f"2.Sayı {random.randint(25,75)}")
# random.seed("araba2")
# print(f"2.Sayı {random.randint(25,75)}")
# random.seed("araba")
# print(f"2.Sayı {random.randint(25,75)}")
# endregion
# region rasgele çekilis

# from random import sample, choice ,randrange
# oListesi=["irem","mert","furkan","ibrahim"]
# i=randrange(0,4)
# #print(oListesi[i])
# _1,_2, _3,_4=0, 0, 0, 0
# for i in range(100):
#     i= randrange(0, 4)
#     if i==0:
#         _1 +=1
#     elif i==1:
#         _2+=1
#     elif i==2:
#         _3+=1
#     elif i==3:
#         _4+=1
# print(f"irem {_1} kez")
# print(f"mert {_2} kez")
# print(f"furkan {_3} kez")
# print(f"ibrahim {_4} kez")
# endregion

# region liste secme

# from random import sample, choice ,randrange
# from unittest import result
# oListesi=["irem","mert","furkan","ibrahim"]
# #print(choice(oListesi))
# # print(sample(oListesi, 2))
# result=sample(oListesi, 2)
# print(result)
# print(type(result))
# endregion

# import random as rnd
# z1 = int(input("zar 1 : "))
# z2 = int(input("zar 2 : "))
# sayac = 0
# if 0 < z1 < 7 and 0 < z2 < 7:
#     while True:
#         zar1 = rnd.randint(1, 6)
#         zar2 = rnd.randint(1, 6)
#         sayac += 1
#         if (zar1 == z1 and zar2 == z2) or (zar1 == z2 and zar2 == z1):
#             print(f"{sayac}. seferde bulundu {zar1}-{zar2}")
#             break
# else:
#     print("hatalı giriş")




