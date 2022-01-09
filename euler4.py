from math import *

def is_palindrome(num):
    digits = list(str(num))
    assert len(digits) > 1, 'Palindrome must have more than one element to compare'

    middle = (len(digits) - 1) / 2

    if len(digits) % 2 == 0:
        seg1 = ''.join(digits[:ceil(middle)])
        print('People who don\'t know be like: ' + seg1)

        seg2 = ''.join(reversed(digits[ceil(middle):]))
        print('People who know: ' + seg2)

        return (seg1 == seg2)
    else:
        seg1 = ''.join(digits[:int(middle)])
        print('People who don\'t know be like: ' + seg1)

        seg2 = ''.join(reversed(digits[int(middle+1):]))
        print('People who know: ' + seg2)

        return (seg1 == seg2)


def find_largest_palindrome(base10):
    toolarge = 10**(2 * base10)

    return -1

if __name__ == '__main__':
    #print(find_largest_palindrome(3))
    print(is_palindrome(12121))