# -*- coding:utf-8 -*-
# @Time: 2020/7/8 9:52
# @Author: duiya duiyady@163.com


"""
你正在使用一堆木板建造跳水板。有两种类型的木板，其中长度较短的木板长度为shorter，长度较长的木板长度为longer。你必须正好使用k块木板。
编写一个方法，生成跳水板所有可能的长度。
返回的长度需要从小到大排列
"""


def divingBoard(shorter, longer, k):
    if k == 0:
        return []
    result = []
    tmp = shorter * k
    result.append(tmp)
    tmp2 = longer - shorter
    if tmp2 == 0:
        return result
    for i in range(1, k + 1):
        tmp += tmp2
        result.append(tmp)
    return result


if __name__ == '__main__':
    print(divingBoard(1, 4, 5))