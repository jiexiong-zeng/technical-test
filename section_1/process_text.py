def numeric_to_text(num):
    res = []
    suffix = 0
    numeric_dic = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
        100: "hundred",
        1000: "thousand"
    }
    if num == 0:
        return numeric_dic[0]

    if num >= 1000:
        prefix = num//1000
        suffix = 1000
        res.append(numeric_to_text(prefix) + " " + numeric_dic[suffix])
        num -= prefix*suffix
    if num >= 100: 
        prefix = num//100
        suffix = 100
        res.append(numeric_dic[prefix] + " " + numeric_dic[suffix])
        num -= prefix*suffix
    #special cases
    if num < 20 and num > 10:
        res.append(numeric_dic[num])
        num -= num
    if num >= 10: 
        prefix = num//10
        suffix = 10
        res.append(numeric_dic[prefix*10])
        num -= prefix*suffix
    if num > 0:
        prefix = num
        #combine
        if suffix == 10:
            res[-1] = res[-1] + "-" + numeric_dic[prefix]
        else:
            res.append(numeric_dic[prefix])

    #return string
    str_output = ""
    for i in range(len(res)):
        if i == 0:
            str_output = res[i]
        elif i == len(res)-1 and len(res) > 1:
            str_output = str_output + " and " + res[i]
        else:
            str_output = str_output + ", " + res[i]
    return str_output


def process_text(sentence):
    res = ""
    start = -1
    for i in range(len(sentence)):
        if sentence[i].isdigit():
            if start == -1:
                start = i
        else:
            if start != -1:
                res = res + numeric_to_text(int(sentence[start:i]))
                start = -1
            res = res + sentence[i]
        
    # account for ending on digit
    if start != -1:
        res = res + numeric_to_text(int(sentence[start:len(sentence)]))

    return res

print(process_text('what is 20 + 232'))

