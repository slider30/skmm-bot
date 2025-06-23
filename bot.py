
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram import F
import asyncio
import random

TOKEN = "ВСТАВЬ_СЮДА_СВОЙ_ТОКЕН"

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

INSIGHTS = [
    "Психика не повреждена — она адаптирована под травму.",
    "VR — это не бегство от реальности, это вход в новую зону роста.",
    "Тело помнит даже то, чего ум не осознаёт.",
]

@dp.message(F.text == "/start")
async def start_handler(message: Message):
    await message.answer("Добро пожаловать в SKMM Bot! Напиши /insight — и получишь инсайт дня.")

@dp.message(F.text == "/insight")
async def insight_handler(message: Message):
    await message.answer(random.choice(INSIGHTS))

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
