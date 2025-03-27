import asyncio
import google.generativeai as genai
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command

# API Tokenlar
TOKEN = "7248324427:AAHEqXfWo9zimVCA-C4Q8KCTekvBuBM4HV0"
GEMINI_API_KEY = "AIzaSyCccyK4vrlNiGjDTJD5QV8md7u4BRb_g0k"
CREATOR_NAME = "AbbosbekAI"

# Bot va AI sozlamalari
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Gemini AI sozlash
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro-latest")  # TO'G'RI MODEL NOMI

@dp.message(Command("start"))
async def welcome(message: Message):
    await message.answer("👋 Salom! Men Gemini AI botman. Menga savol ber!")

@dp.message()
async def gemini_reply(message: Message):
    try:
        response = model.generate_content(message.text)  # Foydalanuvchi matniga javob olish
        await message.answer(response.text)  # Javobni yuborish
    except Exception as e:
        await message.answer("Haddan tashqari ko‘p so‘rov yuborildi. Biroz kuting va qayta urinib ko‘ring.")
        await asyncio.sleep(60)  # 1 daqiqa kutish
        print(f"Xato: {e}")  # Terminalda xatolikni chiqarish

@dp.message(lambda message: "kim yarat" in message.text.lower())
async def creator_info(message: types.Message):
    await message.answer(
        f"Men {CREATOR_NAME} tomonidan ishlab chiqilganman! 🤖\n"
        "Yana savollaringiz bo‘lsa, bemalol so‘rashingiz mumkin!"
    )       

# Asinxron botni ishga tushirish
async def main():
    try:
        print("Bot ishga tushdi...")
        await dp.start_polling(bot)
    except asyncio.CancelledError:
        print("Polling bekor qilindi!")
    except KeyboardInterrupt:
        print("Bot to‘xtatildi!")
    finally:
        print("Bot yopildi.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Dastur majburan to‘xtatildi!")
