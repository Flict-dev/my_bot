import os
from random import randint, choice
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils import executor
from aiogram.utils.emoji import emojize
from aiogram.utils.markdown import bold

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

emoji_list = (
    ':heart:',
    ':unamused:',
    ':smiling_imp:',
    ':point_right: :ok_hand:',
    ':pig:',
)
coin = {
    0: 'Решка, битч!',
    1: 'Орёл, йоу!'
}


def random_pic():
    numb = randint(0, 1)
    PATH = 'D:\ImgaesForProjects\\bot'
    if numb == 0:
        return os.path.join(PATH, 'angry.jpg')
    return os.path.join(PATH, 'sad.jpg')


@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    await bot.send_message(msg.from_user.id,
                           emojize(f'Привет {choice(emoji_list)} \nЕсли хочешь узанть, что я делаю - /help'
                                   )
                           )


@dp.message_handler(commands=['help'])
async def help(msg: types.Message):
    await bot.send_message(msg.from_user.id,
                           bold('Я могу ответить на следующие команды:',
                                emojize('/random - Подброшу монетку :crystal_ball:'),
                                emojize('/photo - Скину милого котика или пёселя :shipit:'),
                                sep='\n'
                                ),
                           )


@dp.message_handler(commands=['random'])
async def random(msg: types.Message):
    await bot.send_message(msg.from_user.id, coin[randint(0, 1)])


@dp.message_handler(commands=['photo'])
async def random(msg: types.Message):
    await bot.send_photo(chat_id=msg.chat.id, photo=open(random_pic(), 'rb'))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
