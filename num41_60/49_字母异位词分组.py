# -*- coding:utf-8 -*-
# @Time: 2020/7/2 19:18
# @Author: duiya duiyady@163.com


"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
示例:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""


def groupAnagrams(strs):
    result_dict = {}
    for val in strs:
        dict = "".join(sorted(list(val)))
        if dict in result_dict.keys():
            result_dict[dict].append(val)
        else:
            result_dict[dict] = [val]
    result = []
    for k, v in result_dict.items():
        result.append(v)
    return result


if __name__ == '__main__':
    print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))