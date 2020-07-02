# -*- coding:utf-8 -*-
# @Time: 2020/6/29 18:32
# @Author: duiya duiyady@163.com


"""
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。
说明:
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
"""


def isMatch(s, p):
    s, p = list(s), list(p)
    now_max = [len(s)]*len(p)  # 当前这个位置能最大填的值
    now_p = 0  # 当前在匹配串的哪个位置
    i = 0  # 当前遍历到哪里
    flag = True
    while flag:
        if i == -1:
            if p[0] == "*" or p[0] == "?":
                now_max.pop(0)
                p.pop(0)
                i = 0
            else:
                return False
        elif now_p == len(p):
            if i == len(s):
                return True
            else:
                now_p -= 1
                i = now_max[now_p] - 1
        elif i == len(s):
            if now_p == len(p)-1 and p[now_p] == "*":
                return True
            now_max[now_p] = i-1
            now_p -= 1
            i = now_max[now_p] - 1
        elif p[now_p] == "*":
            # 如果*是在最后一个，肯定匹配了
            if now_p == len(p) - 1:
                return True
            # 还没有到当前这个匹配点能到的最大位置
            if (i+1) < now_max[now_p]:
                i += 1
            else:
                now_max[now_p] = i
                now_p += 1
        elif p[now_p] == "?":
            if i < len(s):
                if i < now_max[now_p]:
                    now_max[now_p] = i
                    now_p += 1
                else:
                    now_max[now_p] = i
                    i += 1
                    now_p += 1
            else:
                now_p -= 1
                i = now_max[now_p] - 1
        else:
            if p[now_p] == s[i]:
                now_max[now_p] = i
                i += 1
                now_p += 1
            else:
                now_p -= 1
                i = now_max[now_p] - 1




if __name__ == '__main__':
    print(isMatch(s="acdcb",p="a*c?b"))