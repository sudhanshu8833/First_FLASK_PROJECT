# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager


import requests
import json
import pandas as pd
import datetime as dt


# %%
import telepot
bot = telepot.Bot('1997104156:AAElGj2e-Fpqx4LbK8bLEfrPGqSNr_em9DA')
bot.getMe()


df4 = pd.read_csv("system.csv")

client = Client(str(df4['system'][2]),str(df4['system'][3]))


# def candle(symbol, interval):


#     root_url = 'https://api.binance.com/api/v1/klines'
#     url = root_url + '?symbol=' + symbol + '&interval=' + interval
#     data = json.loads(requests.get(url).text)
#     df = pd.DataFrame(data)
#     df.columns = ['Datetime',
#                 'Open', 'High', 'Low', 'Close', 'volume',
#                 'close_time', 'qav', 'num_trades',
#                 'taker_base_vol', 'taker_quote_vol', 'ignore']
#     df.index = [dt.datetime.fromtimestamp(x / 1000.0) for x in df.close_time]
    
#     df.drop(['close_time','qav','num_trades','taker_base_vol', 'taker_quote_vol', 'ignore'],axis=1,inplace=True)
           
    
#     df['Open']=pd.to_numeric(df["Open"], downcast="float")
#     df["High"]=pd.to_numeric(df["High"], downcast="float")
#     df["Low"]=pd.to_numeric(df["Low"], downcast="float")
#     df["Close"]=pd.to_numeric(df["Close"], downcast="float")
#     df["volume"]=pd.to_numeric(df["volume"], downcast="float")

#     # atr1='FIXED_ATR'
#     # df[atr1]=TA.ATR(df,int(df1['atr_fixed'][0]))
#     # df['X_BARS_HIGH']=df['High'][-int(df1['X_bars_high'][0]):-1].max()
#     # df['X_BARS_LOW']=df['Low'][-int(df1['X_bars_low'][0]):-1].min()

#     # atr=TA.ATR(df,int(df1['atr_trailing'][0]))
    

#     # df['TRAILING_ATR']=TA.ATR(df,int(df1['atr_trailing'][0]))
    

#     return df


# %%
def ltp_price(instrument):
    prices = client.get_all_tickers()
    for i in range(len(prices)):
        if prices[i]['symbol']==str(instrument):
            
            return float(prices[i]['price'])


# %%
def market_order():
    global m, price
    # fixed_buy_atr=float(df['FIXED_ATR'][-1])

    p_l=float(client.futures_account_balance()[0]['balance'])
    # stoploss=float(df1['stop_loss_percentage'][0])/100 * p_l
    quantity=int(series['quantity'])

    try:
        order = client.create_order(
            symbol=str(series['instrument']),
            side=Client.SIDE_BUY,
            type=Client.ORDER_TYPE_MARKET,
            quantity=int(series['quantity']))
    except Exception as e:
        botss=str(e)
        bot.sendMessage(1039725953,botss)
    price=ltp_price(series['instrument'])

    m+=1
    


# %%
def market_order1():
    global m,price
    
    # fixed_sell_atr=float(df['FIXED_ATR'][-1])


    p_l=float(client.futures_account_balance()[0]['balance'])
    # stoploss=float(df1['stop_loss_percentage'][0])/100 * p_l
    # quantity_sell=int(stoploss/fixed_buy_atr)

    try:
        order = client.create_order(
            symbol=str(series['instrument']),
            side=Client.SIDE_SELL,
            type=Client.ORDER_TYPE_MARKET,
            quantity=int(series['quantity']))


    except Exception as e:
        botss=str(e)
        bot.sendMessage(1039725953,botss)

    price=ltp_price(series['instrument'])

    m+=1


# %%
def close_position():
    global m,orders
    try:
        for order in orders:
            if order['type']=='buy':
                try:
                    order = client.create_order(
                        symbol=str(order['instrument']),
                        side=Client.SIDE_SELL,
                        type=Client.ORDER_TYPE_MARKET,
                        quantity=int(order['quantity']))

                except Exception as e:
                    botss=str(e)
                    bot.sendMessage(1039725953,botss)

            if order['type']=='sell':
                try:
                    order = client.create_order(
                        symbol=str(order['instrument']),
                        side=Client.SIDE_BUY,
                        type=Client.ORDER_TYPE_MARKET,
                        quantity=int(order['quantity']))

                except Exception as e:
                    botss=str(e)
                    bot.sendMessage(1039725953,botss)

        orders=[]
        bot.sendMessage(1039725953,'POSITIONS CLOSED')
        

        m=0
    except Exception as e:
        botss=str(e)
        bot.sendMessage(1039725953,botss)



    


