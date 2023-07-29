def maxProfit(prices):
    """
    :param prices: A list of prices for a given stock on different days
    :return: The maximum profit that can be obtained by buying and selling the stock

    This method takes in a list of prices representing the stock price on different days. It calculates the maximum profit that can be obtained by buying and selling the stock.

    The method iterates through the prices list and checks if the price on the current day is less than or equal to the price on the next day. If it is, it enters a nested loop to find the index of the subsequent day with a lower price. The difference between the prices on these two days is added to the max_profit variable.

    After the nested loop, the index is updated to the index of the subsequent day with a lower price found within the nested loop. This ensures that the next iteration of the outer loop starts from the correct index.

    The method continues iterating until the second last day in the prices list, as it does not make sense to buy on the last day without selling.

    Finally, the method returns the maximum profit calculated.

    Example usage:
        prices = [7, 1, 5, 3, 6, 4]
        print(maxProfit(prices))
        # Output: 7

    Note: The logic assumes that you can only buy and sell the stock once per day. Any transaction fees or restrictions are not taken into account.

    """

    max_profit = 0
    index = 0

    while index < len(prices) - 1:

        if prices[index] <= prices[index + 1]:
            next_index = index + 1

            while next_index < len(prices) and prices[next_index] < prices[next_index + 1]:
                next_index += 1

            max_profit += prices[next_index] - prices[index]
            index = next_index
        index += 1

    return max_profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(maxProfit(prices))
