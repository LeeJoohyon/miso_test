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
                c = c + (a * b)
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
    # 만 단위 자릿수
    ten_thousand_pos = 4
    # 억 단위 자릿수
    hundred_million_pos = 9
    # 조 단위 자릿수
    hundred_billion_pos = 13
    # 경 단위 자릿수
    hundred_trillion_pos = 17

    txt_digit = ['', '십', '백', '천', '만', '억', '조', '경']
    txt_number = ['', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    result_str = ''
    digit_count = 0
    # 자릿수 카운트

    digit_count = len(str(num))
    index = 0
    num = str(num)
    while True:
        not_show_digit = False
        ch = num[index]
        ch = int(ch)
        # 자릿수가 2자리이고 1이면 '일'은 표시 안함.
        # 단 '만' '억'에서는 표시 함
        if (digit_count > 1) and (digit_count != ten_thousand_pos) and (digit_count != hundred_million_pos) and int(
                ch) == 1:
            result_str = result_str + ''
        elif int(ch) == 0:
            result_str = result_str + ''
            # 단 '만' '억'에서는 표시 함
            if (digit_count != ten_thousand_pos) and (digit_count != hundred_million_pos):
                not_show_digit = True
        else:
            result_str = result_str + txt_number[int(ch)]

        # 1경 이상
        if digit_count > hundred_trillion_pos:
            if not not_show_digit:
                result_str = result_str + txt_digit[digit_count - hundred_trillion_pos]

        # 1조 이상
        if digit_count > hundred_billion_pos:
            if not not_show_digit:
                result_str = result_str + txt_digit[digit_count - hundred_billion_pos]

        # 1억 이상
        if digit_count > hundred_million_pos:
            if not not_show_digit:
                result_str = result_str + txt_digit[digit_count - hundred_million_pos]
        # 1만 이상
        elif digit_count > ten_thousand_pos:
            if not not_show_digit:
                result_str = result_str + txt_digit[digit_count - ten_thousand_pos]
        else:
            if not not_show_digit:
                result_str = result_str + txt_digit[digit_count]

        if digit_count <= 0:
            digit_count = 0
        else:
            digit_count = digit_count - 1
        index = index + 1
        if index >= len(num):
            break

    return result_str


if __name__ == '__main__':
    data = [
        ['오백삼십조칠천팔백구십만천오백삼십구', '삼조사천이만삼천구'],
        ['육십사억삼천십팔만칠천육백구', '사십삼'],
        ['구백육십조칠천억팔천백삼십이만칠천일', '사십삼조오천이백억육천구백십만일'],
        ['이천구백육십조천오백칠십만삼천구백구십', '삼천사백오십조일억이천만육백사십삼'],
        ['사십오억삼천육십만오백구십', '칠십억천이백삼십오만칠천구십이'],
        ['천백십일', '구천오백구십구'],
        ['오억사천', '백십일'],
        ['만오천사백삼십', '십구만삼천오백'],
        ['일조', '삼'],
        ['일억', '만']
    ]
    for i in data:
        num1 = convert_str_to_num(i[0])
        num2 = convert_str_to_num(i[1])
        num_res = num1 + num2
        print(num_res)
        result = convert_num_to_str(num_res)
        print("result : {} ".format(result))