# %%

def trade_signal():
    
    global series,price

    ltp=ltp_price(series['instrument'])
    bot.sendMessage(1039725953,str(ltp))    

    signal=""
    if series['buy/sell']=='buy' and series['trigger']=='PRICE':
        if ltp>=float(series['stop_value']):
            signal='buy'
            # price=ltp



    elif series['buy/sell']=='sell' and series['trigger']=='PRICE':
        if ltp<=float(series['stop_value']):
            signal='sell'
            # price=ltp

    elif series['buy/sell']=='buy' and series['trigger']=='PERCENTAGE':
        if ltp>=price+price*(float(series['stop_value']))/100:
            signal='buy'
            



    elif series['buy/sell']=='sell' and series['trigger']=='PERCENTAGE':
        if ltp<=price-price*(float(series['stop_value']))/100:
            signal='sell'

    elif series['buy/sell']=='close above' and series['trigger']=='PERCENTAGE':
        if ltp>=price+price*(float(series['stop_value']))/100:
            close_position()


            

    elif series['buy/sell']=='close below' and series['trigger']=='PERCENTAGE':
        if ltp<=price-price*(float(series['stop_value']))/100:
            close_position()



    elif series['buy/sell']=='close below' and series['trigger']=='PRICE':
        if ltp<=float(series['stop_value']):
            # bot.sendMessage(1039725953,'POSITIONS CLOSED') 
            close_position()



    elif series['buy/sell']=='close above' and series['trigger']=='PRICE':
        if ltp>=float(series['stop_value']):
            close_position()
            


    return signal    


# %%
def main():
    global ltp,df1,series,m,orders
    df4 = pd.read_csv("system.csv")

    client = Client(str(df4['system'][2]),str(df4['system'][3]))

    df1 = pd.read_csv("strategy.csv")
    length=len(df1)
    series=df1[:].iloc[m]
    # if series['buy/sell']=='N':
    #     m=0

    # if m==len(df1)-1:
    #     m=0
    print(series)
    # ltp=ltp_price(series['instrument'])
    if series['buy/sell']=='restart':
        m=0
    
    if series['buy/sell']=='off':
        while True:
            df1 = pd.read_csv("strategy.csv")
            series=df1[:].iloc[m]
            if series['buy/sell']=='buy' or series['buy/sell']=='sell':
                break
                
    
    
        
        
        # position=position_now(df1['symbol_binance'][0])
    signal=trade_signal()

        
        
    


    if signal=='buy':
        market_order()

        order={}
        order['instrument']=series['instrument']
        order['quantity']=series['quantity']
        order['type']=series['buy/sell']
        orders.append(order)

        bot.sendMessage(1039725953,str(orders))
        bot.sendMessage(1278992057,str(orders))
        bot.sendMessage(1039725953,f"New long position initiated at {price}")
        bot.sendMessage(1278992057,f"New long position initiated at {price}")
        bot.sendMessage(1278992057,f"Now it is looking for order {m+1}")
        bot.sendMessage(1039725953,f"Now it is looking for order {m+1}")



    if signal=='sell':
        market_order1()
        order={}
        order['instrument']=series['instrument']
        order['quantity']=series['quantity']
        order['type']=series['buy/sell']
        orders.append(order)

        bot.sendMessage(1039725953,str(orders))
        bot.sendMessage(1278992057,str(orders))
        bot.sendMessage(1039725953,f"New short position initiated at {price}")
        bot.sendMessage(1278992057,f"New short position initiated at {price}")
        bot.sendMessage(1278992057,f"Now it is looking for order {m+1}")
        bot.sendMessage(1039725953,f"Now it is looking for order {m+1}")

    if signal=="squareoffsell":
        market_order1()




        # bot.sendMessage(1039725953,f" profit of {((price-price)/price)*100*int(df1['binance_X'][0])}")
    if signal=="squareoffbuy":
        market_order()



        # bot.sendMessage(1039725953,f" profit of {((price-price)/price)*100*int(df1['binance_X'][0])}")



# %%
df1 = pd.read_csv("strategy.csv")
m=0
order_id=[]
orders=[]

while True:
    try:

        main()
    # print("hello")
    except Exception as e:
        botss=str(e)
        bot.sendMessage(1039725953,botss)



