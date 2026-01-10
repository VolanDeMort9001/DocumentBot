import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import os
from dotenv import load_dotenv
from infra.routers.router import router

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

def run_bot():
    dp.include_router(router)
    bot.delete_webhook(drop_pending_updates=True)
    try:
        dp.start_polling(bot)
    finally:
        bot.session.close()

if __name__ == "__main__":
    run_bot()