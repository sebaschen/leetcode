#122_Best_Time_to_Buy_and_Sell_Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans_list=[]        
        #Iterate through the substract between each element
        for i in range(1,len(prices)):
            x = prices[i] - prices[i-1]
            #if the gap is a postive number, save it to the list
            if x > 0:
                ans_list.append(x)
        return sum(ans_list)
            