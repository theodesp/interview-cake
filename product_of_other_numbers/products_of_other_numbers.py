import functools
import itertools
import operator

def get_products_of_all_ints_except_at_index(int_list):
    result = []
    for index, item in enumerate(int_list):
        product = functools.reduce(operator.mul, itertools.chain(int_list[:index], int_list[index+1:]), 1)
        result.insert(index, product)

    return result
