# -*- coding:utf-8 -*-
# @Time: 2019-09-15 22:32
# @Author: duiya duiyady@163.com


"""
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
L   C   I   R
E T O E S I I G
E   D   H   N
你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"
"""


def convert(s, numRows):
    if numRows == 1:
        return s
    result = []
    one_line = 2*numRows-2
    i = 0
    while i < len(s):
        result.append(s[i])
        i = i + one_line
    for i in range(1, numRows-1):
        flag = 0  # 0表示单数， 1表示奇数
        j = i
        add_0 = 2 * (numRows - 1 - i)
        add_1 = 2 * i
        while j < len(s):
            result.append(s[j])
            if flag == 0:
                j = j + add_0
                flag = 1
            else:
                j = j + add_1
                flag = 0
    i = numRows-1
    while i < len(s):
        result.append(s[i])
        i = i + one_line
    return ''.join(result)


if __name__ == '__main__':
    print(convert('"PAYPALISHIRIdasfgaNG',5))
