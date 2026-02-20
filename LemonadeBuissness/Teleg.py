import asyncio
import json
import os
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8516795655:AAHfSA9wS3pf4GcOAFxD052HCBMZKrtdIBE"
DATA_FILE = "users.json"

dp = Dispatcher()
users = {}

# --- Работа с данными ---
def load_data():
    global users
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            users = json.load(f)

def save_data():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=4)

load_data()

# --- Клавиатура ---
def get_main_kb():
    kb = [
        [KeyboardButton(text="/buy_lemon"), KeyboardButton(text="/buy_sugar")],
        [KeyboardButton(text="/make_lemonade"), KeyboardButton(text="/stats")]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

# --- Обработчики ---
@dp.message(Command("start"))
async def start(mes: Message):
    uid = str(mes.chat.id)
    if uid not in users:
        # Добавили опыт (lvl) и счетчик приготовлений для защиты новичка
        users[uid] = {'Деньги': 50, 'Лимоны': 0, 'Сахар': 0, 'Лимонад': 0, 'lvl': 1, 'total_made': 0}
        save_data()
        await mes.answer("🥤 Добро пожаловать в бизнес! Твой первый лимонад точно получится удачным.", reply_markup=get_main_kb())
    else:
        await mes.answer("С возвращением к плите!", reply_markup=get_main_kb())

@dp.message(Command("buy_lemon"))
async def buy_lemon(mes: Message):
    uid = str(mes.chat.id)
    cost = 10
    if users[uid]['Деньги'] >= cost:
        users[uid]['Деньги'] -= cost
        users[uid]['Лимоны'] += 1
        save_data()
        await mes.answer(f"🍋 Куплен лимон за {cost} руб.")
    else:
        await mes.answer("Не хватает денег на лимон!")

@dp.message(Command("buy_sugar"))
async def buy_sugar(mes: Message):
    uid = str(mes.chat.id)
    cost = 5
    if users[uid]['Деньги'] >= cost:
        users[uid]['Деньги'] -= cost
        users[uid]['Сахар'] += 100
        save_data()
        await mes.answer(f"🍬 Куплено 100г сахара за {cost} руб.")
    else:
        await mes.answer("Деньги на сахар кончились!")

@dp.message(Command("make_lemonade"))
async def make_lemonade(mes: Message):
    uid = str(mes.chat.id)
    u = users[uid]
    
    if u['Лимоны'] >= 1 and u['Сахар'] >= 100:
        u['Лимоны'] -= 1
        u['Сахар'] -= 100
        u['total_made'] += 1
        
        base_price = 30 # Базовая цена продажи
        
        # Логика порчи (15% шанс, если это не первый раз)
        is_spoiled = False
        if u['total_made'] > 1 and random.random() < 0.15:
            is_spoiled = True
        
        if is_spoiled:
            earned = int(base_price * 0.3)
            msg = f"🤢 О нет! Лимонад испортился. Удалось продать только за {earned} руб. (30% цены)"
        else:
            earned = base_price + (u['lvl'] * 5) # С каждым уровнем доход растет
            u['Лимонад'] += 1
            msg = f"🥤 Идеальный лимонад! Продан за {earned} руб. (включая бонус за уровень)"
        
        u['Деньги'] += earned
        
        # Система уровней: каждые 5 успешных лимонадов = +1 уровень
        new_lvl = (u['Лимонад'] // 5) + 1
        if new_lvl > u['lvl']:
            u['lvl'] = new_lvl
            msg += f"\n\n🆙 УРОВЕНЬ ПОВЫШЕН! Теперь твой уровень: {u['lvl']}"
            
        save_data()
        await mes.answer(msg)
    else:
        await mes.answer("Недостаточно ингредиентов! Нужно 1 лимон и 100г сахара.")

@dp.message(Command("stats"))
async def stats(mes: Message):
    uid = str(mes.chat.id)
    u = users[uid]
    await mes.answer(
        f"👤 Игрок: {mes.from_user.first_name}\n"
        f"🌟 Уровень: {u['lvl']}\n"
        f"💰 Баланс: {u['Деньги']} руб.\n"
        f"📦 Ресурсы: {u['Лимоны']}🍋, {u['Сахар']}г сахара\n"
        f"📈 Успешных продаж: {u['Лимонад']}"
    )

async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")
