"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
"""

def isValid(s):
    index = -1
    stack = [-1 for _ in range(len(s))]
    char_start = {'(':0, '[':1, '{':2, ')':3, ']':4, '}':5}
    for c in s:
        now = char_start.get(c)
        if now <= 2:
            index += 1
            stack[index] = now
        else:
            if index == -1:
                index += 1
                break
            else:
                if now-3 == stack[index]:
                    index -= 1
                else:
                    break

    if index == -1:
        return True
    else:
        return False

if __name__ == '__main__':
    print(isValid('{[]}'))

