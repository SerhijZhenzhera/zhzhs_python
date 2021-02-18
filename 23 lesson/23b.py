'''
Task 2
Write a program that reads in a sequence of characters, and determines whether it's parentheses, braces, and curly brackets are "balanced."
'''


def brackets(check):
    stack = []
    result = ''
    f = 0
    brackets_list_1 = ['(', ')', '{', '}', '[', ']']
    brackets_list_2 = ['()', '{}', '[]']

    for ch in check:
        if ch in brackets_list_1:
            stack.append(ch)

    for st in stack:
        result += st

    while f < len(brackets_list_2):
        for br in brackets_list_2:
            if br in result:
                f = 0
                result = result.replace(br, '')
                if result == '':
                    return 'Sequence is balanced'
            else:
                f += 1
    return 'Sequence is not balanced'


if __name__ == '__main__':
    print(brackets('(aa{bbb})[cc](){}{({[{}]})}'))
    print(brackets('(aa{b)b}b[cc]'))
    print(brackets('(a{aa}b)b]bcc['))
