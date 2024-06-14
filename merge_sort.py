from random import shuffle


# ما در اینجا دوتا لیست مرتب داریم و میخوایم ادغام کنیم
# ایتم های اول را با هم مقایسه و کوچکتر را به لیست سوم انتقال میدیم
# در لیستی که کوچکتر بود یه خونه به جلو میرویم, در اخر اگر لیستی تمام شد باقی مانده لیست دیگر را انتقال میدهیم


def loop_over(lst1, lst2):
    len1 = len(lst1)
    len2 = len(lst2)
    lst3 = []
    i = j = 0

    while i < len1 and j < len2:
        if lst1[i] < lst2[j]:
            lst3.append(lst1[i])
            i += 1
        else:
            lst3.append(lst2[j])
            j += 1

    lst3 += lst1[i:]
    lst3 += lst2[j:]

    return lst3


# در اینجا ما لیست را به لیست های یک عنصر تبدیل میکنیم و عنصر ها را به لوپ اور میدهیم
# از انجا که یک لیست تک عنصر مرتب است انها را با هم مقایسه و مرتب میکند و به عنوان یک لیست کامل برمیگرداند

def merge(lst):
    if len(lst) == 1:
        return lst
    else:
        mid = len(lst) // 2
        right = lst[:mid]
        left = lst[mid:]

    left = merge(left)
    right = merge(right)

    return loop_over(left, right)


length = 10
_list = [i for i in range(length)]
shuffle(_list)

print(_list)
print(merge(_list))
