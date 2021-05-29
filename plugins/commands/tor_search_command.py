import html

from pyrogram import Client, filters
from pyrogram.types import Message
from helpers.torrent import get_torrent_buttons


@Client.on_message(filters.text & filters.private)
async def search_torrent_text(c: Client, m: Message):
    if m.via_bot is not None:
        return
    status = await m.reply_text("ꜱᴇᴀʀᴄʜɪɴɢ ʏᴏᴜʀ ᴛᴏʀʀᴇɴᴛ ꜰɪʟᴇ\n\n<b><a href='https://t.me/coderzHex'>©ᴄᴏᴅᴇʀᴢʜᴇx</a></b>", reply_to_message_id=m.message_id) 
    markup = await get_torrent_buttons(m, status)
    if markup is None:
        return
    search_text = f"ɢᴏᴛ ᴛʜᴇ ꜰᴏʟʟᴏᴡɪɴɢ ʀᴇꜱᴜʟ ꜰᴏʀ ʏᴏᴜʀ Qᴜᴇʀʏ <b>{html.escape(m.text)}</b>."\
                  "\nꜱᴇʟᴇᴄᴛ ᴛʜᴇ ᴘʀᴇꜰᴇʀʀᴇᴅ ᴛʏᴘᴇ ꜰʀᴏᴍ ᴛʜᴇ ʙᴇʟᴏᴡ ᴏᴘᴛɪᴏɴꜱ\n\n<b><a href='https://t.me/coderzHex'>©ᴄᴏᴅᴇʀᴢʜᴇx</a></b>"
    await status.edit(search_text, reply_markup=markup)
