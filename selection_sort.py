from random import randint
import matplotlib.pyplot as plt

LENGTH = 100
_list = [randint(0, LENGTH) for i in range(LENGTH)]

for i in range(LENGTH - 1):
    _min = i
    for j in range(i + 1, LENGTH):
        if _list[_min] > _list[j]:
            _min = j
    _list[i], _list[_min] = _list[_min], _list[i]
    plt.title("selection sort")
    plt.bar(range(LENGTH), _list)
    plt.pause(0.005)
    plt.clf()
plt.bar(range(LENGTH), _list)
plt.show()

# از خونه اول شروع میکنه کل لیست رو پیمایش میکنه و کمترین مقدار رو میزاره تو خونه اول