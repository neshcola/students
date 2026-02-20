from aiogram import Bot, Dispatcher                     
from aiogram.filters import Command
from aiogram.types import Message
import asyncio

TOKEN = "8516795655:AAHfSA9wS3pf4GcOAFxD052HCBMZKrtdIBE"

dp = Dispatcher()

# Command handler
@dp.message(Command("inventory"))
async def inventory(mes):
    global users
    await mes.answer(f'{lemons} лимонов.\n{sugar} грамм сахара.\n{lemonade} бутылок лимонада.\n{money} денег')
users = {}

@dp.message(Command("start"))
async def command_start_handler(mes):
    global users
    x = mes.chat.id
    if x in users.keys():
        await mes.answer("Привет! покупай ингредиенты, делай лимонад и зарабатывай!")
    else:
        users[x] = {'Деньги':50,'Лимоны':0,'Сахар':0,'Лимонад':0} 
        await mes.answer('Пользователь создан')


@dp.message(Command("buy_lemon"))
async def buy_lemon(mes):
    global users
    x = mes.chat.id
    if users[x]['Деньги'] >= 10:
        users[x]['Деньги'] -= 10
        users[x]['Лимоны'] += 1
        await mes.answer(f'Вы купили Лимон! Всего Лимонов: {users[x]['Лимоны']}. Осталось денег: {users[x]['Деньги']}')
    else:
        await mes.answer(f'Недостаточно денег. Всего денег: {users[x]['Деньги']}')

@dp.message(Command("buy_sugar"))
async def buy_sugar(mes):
    global users
    if users[x]['Деньги']>=5:
        users[x]['Сахар'] += 100
        users[x]['Деньги'] -= 5
        await mes.answer(f'Вы получили 100 грамм сахара.\n Всего грамм сахара:{users[x]['Сахар']}')
    else:
        await mes.answer(f'недостаточно денег.\n Всего :{users[x]['Деньги']}рублей')


@dp.message(Command("make_lemonade"))
async def make_lemonade(mes):
    global users
    if users[x]['Лимоны']>=2 and users[x]['Сахар']>=100:
        users[x]['Лимонад'] += 1
        users[x]['Лимоны'] -= 2
        users[x]['Сахар'] -= 100
        await mes.answer(f'Вы сделали 1 бутылку лимонада.\n Всего бутылок лимонада:{users[x]['Лимонад']}\nОсталось:{users[x]['Лимоны']} лимонов и {users[x]['Сахар']} грамм сахара')
    else:
        await mes.answer('недостаточно лимонов и сахара. Всего :' + str(lemons) + 'лимонов и' + str(sugar) + 'грамм сахара')



# Run the bot
async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

asyncio.run(main())          





