# -*- coding:utf-8 -*-
# @Time: 2020/7/11 20:20
# @Author: duiya duiyady@163.com


"""
给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。
你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。
要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。
文本的最后一行应为左对齐，且单词之间不插入额外的空格。
说明:
单词是指由非空格字符组成的字符序列。
每个单词的长度大于 0，小于等于 maxWidth。
输入单词数组 words 至少包含一个单词。
示例:
输入:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
输出:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
"""


def fullJustify(words, maxWidth):
    start = 0
    result = []
    count = len(words[0])
    for i in range(1, len(words)):
        if count + 1 + len(words[i]) <= maxWidth:
            count += (1 + len(words[i]))
        else:
            word_count = i-start
            tmp_result = [words[start], ]
            if word_count == 1:
                tmp_result.append(" "*(maxWidth-count))
            else:
                keyboard = maxWidth - count
                all_key = keyboard // (word_count-1)
                pre_key = keyboard % (word_count-1)
                for j in range(word_count-1):
                    if j < pre_key:
                        tmp_result.append(" "*(2 + all_key))
                    else:
                        tmp_result.append(" "*(1 + all_key))
                    tmp_result.append(words[start + j + 1])
            result.append("".join(tmp_result))
            start = i
            count = len(words[i])

    word_count = len(words) - start
    tmp_result = [words[start], ]
    for j in range(word_count - 1):
        tmp_result.append(" ")
        tmp_result.append(words[start + j + 1])
    tmp_result.append(" "*(maxWidth - count))
    result.append("".join(tmp_result))

    return result

if __name__ == '__main__':
    print(fullJustify(words=["This", "is", "an", "example", "of", "text", "justification."], maxWidth=16))