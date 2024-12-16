# https://leetcode.com/problems/evaluate-reverse-polish-notation/submissions/1370590114

def evalRPN(self, tokens: List[str]) -> int:
    numbers = []
    for item in tokens:
        if item not in ['+', '-', '*', '/']:
            numbers.append(int(item))
            continue
        else:
            a = numbers.pop()
            b = numbers.pop()
            if item == '+':
                numbers.append(b + a)
            elif item == '-':
                numbers.append(b - a)
            elif item == '*':
                numbers.append(b * a)
            else:
                numbers.append(int(b/a))
    return numbers[0]