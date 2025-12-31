import os
import time
from telegram import Bot
from datetime import datetime
import pytz

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=BOT_TOKEN)
tz = pytz.timezone("Africa/Nairobi")

def send(message):
    bot.send_message(chat_id=CHAT_ID, text=message)

while True:
    now = datetime.now(tz).strftime("%H:%M")

    if now == "07:00":
        send("Write all 8 goals here (morning reminder)")

    if now == "20:00":
        send("Daily reviews check-in")

    if now == "21:00":
        send("Write all 8 goals here (night reminder)")

    time.sleep(60)
