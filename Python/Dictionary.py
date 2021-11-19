i=0
ad=""
sozluk={ad:i}
def my_sozluk(ad,i):
    sozluk[ad]=i
def ara(ad):
    print(sozluk.get(ad,"Öğe yok"))
    
    
try:
    print("\n5 kitap ismi girin:")
    while i<5:
        print("\nÇıkmak için ad kısmına 'x' yazın")
        ad=input("Ad:")
        if ad=="x":
            break;
        my_sozluk(ad,i)
        i+=1
except :
    print("Bir hata oluştu")
finally:
    kisi=input("Rehberde arama yapmak için lütfen isim girin:")
    ara(kisi)
