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

    # Take digits of num as character list, make sure num is not a lone number
    digits = list(str(num))
    assert len(digits) > 1, 'Palindrome must have more than one element to compare'

    # Find middle of palindrome
    middle = (len(digits) - 1) / 2

    if len(digits) % 2 == 0:
        ''' Divide num into two segments from middle, reverses 
        one side for comparison. '''
        seg1 = ''.join(digits[:ceil(middle)])
        seg2 = ''.join(reversed(digits[ceil(middle):]))

        # Return first part of palindrome if mustsplit=True
        if mustsplit:
            return seg1

        # Compare seg1, seg2, if not same return false, if same return true
        return (seg1 == seg2)
    else:
        ''' Divide num into two segments from middle, reverses 
        one side for comparison. '''
        seg1 = ''.join(digits[:int(middle)])
        seg2 = ''.join(reversed(digits[int(middle+1):]))

        # Return first part of palindrome if mustsplit=True
        if mustsplit:
            return seg1

        # Compare seg1, seg2, if not same return false, if same return true
        return (seg1 == seg2)

def find_largest_palindrome(base10):
    ''' Finds and returns largest palindrome that can be multiplied from
        two numbers with base10 count of digits. 
        
    Input: base10 (int)
    Output: largest such palindrome as described above (int)
    '''

    # Sets parameters to search for all palindromes between
    toolarge = 10**(2 * base10)
    toosmall = 10**int(2*(base10-1.5))

    # Starts with first palindrome, finds palindrome segment to iterate
    last_palindrome = toolarge-1
    iteration = int(is_palindrome(last_palindrome, True))

    # Middle digit iteration management variables
    middle_digit = False
    middig = 9

    # Controls whether function should continue running, then prints palindrome
    runcheck = True
    print(last_palindrome)

    # While the palindrome being checked is larger than "toosmall"
    while last_palindrome > toosmall:

        # Checks if middle digit need be added for iteration
        if floor(log10(last_palindrome)) % 2 == 0:
            middle_digit = True

        # Iterates middle digit if present
        if middle_digit:
            while middig > 9 and runcheck:
                middig -= 1

        # Iterates palindrome by decreasing digits outwards from center
        iteration -= 1

        if middle_digit:
            # Iterates palindromes with middle digit into last_palindrome
            last_palindrome = int(str(iteration) + str(middig) + ''.join(reversed(list(str(iteration)))))
            print(last_palindrome)
        else:
            # Iterates palindromes without middle digit into last_palindrome
            if floor(log10(iteration)) == floor(log10(iteration+1)):
                last_palindrome = int(str(iteration) + ''.join(reversed(list(str(iteration)))))
            else:
                ''' Iterates palindromes with middle digit into last_palindrome --
                    adds middle digit to account for digit rollover error. '''
                temp = int(str(iteration) + '9' + ''.join(reversed(list(str(iteration)))))
                print("Bruh: " + str(temp))
                last_palindrome = temp

    # Temporary patch since desired palindrome not found
    return -1

''' MAIN CODE BLOCK '''
if __name__ == '__main__':
    
    # For testing purposes
    print(find_largest_palindrome(3))