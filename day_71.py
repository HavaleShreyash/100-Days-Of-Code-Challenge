def select_ice_cream(money, prices):
    """
    Finds two candies that, when purchased together, match the total amount of money available.

    Args:
    - money (int): The total amount of money available.
    - prices (list of int): List containing prices of candies.

    Returns:
    - tuple or None: Indices (1-based indexing) of the two candies that meet the criteria or None if no match.
    """
    price_dict = {}  # Dictionary to store prices and their indices

    for i, price in enumerate(prices):
        complement = money - price  # Find the complement to reach the total money

        if complement in price_dict:
            return price_dict[complement] + 1, i + 1

        price_dict[price] = i  

    return None  


if __name__ == "__main__":
    total_money = int(input())  
    candy_prices = list(map(int, input().split())) 

    result = select_ice_cream(total_money, candy_prices)
    if result:
        print(*result)
