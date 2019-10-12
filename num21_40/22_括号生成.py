"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
例如，给出 n = 3，生成结果为：
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
def generateParenthesis(n):
    result = []
    def create(now, num1, num2):
        if num1 == 0 and num2 == 0:
            result.append("".join(now))
        else:
            if num1 > 0:
                now.append('(')
                num1 -= 1
                create(now, num1, num2)
                now.pop()
                num1 += 1
            if num1 < num2:
                now.append(')')
                num2 -= 1
                create(now, num1, num2)
                now.pop()
                num2 += 1
    now = []
    create(now, n, n)
    return result

if __name__ == '__main__':
    print(generateParenthesis(4))

