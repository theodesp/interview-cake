def get_change_count(amount, denominations):
    """
    Computes the number of ways to make amount of money with coins of the available denominations.
    Recursive solution
    """
    if (len(denominations) == 0) or (amount < 0):
        return 0

    if amount == 0:
        return 1    
 
    return get_change_count(amount, denominations[:-1]) + get_change_count( amount - denominations[-1], denominations );

def get_change_count_dynamic(amount, denominations):
    """
    Computes the number of ways to make amount of money with coins of the available denominations.
    Dynamic programming solution
    """
    if (len(denominations) == 0) or (amount < 0):
        return 0
    
    results = [[0 for x in range(len(denominations))] for x in range(amount+1)]
 
    # Fill the entries for 0 value case (amount = 0)
    for i in range(len(denominations)):
        results[0][i] = 1
 
    # Fill rest of the table enteries in bottom up manner
    for i in range(1, amount+1):
        for j in range(len(denominations)):
            # Count of solutions including S[j]
            x = results[i - denominations[j]][j] if i-denominations[j] >= 0 else 0
 
            # Count of solutions excluding S[j]
            y = results[i][j-1] if j >= 1 else 0
 
            # total count
            results[i][j] = x + y
 
    return results[amount][len(denominations)-1]


def get_change_count_dynamic_space(amount, denominations):
    """
    Computes the number of ways to make amount of money with coins of the available denominations.
    Dynamic space efficient programming solution
    """
    if (len(denominations) == 0) or (amount < 0):
        return 0

    results = [0 for x in range(amount+1)]

    # Fill the entries for 0 value case (amount = 0)
    results[0] = 1

    for coin in denominations:
        for next_amount in range(coin, amount + 1):
            remainder = next_amount - coin
            results[next_amount] += results[remainder]

    return results[amount]

get_change_count_dynamic_space(5, [1,2])