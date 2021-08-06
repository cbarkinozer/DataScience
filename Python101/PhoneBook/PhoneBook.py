cikis="H"
dosya=open("ogrenci.txt","a+")
while(cikis!="E" and cikis!="e"):
    ad=input("Ad Soyad:")
    no=input("Telefon numarası:")
    dosya.write(ad+"\t"+no+"\n")
    cikis=input("Devam edecek misiniz?(Çıkış:E,Devam:H)")
dosya.close()
dosya=open("ogrenci.txt","r")
oku=dosya.read()
print("Rehberdeki kayıtlar:\n",oku)
dosya.close()