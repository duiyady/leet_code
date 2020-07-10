# -*- coding:utf-8 -*-
# @Time: 2020-01-30 17:17
# @Author: duiya duiyady@163.com


def longestValidParentheses(s):
    if len(s) < 2:
        return 0
    now = -1
    now2 = -1
    stack = [-1]*len(s)
    stack2_s = [-100]*len(s)
    stack2_e = [-100]*len(s)
    max = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack[now+1] = i
            now += 1
        else:
            if now >= 0:
                if stack2_e[now2] + 1 == stack[now]:
                    stack2_e[now2] = i
                elif stack2_s[now2] > stack[now]:
                    stack2_s[now2] = stack[now]
                    stack2_e[now2] = i
                    if stack2_e[now2-1] + 1 == stack2_s[now2]:
                        now2 -= 1
                        stack2_e[now2] = stack2_e[now2+1]
                else:
                    now2 += 1
                    stack2_s[now2] = stack[now]
                    stack2_e[now2] = i
                max_tmp = stack2_e[now2] - stack2_s[now2] + 1
                if max_tmp > max:
                    max = max_tmp
                now -= 1
    return max


if __name__ == '__main__':
    print(longestValidParentheses("()()()"))