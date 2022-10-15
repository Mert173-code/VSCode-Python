# isim="ramazan"  #karakter dizisi
# print(isim[0])
"""
trKarakterler="şçğü"
sehir="lüleburgaz"
for i in sehir:
    if i in trKarakterler:
        print("ingilizce klavyesi ile yazamazsın")
        break
else:
    print("sorun yok")
    """    

"""
# PS C:\VSCode-Ecodation-Eylul> pip install keyboard
import keyboard  # using module keyboard
while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('You Pressed A Key!')
            break  # finishing the loop
    except:
        break  # if user pressed a key other than the given key the loop will break

"""


# liste=[i for i in range(1,9)]
# print(liste)
# #aşağı yukarı aynı
# liste=[]
# for i in range(1,9):
#     liste.append(i)
# print(liste)






