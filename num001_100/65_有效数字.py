# -*- coding:utf-8 -*-
# @Time: 2020/7/11 15:34
# @Author: duiya duiyady@163.com


"""
验证给定的字符串是否可以解释为十进制数字。
例如:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false
"""


def isNumber(s):
    s = s.strip()
    if len(s) == 0:
        return False
    if s[0] == "+" or s[0] == "-":
        s = s[1:]
    if len(s) == 1 and s[0] in ["+", "-", ".", "e"]:
        return False
    po = False
    e = False
    z_f = False
    nums = False
    for i in range(len(s)):
        if s[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            nums = True
        elif s[i] in ["+", "-"]:
            if z_f is True or i == 0 or i == len(s)-1:
                return False
            if s[i+1] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] or s[i-1] != "e":
                return False
            e = True
        elif s[i] == ".":
            if po is True or e is True:
                return False
            if i != len(s)-1:
                if s[i + 1] == "e" and nums is False:
                    return False
                if s[i+1] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "e"]:
                    return False
            po = True
        elif s[i] == "e":
            if i == 0 or e is True or i == len(s)-1:
                return False
            elif s[i+1] not in ["+", "-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                return False
            e = True
        else:
            return False
    return True

if __name__ == '__main__':
    print(isNumber("1.e1"))