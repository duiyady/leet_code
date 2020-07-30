# -*- coding:utf-8 -*-
# @Time: 2020/7/30 15:55
# @Author: duiya duiyady@163.com


"""
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。

示例:
输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]
"""


def restoreIpAddresses(s):
    s_len = len(s)
    result = []
    l_a, l_b, l_c, l_d = -1, -1, -1, -1
    for i in range(1, min(s_len, 4)):
        a = int(s[:i])
        tt = pow(10, i-1)
        if tt == 1:
            tt = 0
        if a > 255 or a < tt:
            break
        for j in range(i + 1, min(s_len, i + 4)):
            b = int(s[i:j])
            tt = pow(10, j - i - 1)
            if tt == 1:
                tt = 0
            if b > 255 or b < tt:
                break
            for k in range(j + 1, min(s_len, j + 4)):
                c = int(s[j:k])
                tt = pow(10, k - j - 1)
                if tt == 1:
                    tt = 0
                if c > 255 or c < tt:
                    break
                d = int(s[k:])
                tt = pow(10, s_len - k - 1)
                if tt == 1:
                    tt = 0
                if d <= 255 and d >= tt:
                    if not (l_a == a and l_b == b and l_c == c and l_d == d):
                        l_a, l_b, l_c, l_d = a, b, c, d
                        result.append(str(a) + "." + str(b) + "." + str(c) + "." + str(d))

    return result


if __name__ == '__main__':
    print(restoreIpAddresses("101023"))


