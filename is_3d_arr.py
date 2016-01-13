def prime_factors(n):    
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def product_sets(n):
    return set(products(1, [], n, prime_factors(n)))



def products(current_product, current_list, aim, factors):

    if current_product == aim:
        yield tuple(sorted(current_list))

    elif 0 < current_product < aim:
        for factor in factors:
            if factor != 1:
                for product in products(current_product * factor, current_list + [factor], aim, factors):
                    yield product


def  is_3d_array_size( a_size):
    is_3d = False 
    final_list = list(product_sets(a_size))
    for tuple in final_list:
        if len(tuple)==3:
            is_3d = True
        print tuple
    return is_3d
    

