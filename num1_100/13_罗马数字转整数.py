"""
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


def romanToInt(s):
    num_char = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    char_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    index = 0
    while index < len(s):
        if index < len(s) - 1 and char_num.get(s[index]) < char_num.get(s[index+1]):
            result = result - char_num.get(s[index])
        else:
            result = result + char_num.get(s[index])
        index = index + 1
    return result

if __name__ == '__main__':
    print(romanToInt('III'))