import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web

style.use('ggplot')

#start = dt.datetime(2015, 1, 1)
#end = dt.datetime.now()
#df = web.DataReader("TWTR", 'morningstar', start, end)
#df.reset_index(inplace=True)
#df.set_index("Date", inplace=True)
#df = df.drop("Symbol", axis=1)

# print(df.tail(5))  # df.tail(5) df.head(5)

#df.to_csv('twir.cvs')

df = pd.read_csv('twir.cvs', parse_dates=True, index_col=0)
#print(df.head())
#df[['Open', 'Close']].plot()
#plt.show()

# Close is not correct we must use Adj Close for this calculation
# df['100ma'] = df['Close'].rolling(window=100).mean()
# We can remove not a number if we use next function
# df.dropna(inplace=True)
# print(df.head())

df_ohlc = df['Close'].resample('10D').ohlc()

df_volume = df['Volume'].resample('10D').sum()

print(df_ohlc.head(4))
print(df_volume.head(4))

df_ohlc.reset_index(inplace=True)
print(df_ohlc.head(4))

df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

print(df_ohlc.head(4))

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)

ax1.xaxis_date()

candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values,0)
# ax1.plot(df.index, df['Close'])
# ax1.plot(df.index, df['100ma'])
# ax2.plot(df.index, df['Volume'])


plt.show()
