def fibonacci(base1=1, base2=2, count=1):
    if (count-2) == 1:
        return base1 + base2
    else:
        result = 0
        last_sum1 = base2
        last_sum2 = base1

        temp = 0

        for i in range(count-2):
            temp = fibonacci(last_sum2, last_sum1)
            last_sum2 = last_sum1
            last_sum1 = temp

            result += last_sum1
            print((str(last_sum1) + ' +'), end =" ")
        return result + (base1 + base2)

if __name__ == '__main__':
    print('Fibonacci calc is: ' + str(fibonacci(count=5)))