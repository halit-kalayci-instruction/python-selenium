from human import Human
import matematik as math

math.bol(20,2)

faiz = 1.59
vade = "36"
krediAdi = "İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))


print(int(vade)+12)
#print(int(krediAdi))
faiz = str(faiz)
print(type(faiz))

vade = 36 #int(input("Lütfen istediğiniz vade sayısını giriniz: "))
print(type(vade))
vade = vade + 12

# string interpolation
# Seçtiğiniz vade sonucu ortaya çıkan vade: 
print("Seçtiğiniz vade sonucu ortaya çıkan vade: " + str(vade))
print("Seçtiğiniz vade sonucu ortaya çıkan vade: {vadeSayisi}".format(vadeSayisi=vade))
print(f"Seçtiğiniz vade sonucu ortaya çıkan vade: {vade}")

isim = "halit" #input("İsminizi giriniz")
metin = "Merhaba {name}".format(name=123)
print(metin)


# f-string
metin = f"Hoşgeldiniz {1+1}"
print(metin)


# listeler
# döngüler
# fonksiyonlar

dizi = ["İhtiyaç Kredisi", 10, 5.2, True]
print(dizi)

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
print(type(krediler))

print(krediler[0])

print(len(krediler))  #length
# print(krediler[3]) => hata verir

krediler.append("Özel Kredi")
print(krediler)

krediler.append("X Kredisi")
print(krediler)

krediler.pop(0)
print(krediler)

krediler.append("Taşıt Kredisi")
print(krediler)


krediler.remove("Taşıt Kredisi")
print(krediler)

krediler.extend(["Y Kredisi","Z Kredisi"])
print(krediler)

# for
# i=0 i<10 
x=10
for i in range(x):
    print("xx")
    print(i)
print("***************")

for i in range(5,11):
    print(i)

print("*************")
for i in range(0,51,10):
    print(i)
print("****************")
# for i in range(0.1,0.5):
#     print(i)
krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
for kredi in krediler:
    print(kredi)
print("*************")
for i in range(len(krediler)):
    print(krediler[i])
print("**************")


# sonsuz döngü
i = 0
while i < 10:
    print("x")
    i += 1
print("y")

print("***********")


while True:
    print("X")
    break

print("**** Son Döngü *****")

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
i = 0
while i < len(krediler):
    i+=1
    print(i)
    print(krediler[i])
    if krediler[i] == "Konut Kredisi":
        break

# fonksiyonlar

fiyat = 100
indirim = 20
#definition define
def calculate():
    print(100-20)

def calculateWithParams(fiyat,indirim):
    print(fiyat-indirim)

def sayHello(name):
    print(f"Merhaba {name}")


calculate()
calculateWithParams(50,10)
calculateWithParams(100,30)
sayHello("Halit")
sayHello("Arif")
sayHello("Mevlüt")


def calculateAndReturn(fiyat,indirim):
    return fiyat-indirim

yeniFiyat = calculateAndReturn(200,50)
print(yeniFiyat + 10)

#void
def calculatePrice(price, discount):
    print(price-discount)

def calculatePriceAndReturn(price, discount):
    return price-discount

print("************")
# fonk1 = calculatePrice(100,50)
fonk2 = calculatePriceAndReturn(300,100)
# print(f"159.satır: {fonk1+100}")
print(f"160.satır: {fonk2+100}")
print("**************")


# sınıflar => classlar
# modules
# paket yönetimi
# self => this


# instance => örnek
human1 = Human("Enes")
human1.talk("Merhaba")
human1.walk()
print(human1)


human2 = Human("Halit")
human2.talk("Selam")
human2.walk()
print(human2)

Human("Melike").talk("Merhaba")
