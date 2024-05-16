import re
import time
import logging
from datetime import datetime, timedelta
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from config import DELAY, WAKTU, API_ID, API_HASH, STRING, MESSAGE_LINK

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
)
logger = logging.getLogger("Qwerty")

session = StringSession(str(STRING))
client = TelegramClient(
        session=session,
        api_id=API_ID,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
        device_model="@Qwertystore",
)

async def forward_message(client, message_link, to_chats):
    # Ekstrak informasi dari link pesan
    match = re.match(r'https://t.me/([^/]+)/(\d+)', message_link)
    if not match:
        logger.error("Link pesan tidak valid")
        return
    from_channel = match.group(1)
    message_id = int(match.group(2))

    async with client:
        # Ambil pesan dari channel berdasarkan ID
        message = await client.get_messages(from_channel, ids=message_id)
        if not message:
            logger.error("Pesan tidak ditemukan")
            return

        # Teruskan pesan ke semua grup tujuan
        for chat_id in to_chats:
            try:
                await client.forward_messages(chat_id, message)
                logger.info(f"Pesan diteruskan ke {chat_id}")
                # Tunggu sejenak sebelum mengirim ke grup berikutnya (optional)
                time.sleep(1.5)
            except Exception as e:
                logger.error(f"Gagal meneruskan pesan ke {chat_id}: {e}")

async def main():
    message_link = MESSAGE_LINK
    delay = DELAY
    waktu = WAKTU
    to_chats = ['@Lpm_upsubsupfoll', '@LPM_Roleplayers', '@lpm_roleplay', '@LPM_RPP', '@LPM_BAGI2', '@LPM_Roleplayer_2']
    end_time = datetime.now() + timedelta(hours=waktu)
    while datetime.now() < end_time:
        await forward_message(client, message_link, to_chats)
        logger.info(f"Menunggu {delay} detik sebelum siklus berikutnya...")
        time.sleep(delay)

# Jalankan client
with client:
    client.loop.run_until_complete(main())
