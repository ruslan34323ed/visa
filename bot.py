from aiogram import Router, types
from aiogram.filters import Command
from parser import fetch_latest_news

router = Router()  # Создаем роутер для обработки команд

@router.message(Command("start"))
async def start_command(message: types.Message):
    """
    Обрабатывает команду /start. Отправляет приветственное сообщение.
    """
    await message.answer("Привет! Я буду уведомлять тебя о новых записях на TLScontact.")

@router.message(Command("news"))
async def send_latest_news(message: types.Message):
    """
    Обрабатывает команду /news. Отправляет последнюю новость, если она есть.
    """
    news = fetch_latest_news()
    if news:
        news_date, news_title, news_content = news
        await message.answer(f"<b>{news_date}</b>\n\n<b>{news_title}</b>\n\n{news_content}", parse_mode="HTML")
    else:
        await message.answer("Не удалось получить новости 😕")
