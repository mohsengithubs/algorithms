from random import randint
import matplotlib.pyplot as plt

LENGTH = 10
_list = [randint(0, LENGTH) for i in range(LENGTH)]

for i in range(LENGTH - 1):
    flag = True
    for j in range(LENGTH - i - 1):
        if _list[j] > _list[j + 1]:
            _list[j], _list[j + 1] = _list[j + 1], _list[j]
            flag = False
        plt.title("bubble sort")
        plt.bar(range(LENGTH), _list)
        plt.pause(0.005)
        plt.clf()
    if flag:
        break
plt.bar(range(LENGTH), _list)
plt.show()

# هر خونه رو با خونه بعدش مقایسه میکنه و در هر پیمایش کامل بزرگترین مقدار میره خونه اخر