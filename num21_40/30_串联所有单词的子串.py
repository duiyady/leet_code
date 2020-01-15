"""
给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。
"""

def findSubstring(s, words):
    result = []
    if not s or not words:
        return result
    n_words = len(words)
    n_word = len(words[0])
    n_s = len(s)
    if n_s < n_word*n_words:
        return result
    from collections import Counter
    words = Counter(words)
    for i in range(n_s - n_words*n_word + 1):
        words_dict = words.copy()
        flag = True
        for j in range(n_words):
            tmp_s = s[i+j*n_word: i + (j+1)*n_word]
            if words_dict.get(tmp_s) is not None and words_dict.get(tmp_s) > 0:
                words_dict[tmp_s] = words_dict.get(tmp_s) - 1
            else:
                flag = False
                break
        if flag is True:
            result.append(i)
    return result



if __name__ == '__main__':
    print(findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]))