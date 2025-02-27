import os
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные окружения

CHAT_ID = -1002371597215
URL = "https://it.tlscontact.com/by/msq/page.php?pid=news"

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не найден! Проверьте .env файл.")
