def additive_sum(base, increment, count):
    assert count > 0, ('count of additive sum terms must be positive, input is instead ' + str(count))
    return int(count * (base + (count - 1)*increment/2))

def sum_of_mults_before(factor1, factor2, limit):
    assert type(factor1) == int, ('bad input ' + str(factor1) + 'factor must be positive integer')
    assert type(factor2) == int, ('bad input ' + str(factor2) + 'factor must be positive integer')

    assert factor1 > 0, ('bad input ' + str(factor1) + 'factor must be positive integer')
    assert factor2 > 0, ('bad input ' + str(factor2) + 'factor must be positive integer')
    assert limit > 0, ('bad input ' + str(limit) + 'limit must be positive')

    mult_sum = 0
    need_remove_mults_both = 0

    count_factors_from_1 = int(limit/factor1)
    count_factors_from_2 = int(limit/factor2)

    if count_factors_from_1 > 0:
        mult_sum += additive_sum(factor1, factor1, count_factors_from_1)
        need_remove_mults_both += 1
        
    if count_factors_from_2 > 0:
        mult_sum += additive_sum(factor2, factor2, count_factors_from_2)
        need_remove_mults_both += 1

    if need_remove_mults_both == 2:
        count_double_factors = int(limit/(factor1*factor2))
        if(count_double_factors > 0):
            mult_sum -= additive_sum(factor1*factor2, factor1*factor2, count_double_factors)

    return mult_sum

if __name__ == '__main__':
    print('The sum of all multiples of 3 and 5 before 1000 is: ' + str(sum_of_mults_before(3,5,1000)))