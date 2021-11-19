import random

ad=""
liste=[]
rand_list=[]
i=0
def toList(ad):
    liste.append(ad)
def my_rand(i):
    rand_list.append(random.randint(0,i))
    res_list=[liste[j] for j in rand_list]
    print(str(res_list))

try:
    while True:
        print("\nÇıkmak için ad kısmına 'çık' yazın")
        ad=input("Ad:")
        if ad=="çık":
            break;
        toList(ad)
        i+=1
except ValueError:
    print("ad string olmalıdır")
finally:
    my_rand(i)
