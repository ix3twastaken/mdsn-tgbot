import telebot
import requests
import json
import access_tokens as at

API_TOKEN = at.bot_api_token

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(content_types=['text'])
def get_json(message):
    res = requests.get(f'https://api.vk.com/method/wall.get?domain=nyaslav&count=2&access_token={at.access_token}&v=5.199')
    data = json.loads(res.text)
    bot.send_message(message.chat.id, f'Картиночка: {data["response"]["items"][1]["attachments"][0]["photo"]["sizes"][8]["url"]}')

if __name__ == "__main__":
    bot.polling(none_stop=True)