def fibonacci(base1=1, base2=2, count=3, stringres=False):
    ''' Takes fibonacci sum of count 'count' starting with base1 and base2, 
        F_count = base1 + base2 + (base1 + base2) + (base1 + base2 + base2) + ...
        for 'count' number of terms 
        
    Input: base1 (default=1) -- FLOAT, base2 (default=2) -- FLOAT,
           count (default=3) -- INT, stringres (default=False) -- BOOL

    Output: fibonacci sum from base1 + base2 by as many terms as 'count'
            in the fibonacci sequence
    '''

    # Checks for valid input argument types

    assert (type(base1) == int or type(base1) == float), (str(base1) + ' is not of numerical type!')
    assert (type(base2) == int or type(base2) == float), (str(base2) + ' is not of numerical type!')

    assert type(count) == int, (str(count) + ' is not a positive integer!')
    assert count > 0, (str(count) + ' is not a positive integer!')

    assert type(stringres) == bool, (str(stringres) + ' is not bool value!')

    # Code for base1 + base2 sum, simplest fibonacci calculation

    if (count-2) == 1:
        if stringres == False:
            return base1 + base2
        # String result case, puts our calculation to a string
        else:
            return str(base1) + ' + ' + str(base2) + ' = ' + str(base1 + base2)
    # Code for larger fibonacci sums
    else:
        # Numerical and string result variables
        result = base1 + base2
        strres = ''

        ''' Additive memory variables, so fibonacci function can continously 
            update previous two terms fibonacci next term is summed from. '''
        last_sum1 = base2
        last_sum2 = base1

        # Temporary storage variable
        temp = 0

        # Fibonacci term-summing loop, adding as many terms as 'count'
        for i in range(count-2):
            ''' If a string result is desired, include the last_sum2 in the
                addition list through the string. '''
            if stringres == True:
                strres += (str(last_sum2) + ' + ')

            ''' Uses recursive fibonacci function to sum the next term from the
                previous two, and then updates the 'previous two' to include
                itself so as to find the next term and so on. '''
            temp = fibonacci(last_sum2, last_sum1)
            last_sum2 = last_sum1
            last_sum1 = temp

            # Adds the newly calculated term to the result
            result += last_sum1

        # Formats and concludes the string result data if desired
        if stringres == True:
            strres += (str(last_sum2) + ' + ')
            strres += (str(last_sum1) + ' = ' + str(result))

        ''' If string result desired, returns that -- otherwise returns numerical
            fibonacci sum. '''
        if stringres == False:
            return result
        else:
            return strres

def even_fibonacci_under(base1, base2, limit):
    ''' Takes fibonacci sum starting with base1 and base2, 
        F_count = base1 + base2 + (base1 + base2) + (base1 + base2 + base2) + ...
        for all such terms < limit.
        
    Input: base1 -- INT, base2 -- INT, limit -- FLOAT
    Output: fibonacci sum from base1 + base2 through all fibonacci terms < limit
    '''

    # Checks for valid input argument types

    assert type(base1) == int, (str(base1) + ' is not a positive integer!')
    assert base1 > 0, (str(base1) + ' is not a positive integer!')

    assert type(base2) == int, (str(base2) + ' is not a positive integer!')
    assert base2 > 0, (str(base2) + ' is not a positive integer!')

    assert (type(limit) == float or type(limit) == int), (str(limit) + ' is not a positive float!')
    assert limit > 0, (str(limit) + ' is not a positive float!')

    # Numerical result variable
    result = base1 + base2

    ''' Additive memory variables, so fibonacci function can continously 
        update previous two terms fibonacci next term is summed from. '''
    last_sum1 = base2
    last_sum2 = base1

    # Temporary storage variable
    temp = 0

    # Fibonacci term-summing loop, adding all fibonacci terms < limit
    while last_sum1 < limit:

        ''' Uses recursive fibonacci function to sum the next term from the
            previous two, and then updates the 'previous two' to include
            itself so as to find the next term and so on. '''
        temp = int(fibonacci(last_sum2, last_sum1))
        last_sum2 = last_sum1
        last_sum1 = temp

        # Adds the newly calculated term (IF EVEN) to the result.
        if last_sum1/2 == int(last_sum1/2): result += last_sum1
    # Removes last sum over limit from our result, also excess 1
    if last_sum1/2 == int(last_sum1/2): result -= last_sum1
    result -= 1

    # Returns numerical fibonacci sum.
    return result

# Example code
if __name__ == '__main__':
    print('Fibonacci calc is: ' + fibonacci(count=9,stringres=True))
    print('Even fibonaccis under 10 sum is: ' + str(even_fibonacci_under(1,2,56)))

    # Our targeted result
    print('Even fibonaccis under 4,000,000 sum is: ' + str(even_fibonacci_under(1,2,4000000)))