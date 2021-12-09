def additive_sum(base, increment, count):
    ''' Finds additive sums of type a + (a + d) + (a + 2d) + ... + a + (n-1)d

    Input: base (a) -- FLOAT, increment (d) -- FLOAT, count (n) -- INT > 0
    Output: a + (a + d) + (a + 2d) + ... + a + (n-1)d -- FLOAT
    '''
    assert count > 0, ('count of additive sum terms must be positive, input is instead ' + str(count))
    return count * (base + (count - 1)*increment/2)

def sum_of_mults_before(factor1, factor2, limit):
    ''' Gives the sum of all individual integer multiples of either 
        factor1 or factor2 up to the value 'limit.'
        
    Input: factor1 -- INT, factor2 -- INT, limit -- FLOAT
    Output: sum of integer multiples of either factor1 or factor2 up to limit -- INT
    '''

    # Type/valid input range checks
    assert type(factor1) == int, ('bad input ' + str(factor1) + 'factor must be positive integer')
    assert type(factor2) == int, ('bad input ' + str(factor2) + 'factor must be positive integer')

    assert factor1 > 0, ('bad input ' + str(factor1) + 'factor must be positive integer')
    assert factor2 > 0, ('bad input ' + str(factor2) + 'factor must be positive integer')
    assert limit > 0, ('bad input ' + str(limit) + 'limit must be positive')

    ''' Defines result of sum of multiples, and a variable to check if
    multiples of both factors are present. '''
    mult_sum = 0
    need_remove_mults_both = 0

    # Takes number of int multiples of each individual factor to sum.
    count_factors_from_1 = int((limit-1)/factor1)
    count_factors_from_2 = int((limit-1)/factor2)

    # Sums all multiples of each factor to our multiple sum result variable.
    if count_factors_from_1 > 0:
        mult_sum += int(additive_sum(factor1, factor1, count_factors_from_1))
        # Var counts to 2 if both factors are present.
        need_remove_mults_both += 1
        
    if count_factors_from_2 > 0:
        mult_sum += int(additive_sum(factor2, factor2, count_factors_from_2))
        # Var counts to 2 if both factors are present.
        need_remove_mults_both += 1

    # Removes duplicates of multiples of both factors from our multiple sum.
    if need_remove_mults_both == 2:
        count_double_factors = int((limit-1)/(factor1*factor2))
        if(count_double_factors > 0):
            mult_sum -= int(additive_sum(factor1*factor2, factor1*factor2, count_double_factors))
    
    # Returns our multiple sum calculation.
    return mult_sum

''' Main block prints the answer to our quandary -- the sum of all multiples 
of 3 and 5 before 1000. '''

if __name__ == '__main__':
    print('The sum of all multiples of 3 and 5 before 1000 is: ' + str(sum_of_mults_before(3,5,1000)))