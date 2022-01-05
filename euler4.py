from typing import type_check_only


def largest_prime_factor(num):
    assert type(num) == int, (str(num) + " is not an factorable integer!")
    assert num < 2, (str(num) + " is not an factorable integer!")

if __name__ == '__main__':
    print(largest_prime_factor(600851475143))