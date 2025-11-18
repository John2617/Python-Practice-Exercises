cos,sell=map(int,input().split())
if sell>cos:
    profit=sell-cos
    profit_percentage=(profit*100)//cos
    print("profit = ",profit_percentage)
else:
    loss=cos-sell
    profit_percentage=(loss*100)//sell
    print("loss = ",profit_percentage)