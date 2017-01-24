from copy import deepcopy

############ recursive function ################
def QuickSort(array, *, reversed=False, key=lambda x: x):
    """
        Sort an array using Quick Sort
        :param array: Array to be sorted
        :param key: Sort after a key, default is the element of array
        :param reversed: Sort in reversed order, default is ascending order
        :return: Array sorted
    """
    less = []
    equal = []
    greater = []
    array = deepcopy(array)

    if len(array) > 1:
        pivot = key(array[len(array) // 2])
        for x in array:
            if key(x) < pivot:
                less.append(x)
            elif key(x) > pivot:
                greater.append(x)
            else:
                equal.append(x)
        less = QuickSort(less, reversed=reversed, key=key)
        greater = QuickSort(greater,reversed=reversed, key=key)
        return less + equal + greater if not reversed else greater + equal + less
    else:
        return array


def GnomeSort(array, *, reversed=False, key=lambda x:x):
    """
        Sort an array using Gnome Sort (Stupid sort)
        :param array: Array to be sorted
        :param key: Sort after a key, default is the element of array
        :param reversed: Sort in reversed order, default is ascending order
        :return: Array sorted
    """
    array = deepcopy(array)
    pos = 0
    while pos < len(array):
        if not reversed and (pos == 0 or key(array[pos]) >= key(array[pos - 1])):
            pos += 1
        elif reversed and (pos == 0 or key(array[pos]) <= key(array[pos - 1])):
            pos += 1
        else:
            array[pos], array[pos - 1] = array[pos - 1], array[pos]
            pos -= 1
    return array
