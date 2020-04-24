# -*- coding: utf-8 -*-


import re
import sys


def valid(arr):
    if len(arr) > 2:
        print('IS NOT VALID ARGUMENT.\n')
        return False

    r = re.compile(r"^[0-9]+$")
    for x in arr:
        if not r.match(x):
            print('{} is not Integer'.format(x))
            return False

    return True


def sum(arr):
    sum_number_1 = arr[0] if len(arr[0]) >= len(arr[1]) else arr[1]
    sum_number_2 = arr[0] if len(arr[0]) < len(arr[1]) else arr[1]

    dic = {
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '0': 0
    }
    result = []
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0

    cnt = len(sum_number_1) - 1
    i = cnt
    while i > -1:
        a = dic[sum_number_1[i]]
        b = i - (len(sum_number_1) - len(sum_number_2))
        c = dic[sum_number_2[b]] if (0 <= b < len(sum_number_2)) else 0
        print(22, '{} {} {}'.format(a, c, e))
        d = a + c + e

        if d >= 10:
            d -= 10
            e = 1
        else:
            e = 0

        i -= 1
        result.append(d)

    if e is 1:
        result.append(e)

    return result


def excute_fun(arr):
    if valid(arr):
        result = sum(arr)
        text = ''
        for i in result:
            text = text + str(i)
        print('{} \n'.format(text))


if __name__ == '__main__':
    excute_fun(sys.argv[1:])
