# pip install pyTelegramBotAPI
import telebot

# go to https://t.me/BotFather apply
BOT_TOKEN = "API_KEY"

bot = telebot.TeleBot(BOT_TOKEN)

# read bad words in text file
def read_txt_file(file_path):
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            lines = file.readlines()
            content_list = [line.strip() for line in lines]
        return content_list
    except FileNotFoundError:
        print("file not found")
        return []
    except Exception as e:
        print(f"load file error：{e}")
        return []

# need a words text file
# if detect users' msg include the bad word
# bot will delete msg
file_name = "words.txt"
bad_words = read_txt_file(file_name)

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    for bad_word in bad_words:
        if bad_word in message.text:
          bot.delete_message(message.chat.id, message.message_id)

if __name__ == "__main__":
    bot.infinity_polling()
