from typing import List, Any


def permute(arr: List[Any]) -> List[List[Any]]:
    permutations = [arr, ]
    arr_length = len(arr)
    tmp_arr = [0] * arr_length
    i = 1
    while i < arr_length:
        if tmp_arr[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[tmp_arr[i]], arr[i] = arr[i], arr[tmp_arr[i]]
            permutations.append(arr)
            arr = arr[:]
            tmp_arr[i] += 1
            i = 0
        else:
            tmp_arr[i] = 0
            i += 1
    return permutations


# print(permute([1, 2, 3, 12, 123]))


# test permute
def test_permute():
    assert permute([1]) == [[1]]
    assert permute(['a']) == [['a']]
    assert permute([1, 2, 3, 12, 123]) == [[2, 1, 3, 12, 123], [2, 1, 3, 12, 123], [3, 1, 2, 12, 123],
                                           [1, 3, 2, 12, 123], [2, 3, 1, 12, 123], [3, 2, 1, 12, 123],
                                           [12, 2, 1, 3, 123], [2, 12, 1, 3, 123], [1, 12, 2, 3, 123],
                                           [12, 1, 2, 3, 123], [2, 1, 12, 3, 123], [1, 2, 12, 3, 123],
                                           [1, 3, 12, 2, 123], [3, 1, 12, 2, 123], [12, 1, 3, 2, 123],
                                           [1, 12, 3, 2, 123], [3, 12, 1, 2, 123], [12, 3, 1, 2, 123],
                                           [12, 3, 2, 1, 123], [3, 12, 2, 1, 123], [2, 12, 3, 1, 123],
                                           [12, 2, 3, 1, 123], [3, 2, 12, 1, 123], [2, 3, 12, 1, 123],
                                           [123, 3, 12, 1, 2], [3, 123, 12, 1, 2], [12, 123, 3, 1, 2],
                                           [123, 12, 3, 1, 2], [3, 12, 123, 1, 2], [12, 3, 123, 1, 2],
                                           [1, 3, 123, 12, 2], [3, 1, 123, 12, 2], [123, 1, 3, 12, 2],
                                           [1, 123, 3, 12, 2], [3, 123, 1, 12, 2], [123, 3, 1, 12, 2],
                                           [123, 12, 1, 3, 2], [12, 123, 1, 3, 2], [1, 123, 12, 3, 2],
                                           [123, 1, 12, 3, 2], [12, 1, 123, 3, 2], [1, 12, 123, 3, 2],
                                           [1, 12, 3, 123, 2], [12, 1, 3, 123, 2], [3, 1, 12, 123, 2],
                                           [1, 3, 12, 123, 2], [12, 3, 1, 123, 2], [3, 12, 1, 123, 2],
                                           [2, 12, 1, 123, 3], [12, 2, 1, 123, 3], [1, 2, 12, 123, 3],
                                           [2, 1, 12, 123, 3], [12, 1, 2, 123, 3], [1, 12, 2, 123, 3],
                                           [123, 12, 2, 1, 3], [12, 123, 2, 1, 3], [2, 123, 12, 1, 3],
                                           [123, 2, 12, 1, 3], [12, 2, 123, 1, 3], [2, 12, 123, 1, 3],
                                           [2, 1, 123, 12, 3], [1, 2, 123, 12, 3], [123, 2, 1, 12, 3],
                                           [2, 123, 1, 12, 3], [1, 123, 2, 12, 3], [123, 1, 2, 12, 3],
                                           [123, 1, 12, 2, 3], [1, 123, 12, 2, 3], [12, 123, 1, 2, 3],
                                           [123, 12, 1, 2, 3], [1, 12, 123, 2, 3], [12, 1, 123, 2, 3],
                                           [3, 1, 123, 2, 12], [1, 3, 123, 2, 12], [123, 3, 1, 2, 12],
                                           [3, 123, 1, 2, 12], [1, 123, 3, 2, 12], [123, 1, 3, 2, 12],
                                           [2, 1, 3, 123, 12], [1, 2, 3, 123, 12], [3, 2, 1, 123, 12],
                                           [2, 3, 1, 123, 12], [1, 3, 2, 123, 12], [3, 1, 2, 123, 12],
                                           [3, 123, 2, 1, 12], [123, 3, 2, 1, 12], [2, 3, 123, 1, 12],
                                           [3, 2, 123, 1, 12], [123, 2, 3, 1, 12], [2, 123, 3, 1, 12],
                                           [2, 123, 1, 3, 12], [123, 2, 1, 3, 12], [1, 2, 123, 3, 12],
                                           [2, 1, 123, 3, 12], [123, 1, 2, 3, 12], [1, 123, 2, 3, 12],
                                           [12, 123, 2, 3, 1], [123, 12, 2, 3, 1], [2, 12, 123, 3, 1],
                                           [12, 2, 123, 3, 1], [123, 2, 12, 3, 1], [2, 123, 12, 3, 1],
                                           [3, 123, 12, 2, 1], [123, 3, 12, 2, 1], [12, 3, 123, 2, 1],
                                           [3, 12, 123, 2, 1], [123, 12, 3, 2, 1], [12, 123, 3, 2, 1],
                                           [12, 2, 3, 123, 1], [2, 12, 3, 123, 1], [3, 12, 2, 123, 1],
                                           [12, 3, 2, 123, 1], [2, 3, 12, 123, 1], [3, 2, 12, 123, 1],
                                           [3, 2, 123, 12, 1], [2, 3, 123, 12, 1], [123, 3, 2, 12, 1],
                                           [3, 123, 2, 12, 1], [2, 123, 3, 12, 1], [123, 2, 3, 12, 1]]
