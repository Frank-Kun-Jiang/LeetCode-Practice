def maxProfit(prices: List[int]) -> int:
    result=0
    if len(prices)<2:
        return result
    for i in range(len(prices)-1):
        if prices[i]<prices[i+1]:
            for y in range(i+1,len(prices)):
                tempresult = prices[y]-prices[i]
                if tempresult>result:
                    result=tempresult
    return result


print(maxProfit([7,1,5,3,6,4]))