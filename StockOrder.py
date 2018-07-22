#股票自动交易助手 Python 自动下单使用 例子
#把此脚本和 StockOrderApi.py Order.dll 放到你自己编写的脚本同一目录

from StockOrderApi import *

#买入测试
#Buy(u"600000" , 100, 0, 1, 0)

#卖出测试,是持仓股才会有动作
#Sell(u"000100" , 100, 0, 1, 0)

#账户信息
print("股票自动交易接口测试")
print("账户信息")
print("--------------------------------")

arrAccountInfo = ["总资产", "可用资金", "持仓总市值", "总盈利金额", "持仓数量"];
for i in range(0, len(arrAccountInfo)):
 value = GetAccountInfo( u""  , i, 0)
 print ("%s %f "%(arrAccountInfo[i], value))

print("--------------------------------")
print(" ")

print("股票持仓")
print("--------------------------------")
#取出所有的持仓股票代码,结果以 ','隔开的
allStockCode = GetAllPositionCode(0)
allStockCodeArray = allStockCode.split(',')
for i in range(0, len(allStockCodeArray)):
 vol = GetPosInfo( allStockCodeArray[i]  , 0 , 0)
 changeP = GetPosInfo( allStockCodeArray[i]  , 4 , 0)
 print ("%s %d %.2f%%"%(allStockCodeArray[i], vol, changeP))

print("--------------------------------")

print("可撤买单")
print("--------------------------------")
allStockCode = GetAllOrderCode(0,1)
allStockCodeArray = allStockCode.split(',')
for i in range(0, len(allStockCodeArray)):
 vol = GetOrderInfo( allStockCodeArray[i]  , 0 , 0, 0)
 seconds = GetOrderInfo( allStockCodeArray[i]  , 0 , 1, 0)
 print ("%s %d %d"%(allStockCodeArray[i], vol, seconds))

print("--------------------------------")

print("可撤卖单")
print("--------------------------------")
allStockCode = GetAllOrderCode(0,2)
allStockCodeArray = allStockCode.split(',')
for i in range(0, len(allStockCodeArray)):
 vol = GetOrderInfo( allStockCodeArray[i]  , 1 , 0, 0)
 seconds = GetOrderInfo( allStockCodeArray[i]  , 1 , 1, 0)
 print ("%s %d %d"%(allStockCodeArray[i], vol, seconds))

print("--------------------------------")

#撤买
CancelOrder("600036", 1, 0);
#撤卖
CancelOrder("600018", 2, 0);
