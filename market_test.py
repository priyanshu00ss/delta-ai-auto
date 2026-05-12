import requests
from config import BOT_TOKEN, CHAT_ID

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd"

response = requests.get(url)
data = response.json()

message = f"""
📊 Live Crypto Price

BTC: ${data['bitcoin']['usd']}
ETH: ${data['ethereum']['usd']}
SOL: ${data['solana']['usd']}
"""

telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

payload = {
    "chat_id": CHAT_ID,
    "text": message
}

requests.post(telegram_url, data=payload)

print("Message Sent Successfully!")