from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = "8516795655:AAHfSA9wS3pf4GcOAFxD052HCBMZKrtdIBE"

dp = Dispatcher()

lemons = 0


# Command handler
@dp.message(Command("start"))
async def command_start_handler(mes):
    await mes.answer("Здарова")


@dp.message(Command("buy_lemon"))
async def buy_lemon(mes):
    global lemons
    lemons += 1
    await mes.answer('Вы получили лимон. Всего лимонов:' + str(lemons))
    
    


# Run the bot
async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


asyncio.run(main())
          
