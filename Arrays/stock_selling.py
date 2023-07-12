def stock_sell(l):
    profit=0
    for i in range(1,len(l)):
        if l[i]>l[i-1]:
            profit=profit+(l[i]-l[i-1])
    return profit
l=[1,2,5,3,8,12]
print(stock_sell(l))