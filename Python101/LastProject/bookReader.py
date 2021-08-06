i=1 
# kitap.txt adlı dosyaya erişim sağlanmalıdır.
dosya=open("kitap.txt","a+")
# 3 kez tekrar etmesi sağlanmalıdır.
for i in range(3):
    kitap=input("Kitap Adı:")
    kisi=input("Ödünç alan kişi Adı Soyadı:")
# kitap.txt adlı dosyaya verilerin yazılması sağlanmalıdır.
dosya.write(kitap+kisi)
dosya.close()