from cache.admins import admins
from driver.veez import call_py
from pyrogram import Client, filters
from driver.decorators import authorized_users_only
from driver.filters import command, other_filters
from driver.queues import QUEUE, clear_queue
from driver.utils import skip_current_song, skip_item
from config import BOT_USERNAME, GROUP_SUPPORT, IMG_3, UPDATES_CHANNEL
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)


bttn = InlineKeyboardMarkup(
    [[InlineKeyboardButton("ð Go Back", callback_data="cbmenu")]]
)


bcl = InlineKeyboardMarkup(
    [[InlineKeyboardButton("ð Close", callback_data="cls")]]
)


@Client.on_message(command(["paload", f"paload@{BOT_USERNAME}"]) & other_filters)
async def update_admin(client, message):
    global admins
    new_admins = []
    new_ads = await client.get_chat_members(message.chat.id, filter="administrators")
    for u in new_ads:
        new_admins.append(u.user.id)
    admins[message.chat.id] = new_admins
    await message.reply_text(
        "â **okay na lods**\nâ **Admin list** has been **updated !**"
    )



@Client.on_message(command(["next", f"next@{BOT_USERNAME}", "vskip"]) & other_filters)
@authorized_users_only
async def skip(client, m: Message):

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="â¢ Má´É´á´", callback_data="cbmenu"
                ),
                InlineKeyboardButton(
                    text="â¢ CÊá´sá´", callback_data="cls"
                ),
            ]
        ]
    )

    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await m.reply("â wala naman po nakaplay")
        elif op == 1:
            await m.reply("â __Queues__ is empty.\n\nâ¢ userbot leaving voice chat")
        else:
            await m.reply_photo(
                photo=f"{IMG_3}",
                caption=f"â­ **Skipped to the next track.**\n\nð· **Name:** [{op[0]}]({op[1]})\nð­ **Chat:** `{chat_id}`\nð¡ **Status:** `Playing`\nð§ **Request by:** {m.from_user.mention()}",
                reply_markup=keyboard,
            )
    else:
        skip = m.text.split(None, 1)[1]
        OP = "ð **removed song from queue:**"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x == 0:
                    pass
                else:
                    hm = await skip_item(chat_id, x)
                    if hm == 0:
                        pass
                    else:
                        OP = OP + "\n" + f"**#{x}** - {hm}"
            await m.reply(OP)


@Client.on_message(
    command(["tigil", f"tigil@{BOT_USERNAME}", "tamana", f"tamana@{BOT_USERNAME}", "tumigil"])
    & other_filters
)
@authorized_users_only
async def stop(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await m.reply("â **streaming has ended.**")
        except Exception as e:
            await m.reply(f"ð« **error:**\n\n`{e}`")
    else:
        await m.reply("â *walang nakaplay lods**")


@Client.on_message(
    command(["teka", f"teka@{BOT_USERNAME}", "tekalang"]) & other_filters
)
@authorized_users_only
async def pause(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await m.reply(
                "â¸ **Track paused.**\n\nâ¢ **To resume the stream, use the**\nÂ» /resume command."
            )
        except Exception as e:
            await m.reply(f"ð« **error:**\n\n`{e}`")
    else:
        await m.reply("â **walang nakaplay**")


@Client.on_message(
    command(["tuloy", f"tuloy@{BOT_USERNAME}", "ituloy"]) & other_filters
)
@authorized_users_only
async def resume(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await m.reply(
                "â¶ï¸ **Track resumed.**\n\nâ¢ **To pause the stream, use the**\nÂ» /pause command."
            )
        except Exception as e:
            await m.reply(f"ð« **error:**\n\n`{e}`")
    else:
        await m.reply("â **walang naka play po**")


@Client.on_message(
    command(["ingay", f"ingay@{BOT_USERNAME}", "shh", "pre"]) & other_filters
)
@authorized_users_only
async def mute(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.mute_stream(chat_id)
            await m.reply(
                "ð **uyyyy may chismis**\n\nâ¢ **teka teka baldo may chismis**"
            )
        except Exception as e:
            await m.reply(f"ð« **error:**\n\n`{e}`")
    else:
        await m.reply("â **walang nakaplay po**")


@Client.on_message(
    command(["tahimik", f"tahimik@{BOT_USERNAME}", "lods"]) & other_filters
)
@authorized_users_only
async def unmute(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.unmute_stream(chat_id)
            await m.reply(
                "ð **sure na ba? itutuloy ko na?**\n\nâ¢ **mga chismosa amputa para kang si aling cely**"
            )
        except Exception as e:
            await m.reply(f"ð« **error:**\n\n`{e}`")
    else:
        await m.reply("â **wala po nakaplay**")


@Client.on_callback_query(filters.regex("cbpause"))
async def cbpause(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("ð¡ only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await query.edit_message_text(
                "â¸ streaming has paused", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"ð« **error:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.edit_message_text("â **nothing in streaming**", reply_markup=bcl)


@Client.on_callback_query(filters.regex("cbresume"))
async def cbresume(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("ð¡ only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await query.edit_message_text(
                "â¶ï¸ streaming has resumed", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"ð« **error:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.edit_message_text("â **nothing in streaming**", reply_markup=bcl)


@Client.on_callback_query(filters.regex("cbstop"))
async def cbstop(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("ð¡ only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await query.edit_message_text("â **streaming has ended**", reply_markup=bcl)
        except Exception as e:
            await query.edit_message_text(f"ð« **error:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.edit_message_text("â **nothing in streaming**", reply_markup=bcl)


@Client.on_callback_query(filters.regex("cbmute"))
async def cbmute(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("ð¡ only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.mute_stream(chat_id)
            await query.edit_message_text(
                "ð userbot succesfully muted", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"ð« **error:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.edit_message_text("â **nothing in streaming**", reply_markup=bcl)


@Client.on_callback_query(filters.regex("cbunmute"))
async def cbunmute(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("ð¡ only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.unmute_stream(chat_id)
            await query.edit_message_text(
                "ð userbot succesfully unmuted", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"ð« **error:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.edit_message_text("â **nothing in streaming**", reply_markup=bcl)


@Client.on_message(
    command(["volume", f"volume@{BOT_USERNAME}", "vol"]) & other_filters
)
@authorized_users_only
async def change_volume(client, m: Message):
    range = m.command[1]
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.change_volume_call(chat_id, volume=int(range))
            await m.reply(
                f"â **volume set to** `{range}`%"
            )
        except Exception as e:
            await m.reply(f"ð« **error:**\n\n`{e}`")
    else:
        await m.reply("â **nothing in streaming**")
