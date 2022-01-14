from math import *

def factor_int(num):
    ''' Factors number input num.

    Input: num > 0 (int)
    Output: list of integer factors of num'''

    # Tests if function input is valid
    assert type(num) == int, (str(num) + " is not an factorable integer!")
    assert num > 1, (str(num) + " is not an factorable integer!")

    ''' Loops through possible factors of num, factors out the
        smallest, appends it as start of list element continued
        by recursive function call '''
        
    for i in range(2, ceil(num/2)):
        if num % i == 0:
            return [i] + factor_int(int(num/i))
    # Returns number if no divisor is found (num is prime, so it factors itself)
    return [num]

def is_palindrome(num, mustsplit=False):
    ''' Tests if number is a palindrome or not (if mustsplit=True) instead
        splits palindrome and returns first segment.

    Input: num > 1 (int), mustsplit (boolean, default =False)
    Output: if mustsplit=False, whether num is palindrome (True/False)
            if mustplit=True, returns first segment up to midpoint of num
                              palindrome.
    '''
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
                temp = int(str(iteration) + '9' + ''.join(reversed(list(str(iteration)))))
                print("Bruh: " + str(temp))
                last_palindrome = temp


    return -1

if __name__ == '__main__':
    print(find_largest_palindrome(3))
    #print(is_palindrome(12121))