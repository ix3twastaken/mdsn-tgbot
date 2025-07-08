import telebot, requests, json, time
from telebot import types
import access_tokens as at


API_TOKEN = at.bot_api_token #API бота телеграм
bot = telebot.TeleBot(API_TOKEN)
URL = f"https://api.telegram.org/bot{API_TOKEN}/getUpdates"



@bot.message_handler(commands=['/send']) #Отправка картинки в чат по команде /send (тестовая версия)
def send(message):
    default_url = 'https://sun9-18.userapi.com/s/v1/ig2/eW0B1deRs-UBS6gjTHojhUtoTG-tvPvvlwQyw6zh2hZjWgATGuIYLapcbPxEyaz6YYnCseN_ceSHNA9PRr_YSg-D.jpg'
    print(default_url)
    img_url = requests.get(f'https://api.vk.com/method/wall.get?domain=club231497262&count=2&access_token={at.access_token}&v=5.199')
    data = json.loads(img_url.text)
    new_img_url = data["response"]["items"][1]["attachments"][0]["photo"]["sizes"][8]["url"]
    print(new_img_url)
    return default_url, new_img_url




# def send(message):
#     send_on=True

#     while send_on==True:
#         # image_url = requests.get(f'https://api.vk.com/method/wall.get?domain=nyaslav&count=2&access_token={at.access_token}&v=5.199')
#         responce = get_updates(message=['text'])
#         print(responce)
#         #отдельный чат для тестов
#         CHAT_ID = '-100' + '2896772060'

#         # index 0 - default_url, index 1 - new_img_url
#         if responce(0) == responce(1):
#             print("pass")
#             pass
#         else: 
#             default_url = responce(1)
#             print(default_url)
#             bot.send_photo(chat_id=CHAT_ID, photo=default_url, message_thread_id=2)

#         time.sleep(600)



    # Получение картинки из сообщества VK


    # CHAT_ID = '-100' + at.my_chat_id #Конечный чат в которое отправляется сообщение (id = "-100" + "id чата")

    # bot.send_photo(chat_id=CHAT_ID, photo=image_url, message_thread_id=86031)



# @bot.message_handler(content=['text'])

# def get_updates():
#     response = requests.get(URL)
#     return print(response.json())

# def main():
#     while True:
#         updates = get_updates()
#         if updates["result"]:
#             # Обработка каждого нового сообщения
#             for item in updates["result"]:
#                 print(f"Сообщение от пользователя: {item['message']['text']}")
#         time.sleep(2)  # Задержка в 2 секунды между запросами

if __name__ == "__main__":
    bot.polling(none_stop=True)