from math import *

def largest_prime_factor(num):
    ''' Find largest prime factor of our integer num > 1.
        
    Input: an integer num > 1
    Output: the largest prime factor in our num
    '''

    # Checks our number is a factorable integer > 1
    assert type(num) == int, (str(num) + " is not an factorable integer!")
    assert num > 1, (str(num) + " is not an factorable integer!")

    ''' Finds smallest prime divisor of num, extracts it, then extracts the
        next prime divisor of num through recursion then extracts the next
        prime divisor, and so on until the last, largest prime divisor is
        found. '''
    for i in range(2, ceil(num/2)):
        if num % i == 0:
            return largest_prime_factor(int(num/i))
    # Returns number if no divisor is found (num is prime, ergo it is largest prime)
    return num

# Main block, prints out our found largest prime factor
if __name__ == '__main__':
    print(largest_prime_factor(600851475143))