inp = input().split(', ')


def palindrome_check(a):
    for i in a:
        if i[::-1] == i:
            print('True')
        else:
            print('False')


palindrome_check(inp)
