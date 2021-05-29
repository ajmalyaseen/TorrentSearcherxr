from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton





@Client.on_message(filters.command(["start", "start@GroupMusicPlayBot"]) & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        text="Hello 👋🏻 {}!\n\n𝐈 𝐚𝐦 𝐬𝐢𝐦𝐩𝐥𝐞 𝐲𝐞𝐭 𝐩𝐨𝐰𝐞𝐫𝐟𝐮𝐥 𝐛𝐨𝐭 𝐓𝐨 𝐅𝐢𝐧𝐝 𝐦𝐚𝐠𝐧𝐞𝐭 𝐥𝐢𝐧𝐤𝐬 𝐅𝐫𝐨𝐦 𝐌𝐮𝐥𝐭𝐢𝐩𝐥𝐞 𝐓𝐨𝐫𝐫𝐞𝐧𝐭 𝐒𝐢𝐭𝐞𝐬.\n\n𝘊𝘭𝘪𝘤𝘬 /help 𝘍𝘰𝘳 𝘔𝘰𝘳𝘦 𝘏𝘦𝘭𝘱 𝘖𝘯 𝘔𝘺 𝘜𝘴𝘢𝘨𝘦 ❤".format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton("📫UPDATES", url="https://t.me/CoderzHEX"),
            InlineKeyboardButton("🕵‍♂CREATOR", url="https://t.me/DIAGO_X")
            ],[
            InlineKeyboardButton("📕ABOUT", callback_data= "about"),
            InlineKeyboardButton("🔐 CLOSE", callback_data= "close")
            ]]
        ),
        disable_web_page_preview=True
    )



@Client.on_callback_query()
async def cb_handler(client, query):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b><u>About Me</u></b>\n\n• 𝐍𝐚𝐦𝐞 : ᴛᴏʀʀᴇɴᴛ ᴅʟ \n\n• 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞 : ᴘᴀʏᴛᴏɴ \n\n• 𝐋𝐢𝐛𝐫𝐚𝐫𝐲 : ᴘʏʀᴏɢʀᴀᴍ \n\n• 𝐒𝐞𝐫𝐯𝐞𝐫 :  ʜᴇʀᴏᴋᴜ \n\n• 𝐒𝐭𝐚𝐭𝐮𝐬 :  V 1.0 \n\n• 𝐂𝐫𝐞𝐚𝐭𝐨𝐫 : <b><a href='https://t.me/diago_x'>ᴅɪᴀɢᴏ</a></b>\n\n<b>ᴜᴘᴅᴀᴛᴇᴅ ᴏɴ 30-5-21 ɪɴᴅɪᴀɴ ᴛɪᴍᴇ 10:00 ᴀᴍ</b>\n\n<b><a href='https://t.me/coderzHex'>©ᴄᴏᴅᴇʀᴢʜᴇx</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔐CLOSE", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass


@Client.on_message(filters.command(["start", "start@GroupMusicPlayBot"]) & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text(
          text="**Music Bot Is Online ✅**",
          reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(text="🎙️ Support Group 🎙️", url="https://t.me/MusicBotSupports")
              ]]
          )
      )


@Client.on_message(filters.command(["help", "start@GroupMusicPlayBot"]) & filters.private & ~filters.channel)
async def help(_, message: Message):
    await message.reply_text(
        text="""𝙃𝙤𝙬 𝙏𝙤 𝘿𝙤𝙬𝙣𝙡𝙤𝙖𝙙 𝙎𝙤𝙣𝙜

💡 /song 𝐒𝐨𝐧𝐠 𝐍𝐚𝐦𝐞 : ᴅᴏᴡɴʟᴏᴀᴅ ʏᴏᴜʀ ꜱᴏɴɢ ᴛᴏ ᴀᴜᴅɪᴏ

💡 /vid 𝐬𝐨𝐧𝐠 𝐍𝐚𝐦𝐞 : ᴅᴏᴡɴʟᴏᴀᴅ ʏᴏᴜʀ ꜱᴏɴɢ ᴛᴏ ᴠɪᴅᴇᴏ

•𝐒𝐞𝐚𝐫𝐜𝐡 𝐬𝐨𝐧𝐠 𝐘𝐨𝐮𝐓𝐮𝐛𝐞 𝐥𝐢𝐧𝐤

💡 /search 𝐬𝐨𝐧𝐠 𝐧𝐚𝐦𝐞 : ɢᴇᴛ ʏᴏᴜʀ ꜱᴏɴɢ ʏᴏᴜᴛᴜʙᴇ ʟɪɴᴋ


@CoderzHex
 """,
        reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(text="📫UPDATES", url="https://t.me/CoderzHEX"),
              InlineKeyboardButton("🔐CLOSE", callback_data = "close")
              ]]
          )
      )
