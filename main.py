import telebot, requests, json
from telebot import types
import access_tokens as at


API_TOKEN = at.bot_api_token #API бота телеграм
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['send']) #Отправка картинки в чат по команде /send (тестовая версия)
def send(message):

    # Получение картинки из сообщества VK
    image_url = requests.get(f'https://api.vk.com/method/wall.get?domain=nyaslav&count=2&access_token={at.access_token}&v=5.199')
    data = json.loads(image_url.text)
    image_url = data["response"]["items"][1]["attachments"][0]["photo"]["sizes"][8]["url"]

    CHAT_ID = '-100' + at.my_chat_id #Конечный чат в которое отправляется сообщение (id = "-100" + "id чата")

    bot.send_photo(chat_id=CHAT_ID, photo=image_url, message_thread_id=86031) #Отправка в чат



if __name__ == "__main__":
    bot.polling(none_stop=True)