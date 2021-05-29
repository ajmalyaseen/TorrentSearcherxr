import html

from pyrogram import Client, filters
from pyrogram.types import Message
from helpers.torrent import get_torrent_buttons


@Client.on_message(filters.command('search') & ~filters.channel)
def search(client, message):
    if m.via_bot is not None:
        return
    status = await m.reply_text("Searching your torrent file", reply_to_message_id=m.message_id)
    markup = await get_torrent_buttons(m, status)
    if markup is None:
        return
    search_text = f"Got the following results for your query <b>{html.escape(m.text)}</b>."\
                  "\nSelect the preferred type from the below options"
    await status.edit(search_text, reply_markup=markup)
