# -*- coding:utf-8 -*-
# @Time: 2020/6/30 8:14
# @Author: duiya duiyady@163.com

"""
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，
分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )
输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]
"""

class CQueue:
    def __init__(self):
        self.stack1 = []  # 主
        self.stack2 = []

    def appendTail(self, value: int):
        self.stack1.append(value)


    def deleteHead(self) -> int:
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
        if len(self.stack2) == 0:
            return -1
        else:
            return self.stack2.pop()

