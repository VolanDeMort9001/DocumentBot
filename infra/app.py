import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from infra.routers.router import router
import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()


async def main():
    # Включаем роутер
    dp.include_router(router)

    print("🤖 Бот запускается...")

    # Удаляем вебхук и пропускаем накопившиеся обновления
    await bot.delete_webhook(drop_pending_updates=True)

    print("✅ Вебхук удален, начинаю polling...")

    try:
        # Запускаем поллинг
        await dp.start_polling(bot)
    except Exception as e:
        print(f"❌ Ошибка при запуске бота: {e}")
    finally:
        # Закрываем сессию бота
        await bot.session.close()
        print("👋 Бот остановлен")

if __name__ == "__main__":
    asyncio.run(main())