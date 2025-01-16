from random import randint


SMALL_ARRAY_LEN = 32


def insertion_sort(array: list[int], left: int=0, right: int | None=None) -> list[int]:
    if right is None:
        right = len(array) - 1
    for i in range(left + 1, right + 1):
        temp = array[i]
        j = i - 1
        while j >= left and temp < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = temp
    return array


def partition(array: list[int], left: int=0, right: int | None=None) -> int:
    if right is None:
        right = len(array) - 1
        
    med = (left + right) // 2
    if right - left >= 2:
        tmp_arr = insertion_sort([array[left], array[med], array[right]])
        array[left], array[med], array[right] = tmp_arr
    
    i, j = left, right
    pivot = array[med]
    
    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i >= j:
            break
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1
    return j


def quick_sort(array: list[int], left: int=0, right: int | None=None) -> None:
    if right is None:
        right = len(array) - 1
    if right - left + 1 <= SMALL_ARRAY_LEN:
        insertion_sort(array, left, right)
        return
    if left < right:
        q = partition(array, left, right)
        quick_sort(array, left, q)
        quick_sort(array, q + 1, right)


if __name__ == '__main__':
    # тест быстрой сортировки

    lists = [[], [1]]
    for _ in range(1000): # генерация 1000 случайных списков
        arr_len = randint(1, 500)
        lists.append([randint(-1000, 1000) for _ in range(arr_len)])
    
    ok = True
    for i, l in enumerate(lists):
        quick_sort(l)
        if not l == sorted(l):
            print(i)
            ok = False
    print('OK' if ok else 'FAIL')
