from aiogram import Bot, Dispatcher, executor, types
from PIL import Image, ImageOps
import io

API_TOKEN = '5656912789:AAGs8IFi7M-x8iz_7eX9JilE7rCqKxU7cBk'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(
        "Привет!\nЯ бот-зеркало.\nТы можешь отправить мне фотографию, а я отзеркалю ее и пришлю обратно.")


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply(
        "Ты можешь отправить мне фотографию, а я отзеркалю ее и пришлю обратно.")


@dp.message_handler(content_types=['text'])
async def echo(message: types.Message):
    await message.answer("Я бот-зеркало. Напиши команду /help, чтобы получить инструкции.")


@dp.message_handler(content_types=['photo'])
async def mirror_photo(message: types.Message):
    photo = message.photo[-1]
    photo_file = await bot.download_file_by_id(photo.file_id)
    image = Image.open(photo_file)
    mirrored_image = ImageOps.mirror(image)
    buffer = io.BytesIO()
    mirrored_image.save(buffer, format='JPEG')
    buffer.seek(0)
    await message.reply_photo(buffer)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
