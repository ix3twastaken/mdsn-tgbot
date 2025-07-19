import telebot, requests, json, time
from telebot import types
import access_tokens as at  # Импорт токенов (токен бота, сервисный ключ vk, айди конечного чата telegram)


API_TOKEN = at.bot_api_token #API бота телеграм
bot = telebot.TeleBot(API_TOKEN)


# Получение обновлений изображения из VK
def get_updates():
    new_img_urls = []

    img_url = requests.get(f'https://api.vk.com/method/wall.get?domain=nyaslav&count=2&access_token={at.access_token}&v=5.199') 
    json_urls = img_url.json()                          
    # print(json_urls)               # чтобы получить пост, отличный от второго, необходимо заменить count в ссылке и индекс item в json запросе
    photo_index = 0
    while photo_index < 10:
        try:
            if json_urls["response"]["items"][1]["attachments"][photo_index]["type"] == 'photo':    # Проверка на нужный тип файла
                urls = json_urls["response"]["items"][1]["attachments"][photo_index]["photo"]["sizes"][-1]["url"]    # Получение ссылки на изображение
                new_img_urls.append(urls)   # Добавление в список с ссылками для отправки
        except IndexError:
            print("index_error")
            pass

        photo_index += 1
    return new_img_urls

# Включение периодической пересылки изображений
@bot.message_handler(commands=['send_on']) 
def polling(message):
    send_on=True
    default_url = ''
    CHAT_ID = '-100' + at.my_chat_id   # Конечный чат в которое отправляется сообщение (id = "-100" + "id чата")

    while send_on==True:
        urls_list = get_updates()

        if urls_list == []:     # Проверка на случай, если тип данных не "photo"
            print("empty")
            pass
        else:
            if len(urls_list) < 2:  # Минимально допустимое значение массива, передеваемое в InputMediaPhoto равняется 2
                if default_url in urls_list:
                    print("the same1")
                    pass
                else: 
                    default_url = urls_list[0]
                    bot.send_photo(CHAT_ID, photo=default_url, message_thread_id=86031)
            else:
                if default_url in urls_list: 
                    print("the same2")
                    pass
                else:
                    bot.send_media_group(CHAT_ID, [types.InputMediaPhoto(i) for i in urls_list], message_thread_id=86031)
                

        time.sleep(1200)

if __name__ == "__main__":
    bot.polling(none_stop=True)