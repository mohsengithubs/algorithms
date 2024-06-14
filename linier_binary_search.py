# linier
_list = [4, 2, 8, 4, 7, 54, 2]
target = 7


def linier_search(lst, num):
    for i in lst:
        if num in lst:
            print(f"found {num}")
            break
    else:
        print("not found")


linier_search(_list, target)


# binary
_list2 = [1, 3, 5, 7, 8, 9, 10]
target2 = 10


def binary_search(lst, num):
    if len(lst) < 2:
        if lst[:] == num:
            print(f"found {num}")
        else:
            print("not found")
    else:
        mid = len(lst) // 2
        if lst[mid] == num:
            print(f"found {num}")
        elif num < lst[mid]:
            return binary_search(lst[:mid], num)
        else:
            return binary_search(lst[mid:], num)


binary_search(_list2, target2)
