# -*- coding:utf-8 -*-
# @Time: 2020/7/15 21:40
# @Author: duiya duiyady@163.com


"""
以 Unix 风格给出一个文件的绝对路径，你需要简化它。或者换句话说，将其转换为规范路径。
在 Unix 风格的文件系统中，一个点（.）表示当前目录本身；此外，两个点 （..） 表示将目录切换到上一级（指向父目录）；两者都可以是复杂相对路径的组成部分。更多信息请参阅：Linux / Unix中的绝对路径 vs 相对路径
请注意，返回的规范路径必须始终以斜杠 / 开头，并且两个目录名之间必须只有一个斜杠 /。最后一个目录名（如果存在）不能以 / 结尾。此外，规范路径必须是表示绝对路径的最短字符串。
示例 1：
输入："/home/"
输出："/home"
解释：注意，最后一个目录名后面没有斜杠。
示例 2：
输入："/../"
输出："/"
解释：从根目录向上一级是不可行的，因为根是你可以到达的最高级。
"""


def simplifyPath(path):
    result = []
    start = 0
    for i in range(len(path)):
        if path[i] == "/":
            if i != start:
                ttt = path[start:i]
                if ttt == ".":
                    pass
                elif ttt == "..":
                    if len(result) > 0:
                        result.pop()
                else:
                    result.append(ttt)
            start = i+1
    if start != len(path):
        ttt = path[start:]
        if ttt == ".":
            pass
        elif ttt == "..":
            if len(result) > 0:
                result.pop()
        else:
            result.append(ttt)
    str = []
    if len(result) == 0:
        str.append("/")
    else:
        for va in result:
            str.append("/")
            str.append(va)
    return "".join(str)



if __name__ == '__main__':
    print(simplifyPath("/a//b////c/d//././/.."))
    print(simplifyPath("/home/foo/./.././bar"))
    print(simplifyPath("/..."))



