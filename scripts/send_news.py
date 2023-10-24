import os
from telebot import TeleBot, formatting
from dotenv import load_dotenv


load_dotenv()

bot = TeleBot(
    token=os.getenv('BOT_TOKEN'),
    parse_mode='html',
    disable_web_page_preview=True
)
chat_id = os.getenv('CHANNEL_ID')

if __name__ == '__main__':
    bot.send_photo(
        chat_id=chat_id,
        photo=open("D:\Downloads\photo1.jpg", 'rb'),
        caption=f'{formatting.hbold('Awesome photo')}'
    )
