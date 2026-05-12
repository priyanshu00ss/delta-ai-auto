import requests
import time
from config import BOT_TOKEN, CHAT_ID

while True:
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd"

    response = requests.get(url)
    data = response.json()

    btc = data['bitcoin']['usd']
    eth = data['ethereum']['usd']
    sol = data['solana']['usd']

    signal = "HOLD ⏳"
    entry = btc
    stoploss = 0
    target = 0

    if btc > 100000:
        signal = "BUY 🚀"
        stoploss = btc - 1500
        target = btc + 3000

    elif btc < 90000:
        signal = "SELL 🔻"
        stoploss = btc + 1500
        target = btc - 3000

    message = f"""
🔥 Delta AI Auto Signal

BTC: ${btc}
ETH: ${eth}
SOL: ${sol}

📌 Entry: ${entry}
🎯 Target: ${target}
🛑 Stoploss: ${stoploss}

Signal: {signal}
Timeframe: 15m
Leverage: 5x
"""

    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(telegram_url, data=payload)

    print("Signal Sent!")

    time.sleep(900)