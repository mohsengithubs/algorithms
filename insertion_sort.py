from random import shuffle
import matplotlib.pyplot as plt

#این مدل بهینه نیست از نظر حافظه

_list = list(range(1,11))
shuffle(_list)
#print(_list)

lst = []

for i in _list:
    for j in range(len(lst)):
        if i< lst[j]:
            lst.insert(j,i)
            break
    else:
        lst.append(i)

#print(lst)

#یک لیست خالی درست میکنیم و هر ایتم لیست اول را با کل لیست خالی مقایسه میکنیم اگر ایتم بزرگتری پیدا کردیم ایتم لیست اول را جایگذاری میکنیم 
#و بقیه را یک واحد به راست شیفت میکنیم و اگر ایتم بزرگتری پیدا نکردیم ایتم لیست اول را اپند میکنیم


# این مدل از نظر حافظه بهینه است
LENGTH = 50
_list2 = [i for i in range(LENGTH)]
shuffle(_list2)


for i in range(1,LENGTH):
    for j in range(i):
        if _list2[j] > _list2[i]:
            temp = _list2[i]
            del _list2[i]
            _list2.insert(j,temp)
            break
    plt.title("insertion sort")
    plt.bar(range(LENGTH), _list2)
    plt.pause(0.005)
    plt.clf()
plt.bar(range(LENGTH), _list2)
plt.show()

#ما از ایندکس 2 شروع میکنیم و ایندکس های قبلی رو چک میکنیم اکر ایتم بزرگتری پیدا کردیم ایتم ایندکس فعلی را حدف میکنیم 
#و لیست خود به خود به راست شیفت میشه سپس ایتمی که حذف کردیم رو به ایندکس ایتم بزرگتر ایسرت میکنیم