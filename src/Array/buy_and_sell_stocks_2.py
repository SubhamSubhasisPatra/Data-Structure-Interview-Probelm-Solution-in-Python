def maxProfit(prices):
    """
    :param prices: A list of prices for a given stock on different days
    :return: The maximum profit that can be obtained by buying and selling the stock

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
