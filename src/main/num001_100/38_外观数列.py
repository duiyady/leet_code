# -*- coding:utf-8 -*-
# @Time: 2020/6/27 9:14 上午
# @Author: duiya duiyady@163.com


def countAndSay(n):
    array = ["1"]
    for i in range(1, n):
        last = None
        count = 0
        array_tmp = []
        for index in range(len(array)):
            if last is None:
                last = array[index]
                count += 1
            elif last == array[index]:
                count += 1
            elif last != array[index]:
                array_tmp.append(str(count))
                array_tmp.append(last)
                last = array[index]
                count = 1
        array_tmp.append(str(count))
        array_tmp.append(last)
        array = array_tmp
        array_tmp = []
    return "".join(array)

if __name__ == '__main__':
    print(countAndSay(5))

