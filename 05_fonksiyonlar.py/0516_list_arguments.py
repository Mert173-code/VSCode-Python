# from unittest import result


# def ortalama(liste):
#     tektoplam = 0
#     tekadet = 0
#     for i in liste:
#             if i % 2 == 1:
#                 tektoplam += i
#                 tekadet += 1
#     return (tektoplam, tekadet)  

# result=ortalama([3,6,5,8,10])
# print(result)
# print(ortalama([3,6,5,8,10]))

#---------------------------------------#

#Epoch Converter

# import time
# cTime= time.time()
# print(cTime)        #1666512953.0028937
# from datetime import datetime
# print(datetime.now())   #2022-10-23 11:15:53.007896
# print(datetime.now().timestamp) #bugünün tarihi/saat epoch


# print(datetime.fromisoformat("2022-10-23").timestamp()) 


#------------------------------------#
import time




from datetime import datetime
def urunKontol(liste):
    for i in liste:
        cTime = datetime.now().timestamp()
        pTime = datetime.fromisoformat(i).timestamp()
        if (cTime-pTime)/86400>60:
            print(i)


urunTarihleri = [
    "2022-08-21",
    "2022-08-22",
    "2022-08-23",
    "2022-08-24",
    "2022-08-25",
    "2022-08-26",
]

urunKontol(urunTarihleri)




