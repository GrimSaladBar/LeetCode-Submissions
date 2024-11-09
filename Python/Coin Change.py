class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        output = [float('inf')] * (amount + 1)

        #This is the base case
        output[0] = 0

        for c in coins:
            for i in range(c, (amount + 1)):
                output[i] = min(output[i], output[i - c] + 1)
                #print(i, c, output[i])
        return output[amount] if output[amount] != float('inf') else -1

        """
        Init list to inf (just to have a value you wouldn't get from the calc)
        list[0] = 0 cause 0 coins is required for amount 0
        update list with min value:
            Value stored in index i:
                [list[i]starts as inf,
                becomes min coins needed of the
                denomination c to meet the amount i]

                e.g:
                coins = [1, 5, 10]
                amount = 11
                c = 1, i = 1 | 1 to 12
                -> list[1] = min(inf, list[1-1] + 1)
                -> list[1] = min(inf, list[0] + 1) #List[0] is 0 | Base Case
                -> list[1] = min(inf, 1) | therefore list[1] = 1

                c = 5, i = 5 | 5 to 12 || List[5] == 5 for c = 1
                    (cause 5 1-cents needed to meet amount 5)

                -> list[5] = min(5, list[5-5] + 1)
                -> list[5] = min(5, list[0] + 1) #List[0] is 0 | Base Case
                -> list[5] = min(5, 1) | therefore list[5] = 1
        """
