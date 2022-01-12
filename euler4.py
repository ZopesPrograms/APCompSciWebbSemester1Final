from math import *

def factor_int(num):
    
    assert type(num) == int, (str(num) + " is not an factorable integer!")
    assert num > 1, (str(num) + " is not an factorable integer!")

    ''' Finds smallest prime divisor of num, extracts it, then extracts the
        next prime divisor of num through recursion then extracts the next
        prime divisor, and so on until the last, largest prime divisor is
        found. '''
    for i in range(2, ceil(num/2)):
        if num % i == 0:
            return [i] + factor_int(int(num/i))
    # Returns number if no divisor is found (num is prime, ergo it is largest prime)
    return [num]

def is_palindrome(num, mustsplit=False):
    digits = list(str(num))
    assert len(digits) > 1, 'Palindrome must have more than one element to compare'

    middle = (len(digits) - 1) / 2

    if len(digits) % 2 == 0:
        seg1 = ''.join(digits[:ceil(middle)])
        print('People who don\'t know be like: ' + seg1)

        seg2 = ''.join(reversed(digits[ceil(middle):]))
        print('People who know: ' + seg2)

        if mustsplit:
            return seg1

        return (seg1 == seg2)
    else:
        seg1 = ''.join(digits[:int(middle)])
        print('People who don\'t know be like: ' + seg1)

        if mustsplit:
            return seg1

        seg2 = ''.join(reversed(digits[int(middle+1):]))
        print('People who know: ' + seg2)

        return (seg1 == seg2)

def find_largest_palindrome(base10):
    toolarge = 10**(2 * base10)
    toosmall = 10**int(2*(base10-1.5))

    last_palindrome = toolarge-1
    iteration = int(is_palindrome(last_palindrome, True))

    middle_digit = False
    middig = 9

    runcheck = True
    print(last_palindrome)

    while last_palindrome > toosmall:
        if floor(log10(last_palindrome)) % 2 == 0:
            middle_digit = True
        
        if middle_digit:
            while middig > 9 and runcheck:
                middig -= 1

        iteration -= 1
        if middle_digit:
            last_palindrome = int(str(iteration) + str(middig) + ''.join(reversed(list(str(iteration)))))
            print(last_palindrome)
        else:
            if floor(log10(iteration)) == floor(log10(iteration+1)):
                last_palindrome = int(str(iteration) + ''.join(reversed(list(str(iteration)))))
            else:
                last_palindrome = int(str(iteration) + '9' + ''.join(reversed(list(str(iteration)))))
            print(last_palindrome)

    return -1

if __name__ == '__main__':
    print(find_largest_palindrome(3))
    #print(is_palindrome(12121))