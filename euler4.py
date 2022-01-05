from math import *

def largest_prime_factor(num):
    assert type(num) == int, (str(num) + " is not an factorable integer!")
    assert num > 1, (str(num) + " is not an factorable integer!")

    for i in range(0, ceil(num/2)):
        if num % i == 0:
            return num/i
    return -1

if __name__ == '__main__':
    print(largest_prime_factor(600851475143))