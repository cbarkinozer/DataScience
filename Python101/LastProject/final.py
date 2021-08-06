def myLoop(sayi):
    for i in range(3):
       if sayi in liste:
           print("Var")
       else:
           print("Yok")
    return
    

liste = []
#77 dersek 77yi almıyor
#bu nedenle 78 dedim
for i in range(1,78, 2):
    liste.append(i)
try:
    sayi=int(input("Sayı giriniz:"))
    myLoop(sayi)
except ValueError:
    print("Hata: Lütfen sadece sayı giriniz!")