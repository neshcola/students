import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = "8516795655:AAHfSA9wS3pf4GcOAFxD052HCBMZKrtdIBE"

dp = Dispatcher()


# Command handler
@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer("Привет! Купи продукты, приготовь лимонад и начни продавать!")


# Run the bot
async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


asyncio.run(main())
