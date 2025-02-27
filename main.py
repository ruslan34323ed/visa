import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from config import BOT_TOKEN, CHAT_ID
from bot import router
from parser import fetch_latest_news

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()

last_news_title = None  # Переменная для хранения последней новости

async def check_news():
    """
    Проверяет новости на сайте каждые 30 минут.
    Если появляется новая запись, отправляет уведомление.
    """
    global last_news_title
    while True:
        news = fetch_latest_news()
        if news:
            news_date, news_title, news_content = news
            if news_title != last_news_title:  # Проверяем, чтобы новость не повторялась
                await bot.send_message(CHAT_ID, f"<b>{news_date}</b>\n\n<b>{news_title}</b>\n\n{news_content}")
                last_news_title = news_title  # Обновляем последнюю новость
        await asyncio.sleep(1800)  # Проверяем каждые 30 минут

async def main():
    """
    Запускает бота и фоновый процесс проверки новостей.
    """
    dp.include_router(router)  # Подключаем обработчики команд
    asyncio.create_task(check_news())  # Запускаем проверку новостей в фоне
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())