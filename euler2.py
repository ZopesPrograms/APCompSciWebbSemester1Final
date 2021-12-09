def fibonacci(base1=1, base2=2, loops=1):
    if loops == 1:
        return base1 + base2
    else:
        result = 0
        last_sum1 = 0
        last_sum2 = 0

        for i in range(loops):
            last_sum2 = last_sum1
            last_sum1 = fibonacci(last_sum2, last_sum1)

            result += last_sum1
        return result

if __name__ == '__main__':
    print('Fibonacci calc is: ' + fibonacci(loops=4))