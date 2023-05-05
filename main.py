import os
import requests
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = os.environ['API_TOKEN']
API_KEY = os.environ['API_KEY']

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Welcome to the Weather Bot! Please enter a city name to get the current weather.")


@dp.message_handler()
async def get_weather(message: types.Message):
    city_name = message.text
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric")
    if response.status_code == 200:
        weather_data = response.json()
        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        await message.reply(f"The current temperature in {city_name} is {temperature}°C and the weather is {description}.")
    else:
        await message.reply(f"Sorry, I couldn't get the weather for {city_name}.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
