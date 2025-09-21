import random

print("""
Bilgisayara karşı taş kağıt makas oyunu
Taş için 'T' Makas için 'M' Kağıt için 'K' tuşuna basın .Oyunu bitirmek için boşluğa basın veya 'exit' girin
""")
liste=["T","K","M"]
bilgisayar=0
oyuncu=0
while True:

    deger = input("T,K,M:")
    var =random.choice(liste)
    if deger=="exit" or "":
        print("Sonuç:Oyuncu:{},Bilgisayar:{}".format(oyuncu,bilgisayar))
        break
    elif deger == "T":
        if var =="T":
            print("Berabere")
        elif var =="K":
            bilgisayar+=1
            print("Kağıt . Bilgisayar yendi.Skor:{}-{}".format(oyuncu,bilgisayar))
        elif var =="M":
            oyuncu+=1
            print("Makas .  Oyuncu yendi.Skor:{}-{}".format(oyuncu, bilgisayar))
    elif deger == "M":
        if var =="M":
            print("Makas .Berabere")
        elif var =="K":
            oyuncu+=1
            print("Kağıt . Oyuncu yendi.Skor:{}-{}".format(oyuncu,bilgisayar))
        elif var =="T":
            bilgisayar+=1
            print("Taş . Bilgisayar yendi.Skor:{}-{}".format(oyuncu, bilgisayar))
    elif deger == "K":
        if var =="K":
            print("Kağıt.Berabere")
        elif var =="T":
            oyuncu+=1
            print("Taş . Oyuncu yendi.Skor:{}-{}".format(oyuncu,bilgisayar))
        elif var =="M":
            bilgisayar+=1
            print("Makas . Bilgisayar yendi.Skor:{}-{}".format(oyuncu, bilgisayar))
    else:
        print("Geçerli değer gir.")
