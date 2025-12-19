from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = "8516795655:AAHfSA9wS3pf4GcOAFxD052HCBMZKrtdIBE"

dp = Dispatcher()

lemons = 0
money = 50
lemonade = 0
sugar = 0
price_lemons = 15
price_lemonade = 50
price_sugar = 5
production_lemonade = 5

# Command handler
@dp.message(Command("start"))
async def command_start_handler(mes):
    await mes.answer("Здорово")
    
@dp.message(Command("buy_lemon"))
async def buy_lemon(mes):
    global lemons
    lemons += 1
    await mes.answer('Вы получили лимон. Всего лимонов:' + str(lemons))

@dp.message(Command("buy_sugar"))
async def buy_sugar(mes):
    global sugar
    sugar += 100
    await mes.answer('Вы получили 100 грамм сахара. Всего грамм сахара:' + str(sugar))

@dp.message(Command("make_lemonade"))
async def buy_sugar(mes):
    global lemonade
    lemonade += 1
    await mes.answer('Вы сделали 1 бутылку лимонада. Всего бутылок лимонада:' + str(lemonade))
    
# Run the bot
async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

asyncio.run(main())          


