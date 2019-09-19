"""
编写一个函数来查找字符串数组中的最长公共前缀。如果不存在公共前缀，返回空字符串 ""。
输入: ["flower","flow","flight"]
输出: "fl"
"""
def longestCommonPrefix(strs):
    result = []
    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]
    for i in range(len(strs[0])):  # 一个单词有多长
        flag = 1
        for j in range(len(strs) - 1):  # 列表有多少个单词
            try:
                if strs[j][i] != strs[j+1][i]:
                    flag = 0
            except IndexError as e:
                flag = 0
            if flag == 0:
                break
        if flag == 0:
            break
        else:
            result.append(strs[0][i])
    return ''.join(result)


if __name__ == '__main__':
    print(longestCommonPrefix( ["flower","flow","flight"]))
