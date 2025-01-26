import os
import requests
import re
import telebot

# قراءة التوكن من متغيرات البيئة
token = os.getenv("TOKEN")
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "اكتب ماتريد بالغه الانكليزيه لصنع صوره عليه  مبرمج البوت :- @MRBMOX")

@bot.message_handler(func=lambda message: True)
def Hamko(message):
    query = message.text
    url = "https://flux-image.com/generator"
    params = {
        'prompt': query,
    }
    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36",
        'Accept-Encoding': "gzip, deflate, br, zstd",
        'rsc': "1",
        'sec-ch-ua-platform': "\"Android\"",
        'sec-ch-ua': "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
        'sec-ch-ua-mobile': "?1",
        'next-router-state-tree': "%5B%22%22%2C%7B%22children%22%3A%5B%22(default)%22%2C%7B%22children%22%3A%5B%22PAGE%3F%7B%5C%22gad_source%5C%22%3A%5C%221%5C%22%2C%5C%22gclid%5C%22%3A%5C%22CjwKCAjw9p24BhB_EiwA8ID5Bmz1pj1NONvgX4X5cZx1qExcLF0ad_Uq-z4exPTUpB4ejADVFktdwxoCSeoQAvD_BwE%5C%22%7D%22%2C%7B%7D%2C%22%2F%3Fgad_source%3D1%26gclid%3DCjwKCAjw9p24BhB_EiwA8ID5Bmz1pj1NONvgX4X5cZx1qExcLF0ad_Uq-z4exPTUpB4ejADVFktdwxoCSeoQAvD_BwE%22%2C%22refresh%22%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
        'baggage': "sentry-environment=production,sentry-release=2xqk_ruynNi-OZvrVWofc,sentry-public_key=f7938aa89caf2856d456309bcb2f7d15,sentry-trace_id=84cbe7cecd5242f3ac86090e25c9c7c2,sentry-sample_rate=1,sentry-sampled=true",
        'sentry-trace': "84cbe7cecd5242f3ac86090e25c9c7c2-b673608bc9fac0b0-1",
        'next-url': "/",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://flux-image.com/?gad_source=1&gclid=CjwKCAjw9p24BhB_EiwA8ID5Bmz1pj1NONvgX4X5cZx1qExcLF0ad_Uq-z4exPTUpB4ejADVFktdwxoCSeoQAvD_BwE",
        'accept-language': "ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7",
        'priority': "u=1, i",
    }
    response = requests.get(url, params=params, headers=headers).text
    image_url_pattern = r'"image_url":"(.*?)"'
    match = re.search(image_url_pattern, response)
    if match:
        image_url = match.group(1)
        bot.send_photo(message.chat.id, image_url, caption='PY :- @MRBMOX')
    else:
        bot.send_message(message.chat.id, 'NOT MASSGE ')

bot.polling()