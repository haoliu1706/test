from hikyuu.interactive.interactive import *
import pandas as pd
# use_draw_engine('echarts') #use_draw_engine('matplotlib')  #默认为'matplotlib'绘图
aqq = pd.DataFrame()
#合并close
for s in blocka:
    #exit()
    k = s.getKData(Query(-10000, recoverType=Query.FORWARD))
    # print(s.code)
    #break
    df = k.to_df() 
    d = pd.read_csv('000001.csv', index_col='datetime')  # ['close']#header=0 )#,
            # print(d.tail(5))
    d.rename(columns={'close': 'sh'}, inplace=True)
    d.drop(['open', 'high', 'low', 'amount', 'volume'], 1, inplace=True)
            # print(d)
            # print(d.tail(5))
    df.rename(columns={'close': s.code}, inplace=True)
    df.drop(['open', 'high', 'low', 'amount', 'volume'], 1, inplace=True)
            # print(df.tail(5))
    if aqq.empty:
        aqq = d
                # print(a.tail(5))
    else:
        aqq = aqq.join(df, how='outer')  # ,on='datetime')
    aqq.fillna(0, inplace=True)

aqq.to_csv('aa0620.csv')



############################################################################################################################
aaa= pd.read_csv('aa0620.csv', index_col=0)
#print(len(aaa.index))

for i in aaa.columns:
    aaa[i] = aaa[i].pct_change()


#日期转成股票

d2=aaa.T
#print(d2.tail(1))
p1=[]
p2=[]
#涨跌幅个数

for i in d2.columns:
    #print(d2[i])

    pp = 0
    ppp = 0
    for p in d2[i]:
        if p>0.05 and p <0.101:
            pp+=1

        elif p<-0.05 and p> -0.11:
            ppp+=1
    p1.append(pp)
    p2.append(ppp)
aaa.fillna(0, inplace=True)
aaa['+0.05 no.']=p1
aaa['-0.05 no.']=p2
#print(len(aaa['+0.08 no.']))
print(aaa.tail(100))
aaa.to_csv('0.050620.csv')

