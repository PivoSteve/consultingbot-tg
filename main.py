import asyncio
import logging
import os
import sys
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from datetime import datetime
from modules.handlers.start import start_router
if os.name == 'nt':
    logging.info('Using WIN system base')
    TOKEN_FILE_PATH = 'C:/2501/telegram_bot/data_consulting/TOKEN' ## MARK: CHANGE TOKEN PATH 
else:
    logging.info('Using UNIX system base')
    TOKEN_FILE_PATH = '/home/syra/2501/tg_bots/consultingbot/TOKEN'

def read_token_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            token = file.read().strip()
            return token
    except Exception as e:
        raise ValueError(f"Error reading token from file: {e}")

TOKEN = read_token_from_file(TOKEN_FILE_PATH)
if not TOKEN:
    raise ValueError("No BOT_TOKEN found in the token file. Please check your token.")

async def main() -> None:
    dp = Dispatcher()
    dp.include_routers(
        start_router,
    )

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

log_filename = f'./logs/{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log'

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s]:%(levelname)s:%(funcName)s:%(message)s',
        datefmt='%Y-%m-%d|%H:%M:%S',
        handlers=[
            logging.FileHandler(log_filename, mode='a', encoding='utf-8'),
            logging.StreamHandler(sys.stdout)
        ]
    )
    asyncio.run(main())
