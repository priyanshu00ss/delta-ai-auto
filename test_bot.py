import requests
from config import BOT_TOKEN, CHAT_ID

message = "✅ Bot Working Perfectly!"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

data = {
    "chat_id": CHAT_ID,
    "text": message
}

response = requests.post(url, data=data)

print(response.text)