def myLoop():
    print("3 hakkınız var.")
    for i in range(3):
       sayi2=int(input("Lütfen verilen aralıktan bir sayi giriniz(1-100):"))
       if sayi2<1 or sayi2>100:
           raise Exception("Belirtilen aralıkta değer girin.")
       if sayi1==sayi2:
           print("\nTebrikler! Bildiniz.")
           return
       elif sayi1!=sayi2:
           print("\nBilemediniz. Kalan hak sayısı:",2-i,)
    
sayi1=50
sayi2=0
try:
    myLoop()
except ValueError:
    print("Hata: Lütfen sadece sayı giriniz!")
except Exception as sinirHata:
    print("Hata:",sinirHata)
finally:
    print("Oyun bitti, oynadığınız için teşekkürler")