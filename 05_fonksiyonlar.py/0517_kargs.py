# def galeri(kargs):
#     print(kargs)
#     print(type(kargs))


# araba = {
#     "motor": 1.4,
#     "şasiNo": "h11233",
#     "renk": "kırmızı"
# }
# galeri(araba)

#-----------------------------------------#

# def galeri(kargs):
#     print(f'{kargs["motor"]}\t{kargs["sasiNo"]}\t{kargs["renk"]}\t{kargs["marka"]}')


# arabaHyndai = {
#     "motor": 1.4,
#     "sasiNo": "hy11233",
#     "renk": "kırmızı",
#     "marka" : "hyndai"
# }
# arabaHonda = {
#     "motor": 1.8,
#     "sasiNo": "ho1454",
#     "renk": "beyaz",
#     "marka" : "honda"
# }

# print("Motor\tŞasi\tRenk\tMarka")
# print("-----\t-----\t-----\t-----")

# galeri(arabaHyndai)
# galeri(arabaHonda)


#-------------------------------------------------------#


def galeri(kargs):
    # print(f'{kargs["motor"]}\t{kargs["sasiNo"]}\t{kargs["renk"]}\t{kargs["marka"]}')
    print("Motor\tŞasi\tRenk\tMarka")
    print("-----\t-----\t-----\t-----")
    for i in range(len(kargs)):
        print(
            f'{kargs[i]["motor"]}\t{kargs[i]["sasiNo"]}\t{kargs[i]["renk"]}\t{kargs[i]["marka"]}')


# anadolu parsı :)
arabaHyndai = {
    "motor": 1.4,
    "sasiNo": "hy11233",
    "renk": "kırmızı",
    "marka": "hyndai"
}
arabaHonda = {
    "motor": 1.8,
    "sasiNo": "ho1454",
    "renk": "beyaz",
    "marka": "honda"
}
arabalar = [arabaHonda, arabaHyndai]
galeri(arabalar)


# galeri(arabaHyndai)
# galeri(arabaHonda)


def intro(**data):
    print("\nData type of argument:", type(data))

    for key, value in data.items():
        print("{} is {}".format(key, value))


intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com",
      Country="Wakanda", Age=25, Phone=9876543210)
