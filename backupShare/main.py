import asyncio
import sys

import keyring
from aiogram import Bot, types

token = keyring.get_password("telegram", "api key")
chat_id = int(keyring.get_password("telegram", "test_chat_id"))  # VOLS_CHANNEL_ID #test_chat_id

bot = Bot(token=token)
loop = asyncio.get_event_loop()


def send_message(text, path_to_log, parse_mode="HTML"):
    async def _async_send_message():
        media_group = [types.InputMediaDocument(open(path_to_log, 'rb'), parse_mode=parse_mode)]
        media_group[0].caption = text.rstrip('\n')
        return await bot.send_media_group(chat_id=chat_id, media=media_group)
    loop.run_until_complete(_async_send_message())


def edit_pattern(msg):
    return "<b>Backup (soc-files)</b>\n" \
           f"🛑 Произошла ошибка во время: <b><i>{msg}</i></b>."


#"архивации данных" "отправки архива на файловый сервер"
send_message(text=edit_pattern(sys.argv[1]), path_to_log=sys.argv[2])
