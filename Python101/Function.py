def prime(variable):
    for i in range(2,variable):
      if (variable % i) == 0:
        print(variable,"asal sayı değildir")
        break
    else:
        print(variable,"asal sayıdır")

def separate(variable):
    print(*variable,sep=' ')


def cikis(menu):
    print("Çıkış yapıldı")
    return "x"

menu=0
variable=0
while menu!="x":
    print("Lütfen bir sayı veya cümle giriniz:")
    variable=input()
    if variable.isdigit():
        prime(int(variable))
    else:
        separate(variable)
    print("Çıkış yapmak istiyor musunuz?(Evet:1 / Hayır:0)")
    menu=int(input())
    if menu==1:
        menu=cikis(menu)
        