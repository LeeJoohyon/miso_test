# -*- coding: utf-8 -*-
def convert_str_to_num(arg):
    string_num = {
        '일': 1,
        '이': 2,
        '삼': 3,
        '사': 4,
        '오': 5,
        '육': 6,
        '칠': 7,
        '팔': 8,
        '구': 9
    }

    string_amount = {
        '십': 10,
        '백': 100,
        '천': 1000,
    }

    string_keys_amount = {
        '만': 10000,
        '억': 100000000,
        '조': 1000000000000,
        '경': 10000000000000000
    }

    num_list = []
    a = 1
    b = 0
    c = 0

    for i in range(0, len(arg)):
        d = arg[i]
        if d in string_num.keys():
            a = string_num[d]
        elif d in string_amount.keys():
            b = string_amount[d]
            if a is not 0:
                c = a * b
            a = 0
        elif d in string_keys_amount.keys():
            c = (c + a) * string_keys_amount[d] if a is not 0 else c * string_keys_amount[d]
            num_list.append(c)
            a = 0
            c = 0
            a = 0
    if c:
        c = c + a if a is not 0 else c
        num_list.append(c)
    elif a:
        num_list.append(a)

    return sum(num_list)

def convert_num_to_str(num):
    def check_num(n):
        string_num = {
            '일': 1,
            '이': 2,
            '삼': 3,
            '사': 4,
            '오': 5,
            '육': 6,
            '칠': 7,
            '팔': 8,
            '구': 9
        }
        convert_list = n.split('')
        string_amount = {
            '십': 10,
            '백': 100,
            '천': 1000,
        }
        for i in convert_list:
            if i is 0:
                return
            else:

    num_list = []
    while num > 0:
        num_list.append()

if __name__ == '__main__':
    print(convert_str_to_num('오조삼천억이천만'))
