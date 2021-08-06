cikis="a"
while(cikis!="x"):
    print("Lütfen 1-100 arası bir sayı giriniz:")
    girdi = int(input())
    while(girdi>100 or girdi<1 ):    
        print("Lütfen sayınız 1'den büyük 100'den küçük olsun")
        girdi= int(input())
    for x in range(girdi,101):
        if(x%2==0): 
           print(x)
    print("Çıkmak ister misiniz?(Çıkış için x'e basın)")
    cikis=input()
print("Çıkış yapıldı")    
