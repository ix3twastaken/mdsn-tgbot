import telebot, requests, json, time
from telebot import types
import access_tokens as at


API_TOKEN = at.bot_api_token #API бота телеграм
bot = telebot.TeleBot(API_TOKEN)


#Получение обновлений изображения из VK
def get_updates():
    default_url = ''

    img_url = requests.get(f'https://api.vk.com/method/wall.get?domain=club231497262&count=2&access_token={at.access_token}&v=5.199')
    data = json.loads(img_url.text)
    new_img_url = data["response"]["items"][1]["attachments"][0]["photo"]["sizes"][8]["url"]
    return default_url, new_img_url

@bot.message_handler(commands=['send_on']) #Включение периодической пересылки изображений
def polling(message):
    send_on=True
    while send_on==True:
        responce = get_updates()

        CHAT_ID = '-100' + at.my_chat_id    #Конечный чат в которое отправляется сообщение (id = "-100" + "id чата")

        if responce[0] == responce[1]:      # index 0 - default_url, index 1 - new_img_url
            pass
        else: 
            default_url = responce[1]
            bot.send_photo(chat_id=CHAT_ID, photo=default_url, message_thread_id=2)

        time.sleep(600)



if __name__ == "__main__":
    bot.polling(none_stop=True)