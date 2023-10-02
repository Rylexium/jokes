import argparse
import asyncio

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
    return msg.rstrip('\n').rstrip('\n')


def parse_arguments():
    parser = argparse.ArgumentParser(description='',
                                     usage='use "python %(prog)s --help" for more information',
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("-m", "--msg", required=False, help="Error message", default=None)
    parser.add_argument("-s", "--source", required=False, help="Source (creds of host)", default=None)
    parser.add_argument("-f", "--folder", required=False, help="What is backup", default=None)
    parser.add_argument("-lb", "--localbackup", required=False, help="Path to local backup where save archive", default=None)
    parser.add_argument("-rb", "--remotebackup", required=False, help="Path to remote backup where save archive", default=None)
    parser.add_argument("-l", "--log", required=False, help="Path to backupScript log", default=None)

    return parser.parse_args()


args = parse_arguments()


#"архивации данных" "отправки архива на файловый сервер"
#python .\main.py --msg "архивация данных" --log '.\backupScript (8).log' --source "soc-siemcore(172.17.250.66)" --folder "\\172.17.250.10\soc-files" --localbackup "\\172.17.250.66\C$\backup(172.17.250.10)" --remotebackup '\\172.17.250.10\soc-files\backup'
send_message(edit_pattern(msg=args.msg, source=args.source, folder=args.folder,
                          local_backup=args.localbackup, remote_backup=args.remotebackup), args.log)