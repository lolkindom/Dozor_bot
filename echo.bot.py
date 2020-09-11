import logging
from Find_word import find_word
from aiogram import Bot, Dispatcher, executor, types
import requests
import re

API_TOKEN = '987969357:AAEA8ZYoFtboEh9FfLRe2xiUNb2WCifziII'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    Я маленький ботик и только учусь
    """
    await message.reply("Приветствую\nЯ часть команды\nНочного Позора 1.0\nПомогу в поиске слов\nНеизвестные буквы "
                        "закрываем ?\nНе знаем количество неизвестных букв - ставим *\nпримеры:\nС??АК? = "
                        "СобАКа\n*БАК* = соБАКа и другие варианты")


@dp.message_handler(regexp='(^cat[s]?$|puss)')
async def cats(message: types.Message):
    with open('cat.jpg', 'rb') as photo:
        '''
        # Old fashioned way:
        await bot.send_photo(
            message.chat.id,
            photo,
            caption='Cats are here 😺',
            reply_to_message_id=message.message_id,
        )
        '''

        await message.reply_photo(photo, caption='Cats are here 😺')


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    # await message.answer(message.text)
    ideal = r'\w+'
    msg = message.text
    msg = msg.replace('*', '%')
    msg = msg.replace('?', '*')
    if len(re.findall(ideal, msg)) > 0:
        if len(find_word(msg)) > 0:
            try:
                await message.answer(find_word(msg))
            except:
                await message.answer('Простите, вариантов слишком много, нужно сократить запрос')
        else:
            await message.answer('Простите, я не нашел подходящих вариантов =(')
    else:
        await message.reply('Неверный запрос\n'
                            'примеры:\nС??АК? = '
                            'СобАКа\n*БАК* = соБАКа и другие варианты')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
