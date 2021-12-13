def fibonacci(base1=1, base2=2, count=3, stringres=False):
    ''' Takes fibonacci sum of count 'count' starting with base1 and base2, 
        F_count = base1 + base2 + (base1 + base2) + (base1 + base2 + base2) + ...
        for 'count' number of terms 
        
    Input: base1 (default=1) -- FLOAT, base2 (default=2) -- FLOAT,
           count (default=3) -- INT, stringres (default=False) -- BOOL

    Output: fibonacci sum
    '''

    assert (type(base1) == int or type(base1) == float), (str(base1) + ' is not of numerical type!')
    assert (type(base2) == int or type(base2) == float), (str(base2) + ' is not of numerical type!')

    assert type(count) == int, (str(count) + ' is not a positive integer!')
    assert count > 0, (str(count) + ' is not a positive integer!')

    assert type(stringres) == bool, (str(stringres) + ' is not bool value!')

    if (count-2) == 1:
        if stringres == False:
            return base1 + base2
        else:
            return str(base1) + ' + ' + str(base2) + ' = ' + str(base1 + base2)
    else:
        result = 0
        strres = ''

        last_sum1 = base2
        last_sum2 = base1

        temp = 0

        for i in range(count-2):
            if stringres == True:
                strres += (str(last_sum2) + ' + ')
            temp = fibonacci(last_sum2, last_sum1)
            last_sum2 = last_sum1
            last_sum1 = temp

            result += last_sum1
        result += (base1 + base2)

        if stringres == True:
            strres += (str(last_sum2) + ' + ')
            strres += (str(last_sum1) + ' = ' + str(result))

        if stringres == False:
            return result
        else:
            return strres

if __name__ == '__main__':
    print('Fibonacci calc is: ' + fibonacci(count=5,stringres=True))