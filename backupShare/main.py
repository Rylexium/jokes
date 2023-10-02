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


def wrapper(key, item):
    if item is not None:
        return f"<b>{key}</b>: <code>{item}</code>\n"
    return ""


def edit_pattern(msg, source=None, folder=None, local_backup=None, remote_backup=None):
    msg = "<b>Backup</b>\n" \
           f"🛑 Произошла ошибка во время: <b><i>{msg}</i></b>.\n\n"
    msg += wrapper("source", source)
    msg += wrapper("folder", folder)
    msg += wrapper("localBackup", local_backup)
    msg += wrapper("remoteBackup", remote_backup)
    return msg.rstrip('\n')


#"архивации данных" "отправки архива на файловый сервер"
send_message(edit_pattern(msg=sys.argv[1], source=sys.argv[3], folder=sys.argv[4],
                          local_backup=sys.argv[5], remote_backup=sys.argv[6]), sys.argv[2])

#start:
# python .\main.py "архивация данных" '.\backupScript (8).log' "soc-siemcore(172.17.250.66)" "\\172.17.250.10\soc-files" "\\172.17.250.66\C$\backup(172.17.250.10)" "\\172.17.250.10\soc-files\backup"
