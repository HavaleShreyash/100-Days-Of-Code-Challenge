class StockProfitMaximizer:
    """
    Class to maximize stock profit by identifying buy and sell points.
    """

    def findBuySellPoints(self, stock_prices, num_days):
        """
        Function to find the days of buying and selling stock for max profit.

        Args:
        stock_prices (list): List containing stock prices for each day.
        num_days (int): Total number of days for which stock prices are available.

        Returns:
        list: List of pairs representing buy-sell points for maximizing profit.
              Each pair contains the day index for buying and selling the stock.
        """
        if num_days < 2:
            return []  # If there are fewer than 2 days, no transactions can be made.

        buy_sell_pairs = []
        current_day = 0

        while current_day < num_days - 1:
            # Finding local minima as the buying point
            while current_day < num_days - 1 and stock_prices[current_day + 1] <= stock_prices[current_day]:
                current_day += 1

            if current_day == num_days - 1:
                break  # If we reach the end, break the loop

            buy = current_day  # Store the index of the local minima as the buying point

            current_day += 1

            # Finding local maxima as the selling point
            while current_day < num_days and stock_prices[current_day] >= stock_prices[current_day - 1]:
                current_day += 1

            sell = current_day - 1  # Store the index of the local maxima as the selling point
            buy_sell_pairs.append([buy, sell])  # Add the buy-sell pair to the result

        return buy_sell_pairs

def check(buy_sell_points, stock_prices, total_profit):
    """
    Function to check if the calculated buy-sell points yield the expected profit.

    Args:
    buy_sell_points (list): List of pairs representing buy-sell points.
    stock_prices (list): List containing stock prices for each day.
    total_profit (int): Expected total profit from the buy-sell points.

    Returns:
    int: 1 if the calculated profit matches the expected profit, otherwise 0.
    """
    calculated_profit = 0
    for buy, sell in buy_sell_points:
        calculated_profit += stock_prices[sell] - stock_prices[buy]

    if calculated_profit == total_profit:
        return 1
    else:
        return 0

# Driver Code
if __name__ == '__main__':
    num_test_cases = int(input())
    while num_test_cases > 0:
        input_prices = input().split()  # Read stock prices as a string, split them into individual prices
        num_days = len(input_prices)
        stock_prices = [int(price) for price in input_prices]
        
        stock_manager = StockProfitMaximizer()
        buy_sell_points = stock_manager.findBuySellPoints(stock_prices, num_days)
        total_profit = 0
        for i in range(num_days - 1):
            total_profit += max(0, stock_prices[i + 1] - stock_prices[i])

        if len(buy_sell_points) == 0:
            print("No Profit", end="")
        else:
            print(check(buy_sell_points, stock_prices, total_profit), end="")
        print()
        num_test_cases -= 1
