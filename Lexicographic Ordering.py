"""Algorithm Phases:

1_Find the largest x such that p[x] < p[x+1].
 (If no such x exists, the permutation is the last permutation.) -> break statement
2_Find the largest y such that p[x] < p[y].
3_Swap p[x] and p[y].
4_Reverse P[x+1 .. n].
5_Loop untill break statement reaches."""


# step 3 (swap)
def swap(_list, index_i, index_j):
    _list[index_i], _list[index_j] = _list[index_j], _list[index_i]
    return _list


items = [1, 2, 3, 4, 5]
print(items)

while True:
    # step 1
    largest_x = -1
    for i in range(len(items) - 1):
        if items[i] < items[i + 1]:
            largest_x = i
    if largest_x == -1:
        break

    # step 2
    largest_y = -1
    for y in range(len(items)):
        if items[largest_x] < items[y]:
            largest_y = y

    # step 3
    items = swap(items, largest_x, largest_y)

    # step 4
    left_side = items[:largest_x+1]
    right_side = items[largest_x+1:]
    right_side.reverse()
    items = left_side + right_side

    print(items)


