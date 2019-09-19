"""
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
"""


def intToRoman(num):
    num_char = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
    char_num = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    result = []
    while num > 0:
        if num >= 1000:
            result.append(num_char.get(1000))
            num = num - 1000
        elif num >= 900:
            result.append(num_char.get(100))
            result.append(num_char.get(1000))
            num  = num - 900
        elif num >= 500:
            result.append(num_char.get(500))
            num = num - 500
        elif num >= 400:
            result.append(num_char.get(100))
            result.append(num_char.get(500))
            num = num - 400
        elif num >= 100:
            result.append(num_char.get(100))
            num = num - 100
        elif num >= 90:
            result.append(num_char.get(10))
            result.append(num_char.get(100))
            num = num - 90
        elif num >= 50:
            result.append(num_char.get(50))
            num = num - 50
        elif num >= 40:
            result.append(num_char.get(10))
            result.append(num_char.get(50))
            num = num - 40
        elif num >= 10:
            result.append(num_char.get(10))
            num = num - 10
        elif num >= 9:
            result.append(num_char.get(1))
            result.append(num_char.get(10))
            num = num - 9
        elif num >= 5:
            result.append(num_char.get(5))
            num = num - 5
        elif num >= 4:
            result.append(num_char.get(1))
            result.append(num_char.get(5))
            num = num - 4
        else:
            result.append(num_char.get(1))
            num = num - 1
    return ''.join(result)

if __name__ == '__main__':
    print(intToRoman(4))

