from random import randint
import matplotlib.pyplot as plt


length = 100
_list = [randint(0, length) for i in range(length)]


def qsort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst.pop()
    rigth = []
    left = []
    for i in lst:
        if i < pivot:
            left.append(i)
        else:
            rigth.append(i)
    
    return qsort(left) + [pivot] + qsort(rigth)


plt.bar(range(length),_list)
plt.pause(0.005)
plt.clf()

sorted_list = qsort(_list)
plt.bar(range(length),sorted_list)
plt.show()
