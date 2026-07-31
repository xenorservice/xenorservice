from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

TOKEN = "8934536522:AAH_ZZnrs8cAJVBG5mcRL5KR2lBdBhpOhQY"

bot = Bot(token=TOKEN)
dp = Dispatcher()

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📁 Buyurtma berish")],
        [
            KeyboardButton(text="📊 Buyurtmalar"),
            KeyboardButton(text="💵 Mening hisobim")
        ],
        [
            KeyboardButton(text="🗣 Referal tizimi"),
            KeyboardButton(text="💰 Hisob to'ldirish")
        ],
        [
            KeyboardButton(text="☎️ Murojaat"),
            KeyboardButton(text="📚 Qo'llanma")
        ]
    ],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        "👋 Assalomu alaykum!\nXush kelibsiz!",
        reply_markup=menu
    )

@dp.message(lambda m: m.text == "📁 Buyurtma berish")
async def buyurtma(message: types.Message):
    await message.answer("📁 Buyurtma berish bo'limiga xush kelibsiz!")

@dp.message(lambda m: m.text == "📊 Buyurtmalar")
async def buyurtmalar(message: types.Message):
    await message.answer("📊 Sizda hozircha buyurtmalar yo'q.")

@dp.message(lambda m: m.text == "💵 Mening hisobim")
async def hisob(message: types.Message):
    await message.answer("💵 Balansingiz: 0 so'm")

@dp.message(lambda m: m.text == "🗣 Referal tizimi")
async def referal(message: types.Message):
    await message.answer(
        f"🗣 Referal havolangiz:\nhttps://t.me/{(await bot.get_me()).username}?start={message.from_user.id}"
    )

@dp.message(lambda m: m.text == "💰 Hisob to'ldirish")
async def toldirish(message: types.Message):
    await message.answer("💰 Hisobni to'ldirish uchun admin bilan bog'laning.")

@dp.message(lambda m: m.text == "☎️ Murojaat")
async def murojaat(message: types.Message):
    await message.answer("☎️ Admin: @esen_best")

@dp.message(lambda m: m.text == "📚 Qo'llanma")
async def qollanma(message: types.Message):
    await message.answer(
        "📚 Qo'llanma\n\n"
        "1. Buyurtma bering.\n"
        "2. To'lovni amalga oshiring.\n"
        "3. Buyurtmangiz bajariladi."
    )

async def main():
    await dp.start_polling(bot)

asyncio.run(main())
