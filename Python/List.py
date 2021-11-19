ad=""
soyad=""
kurum=""
siparis=0
liste=[]
def toList(ad,soyad,kurum,siparis):
    
    liste.append(ad)
    liste.append(soyad)
    liste.append(kurum)
    liste.append(siparis)



try:
    while True:
        print("\nÇıkmak için ad kısmına 'çık' yazın")
        ad=input("Ad:")
        if ad=="çık":
            break;
        soyad=input("soyad:")
        kurum=input("kurum:")
        siparis=int(input("siparis:"))
        toList(ad,soyad,kurum,siparis)
except ValueError:
    print("ad,soyad,kurum,siparis sırası ile str,str,str,int olmalıdır")
finally:
    for i in liste:
        print(i)
        if type(i)== int:
            print("--------------")
