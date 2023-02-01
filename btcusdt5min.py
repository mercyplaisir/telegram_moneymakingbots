import requests
import time
import telegram

# Telegram bot configuration
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
chat_id = "YOUR_TELEGRAM_CHANNEL_ID"
bot = telegram.Bot(token=TOKEN)

# Define Variables
symbol = "BTCUSDT"
interval = "5m"
smaLength = 9
atrLength = 14
rsiLength = 14

# Fetch klines data from Binance
url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}"
response = requests.get(url)
data = response.json()
price = [d[4] for d in data]

# Calculate indicators
sma = ta.sma(price, smaLength)
atr = ta.atr(price, atrLength)
rsi = ta.rsi(price, rsiLength)

# Buy signal
buySignal = ta.cross(price, sma) and rsi < 50

# Sell signal
sellSignal = price > (strategy.position_avg_price + (strategy.position_avg_price * 0.01))

# Trailing Stop
stopPrice = strategy.position_avg_price * (1 - (atr * 0.15))

# Trade management
if (buySignal):
    bot.send_message(chat_id=chat_id, text="Buy opportunity detected! Buy price: {}, Stop loss: {}, Take profit: {}".format(price, stopPrice, price + (price * 0.01)))

if (sellSignal):
    bot.send_message(chat_id=chat_id, text="Sell opportunity detected!")
