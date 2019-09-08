"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""


class BestTimeToBuyAndSellStocks:
    @staticmethod
    def brute_force(prices):
        """
        time complexity: O(n^2)
        space complexity: O(n)
        """
        spreads = [0]
        for index, price in enumerate(prices):
            spread = 0
            for j in range(index + 1, len(prices)):
                next_price = prices[j]
                if next_price - price > spread:
                    spread = next_price - price

            spreads.append(spread)

        return max(spreads)

    @staticmethod
    def one_pass(prices):
        """
        time complexity: O(n)
        space complexity: O(1)
        """
        best_spread = 0
        buy = prices[0] if prices else None

        for i in range(1, len(prices)):
            new_price = prices[i]

            if new_price - buy > best_spread:
                best_spread = new_price - buy

            if new_price < buy:
                buy = new_price

        return best_spread


input1 = [7, 1, 5, 3, 6, 4]
input2 = [7, 6, 4, 3, 1]
input3 = [3, 6, 2, 7, 1, 8]
input4 = []

assert(BestTimeToBuyAndSellStocks.brute_force(input1) == 5)
assert(BestTimeToBuyAndSellStocks.brute_force(input2) == 0)
assert(BestTimeToBuyAndSellStocks.brute_force(input3) == 7)
assert(BestTimeToBuyAndSellStocks.brute_force(input4) == 0)

assert(BestTimeToBuyAndSellStocks.one_pass(input1) == 5)
assert(BestTimeToBuyAndSellStocks.one_pass(input2) == 0)
assert(BestTimeToBuyAndSellStocks.one_pass(input3) == 7)
assert(BestTimeToBuyAndSellStocks.one_pass(input4) == 0)
