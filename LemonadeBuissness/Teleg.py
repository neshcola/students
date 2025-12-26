from aiogram import Bot, Dispatcher                     
from aiogram.filters import Command
from aiogram.types import Message
import asyncio

TOKEN = "8516795655:AAHfSA9wS3pf4GcOAFxD052HCBMZKrtdIBE"

dp = Dispatcher()

lemons = 0
money = 50
lemonade = 0
sugar = 0
price_lemons = 15
price_lemonade = 60
price_sugar = 5
production_lemonade = 5

# Command handler
@dp.message(Command("start"))
async def command_start_handler(mes):
    await mes.answer("Здорово")
    
@dp.message(Command("buy_lemon"))
async def buy_lemon(mes):
    global money
    global lemons
    if money>=15:
        lemons += 1
        money -= 15
        await mes.answer('Вы получили лимон. Всего лимонов:' + str(lemons))
    else:
        await mes.answer('недостаточно денег.Всего :' + str(money) + 'рублей')
        

@dp.message(Command("buy_sugar"))
async def buy_sugar(mes):
    global money
    global sugar
    if money>=5:
        sugar += 100
        money -= 5
        await mes.answer('Вы получили 100 грамм сахара. Всего грамм сахара:' + str(sugar))
    else:
        await mes.answer('недостаточно денег.Всего :' + str(money) + 'рублей')

@dp.message(Command("make_lemonade"))
async def make_lemonade(mes):
    global lemonade
    global sugar
    global lemons
    if lemons>=2 and sugar>=100:
        lemonade += 1
        lemons -= 2
        sugar -= 100
        await mes.answer('Вы сделали 1 бутылку лимонада. Всего бутылок лимонада:' + str(lemonade))
    else:
        await mes.answer('недостаточно лимонов и сахара.Всего :' + str(lemons) + 'лимонов и' + str(sugar) + 'грамм сахара')
@dp.message(Command("inventory"))
async def inventory(mes):
    global lemonade
    global sugar
    global lemons
    await mes.answer(str(lemons) + "лимонов" +
                     str(sugar) + 'грамм сахара' +
                     str(lemonade) + 'бутылок лимонада' )
      
# Run the bot
async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

asyncio.run(main())          












