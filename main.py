# Fully Corrected main.py for Render Deployment (BOT mode only)

from telethon import TelegramClient, events, Button
from configs import Config
import asyncio
import urllib.parse
from telethon.errors import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
from plugins.tgraph import *
from helpers import *

# Start bot client ONLY (No user session)
tbot = TelegramClient(
    Config.BOT_SESSION_NAME,
    Config.API_ID,
    Config.API_HASH
).start(bot_token=Config.BOT_TOKEN)

print()
print("-------------------- Initializing Telegram Bot --------------------")
print()

# ---------------------------- Force Sub -----------------------------

async def get_user_join(id):
    if Config.FORCE_SUB == "False":
        return True

    try:
        await tbot(GetParticipantRequest(
            channel=int(Config.UPDATES_CHANNEL),
            participant=id
        ))
        return True
    except UserNotParticipantError:
        return False


# -------------------------- Message Handler --------------------------

@tbot.on(events.NewMessage(incoming=True))
async def message_handler(event):

    if event.message.post:
        return

    if event.text.startswith("/"):
        return

    # Force Sub
    if not await get_user_join(event.sender_id):
        haha = await event.reply(
            f"**Hey {event.sender.first_name} 😃**\n\n"
            f"**You must join our update channel to use me!**",
            buttons=Button.url(
                "🍿 Updates Channel 🍿",
                f"https://t.me/{Config.UPDATES_CHANNEL_USERNAME}"
            )
        )
        await asyncio.sleep(Config.AUTO_DELETE_TIME)
        return await haha.delete()

    query = event.text.strip()
    if not query:
        return

    txt = await event.reply(f"**Searching for `{query}` 🔍**")

    try:
        search = []

        # Search using BOT instead of USER client
        async for word in AsyncIter(query.split()):
            msgs = tbot.iter_messages(
                Config.CHANNEL_ID,
                limit=5,
                search=word
            )
            search.append(msgs)

        username = Config.UPDATES_CHANNEL_USERNAME
        answer = f"**Join** [@{username}](https://telegram.me/{username})\n\n"

        c = 0

        # Extract results
        async for msg_list in AsyncIter(search):
            async for msg in msg_list:
                c += 1
                f_text = msg.text.replace("*", "")
                f_text = await link_to_hyperlink(f_text)

                answer += (
                    f"\n\n**✅ PAGE {c}:**\n\n━━━━━━━━━\n\n" +
                    f_text.split("\n", 1)[0] +
                    "\n\n" +
                    f_text.split("\n", 1)[-1]
                )

        if c <= 0:
            await txt.delete()
            res = await event.reply(
                f"**No results found for `{query}`**",
                buttons=[[Button.url(
                    "Check on Google 🔍",
                    f"http://google.com/search?q={query.replace(' ', '%20')}"
                )]],
                link_preview=False
            )
            await asyncio.sleep(Config.AUTO_DELETE_TIME)
            return await res.delete()

        # Telegraph Page
        answer += f"\n\n**Uploaded By @{username}**"
        answer = await replace_username(answer)
        html_page = await markdown_to_html(answer)
        html_page = await make_bold(html_page)

        tgraph_link = await telegraph_handler(
            html=html_page,
            title=query,
            author=Config.BOT_USERNAME
        )

        final_msg = (
            f"**Click Here 👇 For `{query}`**\n\n"
            f"[🍿🎬 {query.upper()}]\n({tgraph_link})"
        )

        await txt.delete()
        res = await event.reply(
            final_msg,
            buttons=[[Button.url("❓How To Open❓", "https://t.me/iP_Update/8")]],
            link_preview=False
        )
        await asyncio.sleep(Config.AUTO_DELETE_TIME)
        await event.delete()
        return await res.delete()

    except Exception as e:
        print("Error:", e)
        await txt.delete()
        res = await event.reply("**Error while searching!**")
        await asyncio.sleep(Config.AUTO_DELETE_TIME)
        await event.delete()
        return await res.delete()


# -------------------------- Start Bot --------------------------

print("Bot Started Successfully!")
print()
print(f"Join @{Config.UPDATES_CHANNEL_USERNAME}")

tbot.run_until_disconnected()
# Fully Corrected main.py for Render Deployment (BOT mode only)

from telethon import TelegramClient, events, Button
from configs import Config
import asyncio
import urllib.parse
from telethon.errors import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
from plugins.tgraph import *
from helpers import *

# Start bot client ONLY (No user session)
tbot = TelegramClient(
    Config.BOT_SESSION_NAME,
    Config.API_ID,
    Config.API_HASH
).start(bot_token=Config.BOT_TOKEN)

print()
print("-------------------- Initializing Telegram Bot --------------------")
print()

# ---------------------------- Force Sub -----------------------------

async def get_user_join(id):
    if Config.FORCE_SUB == "False":
        return True

    try:
        await tbot(GetParticipantRequest(
            channel=int(Config.UPDATES_CHANNEL),
            participant=id
        ))
        return True
    except UserNotParticipantError:
        return False


# -------------------------- Message Handler --------------------------

@tbot.on(events.NewMessage(incoming=True))
async def message_handler(event):

    if event.message.post:
        return

    if event.text.startswith("/"):
        return

    # Force Sub
    if not await get_user_join(event.sender_id):
        haha = await event.reply(
            f"**Hey {event.sender.first_name} 😃**\n\n"
            f"**You must join our update channel to use me!**",
            buttons=Button.url(
                "🍿 Updates Channel 🍿",
                f"https://t.me/{Config.UPDATES_CHANNEL_USERNAME}"
            )
        )
        await asyncio.sleep(Config.AUTO_DELETE_TIME)
        return await haha.delete()

    query = event.text.strip()
    if not query:
        return

    txt = await event.reply(f"**Searching for `{query}` 🔍**")

    try:
        search = []

        # Search using BOT instead of USER client
        async for word in AsyncIter(query.split()):
            msgs = tbot.iter_messages(
                Config.CHANNEL_ID,
                limit=5,
                search=word
            )
            search.append(msgs)

        username = Config.UPDATES_CHANNEL_USERNAME
        answer = f"**Join** [@{username}](https://telegram.me/{username})\n\n"

        c = 0

        # Extract results
        async for msg_list in AsyncIter(search):
            async for msg in msg_list:
                c += 1
                f_text = msg.text.replace("*", "")
                f_text = await link_to_hyperlink(f_text)

                answer += (
                    f"\n\n**✅ PAGE {c}:**\n\n━━━━━━━━━\n\n" +
                    f_text.split("\n", 1)[0] +
                    "\n\n" +
                    f_text.split("\n", 1)[-1]
                )

        if c <= 0:
            await txt.delete()
            res = await event.reply(
                f"**No results found for `{query}`**",
                buttons=[[Button.url(
                    "Check on Google 🔍",
                    f"http://google.com/search?q={query.replace(' ', '%20')}"
                )]],
                link_preview=False
            )
            await asyncio.sleep(Config.AUTO_DELETE_TIME)
            return await res.delete()

        # Telegraph Page
        answer += f"\n\n**Uploaded By @{username}**"
        answer = await replace_username(answer)
        html_page = await markdown_to_html(answer)
        html_page = await make_bold(html_page)

        tgraph_link = await telegraph_handler(
            html=html_page,
            title=query,
            author=Config.BOT_USERNAME
        )

        final_msg = (
            f"**Click Here 👇 For `{query}`**\n\n"
            f"[🍿🎬 {query.upper()}]\n({tgraph_link})"
        )

        await txt.delete()
        res = await event.reply(
            final_msg,
            buttons=[[Button.url("❓How To Open❓", "https://t.me/iP_Update/8")]],
            link_preview=False
        )
        await asyncio.sleep(Config.AUTO_DELETE_TIME)
        await event.delete()
        return await res.delete()

    except Exception as e:
        print("Error:", e)
        await txt.delete()
        res = await event.reply("**Error while searching!**")
        await asyncio.sleep(Config.AUTO_DELETE_TIME)
        await event.delete()
        return await res.delete()


# -------------------------- Start Bot --------------------------

print("Bot Started Successfully!")
print()
print(f"Join @{Config.UPDATES_CHANNEL_USERNAME}")

tbot.run_until_disconnected()
            # Telegraph Page
        answer += f"\n\n**Uploaded By @{username}**"
        answer = await replace_username(answer)
        html_page = await markdown_to_html(answer)
        html_page = await make_bold(html_page)

        tgraph_link = await telegraph_handler(
            html=html_page,
            title=query,
            author=Config.BOT_USERNAME
        )

        final_msg = (
            f"**Click Here 👇 For `{query}`**\n\n"
            f"[🍿🎬 {query.upper()}]\n({tgraph_link})"
        )

        await txt.delete()
        res = await event.reply(
            final_msg,
            buttons=[[Button.url("❓How To Open❓", "https://t.me/iP_Update/8")]],
            link_preview=False
        )
        await asyncio.sleep(Config.AUTO_DELETE_TIME)
        await event.delete()
        return await res.delete()

    except Exception as e:
        print("Error:", e)
        await txt.delete()
        res = await event.reply("**Error while searching!**")
        await asyncio.sleep(Config.AUTO_DELETE_TIME)
        await event.delete()
        return await res.delete()


# -------------------------- Start Bot --------------------------

print("Bot Started Successfully!")
print()# Fully Corrected main.py for Render Deployment (BOT mode only)

from telethon import TelegramClient, events, Button
from configs import Config
import asyncio
import urllib.parse
from telethon.errors import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
from plugins.tgraph import *
from helpers import *

# Start bot client ONLY (No user session)
tbot = TelegramClient(
    Config.BOT_SESSION_NAME,
    Config.API_ID,
    Config.API_HASH
).start(bot_token=Config.BOT_TOKEN)

print()
print("-------------------- Initializing Telegram Bot --------------------")
print()

# ---------------------------- Force Sub -----------------------------

async def get_user_join(id):
    if Config.FORCE_SUB == "False":
        return True

    try:
        await tbot(GetParticipantRequest(
            channel=int(Config.UPDATES_CHANNEL),
            participant=id
        ))
        return True
    except UserNotParticipantError:
        return False


# -------------------------- Message Handler --------------------------

@tbot.on(events.NewMessage(incoming=True))
async def message_handler(event):

    if event.message.post:
        return

    if event.text.startswith("/"):
        return

    # Force Sub
    if not await get_user_join(event.sender_id):
        haha = await event.reply(
            f"**Hey {event.sender.first_name} 😃**\n\n"
            f"**You must join our update channel to use me!**",
            buttons=Button.url(
                "🍿 Updates Channel 🍿",
                f"https://t.me/{Config.UPDATES_CHANNEL_USERNAME}"
            )
        )
        await asyncio.sleep(Config.AUTO_DELETE_TIME)
        return await haha.delete()

    query = event.text.strip()
    if not query:
        return

    txt = await event.reply(f"**Searching for `{query}` 🔍**")

    try:
        search = []

        # Search using BOT instead of USER client
        async for word in AsyncIter(query.split()):
            msgs = tbot.iter_messages(
                Config.CHANNEL_ID,
                limit=5,
                search=word
            )
            search.append(msgs)

        username = Config.UPDATES_CHANNEL_USERNAME
        answer = f"**Join** [@{username}](https://telegram.me/{username})\n\n"

        c = 0

        # Extract results
        async for msg_list in AsyncIter(search):
            async for msg in msg_list:
                c += 1
                f_text = msg.text.replace("*", "")
                f_text = await link_to_hyperlink(f_text)

                answer += (
                    f"\n\n**✅ PAGE {c}:**\n\n━━━━━━━━━\n\n" +
                    f_text.split("\n", 1)[0] +
                    "\n\n" +
                    f_text.split("\n", 1)[-1]
                )

        if c <= 0:
            await txt.delete()
            res = await event.reply(
                f"**No results found for `{query}`**",
                buttons=[[Button.url(
                    "Check on Google 🔍",
                    f"http://google.com/search?q={query.replace(' ', '%20')}"
                )]],
                link_preview=False
            )
            await asyncio.sleep(Config.AUTO_DELETE_TIME)
            return await res.delete()

        # Telegraph Page
        answer += f"\n\n**Uploaded By @{username}**"
        answer = await replace_username(answer)
        html_page = await markdown_to_html(answer)
        html_page = await make_bold(html_page)

        tgraph_link = await telegraph_handler(
            html=html_page,
            title=query,
            author=Config.BOT_USERNAME
        )

        final_msg = (
            f"**Click Here 👇 For `{query}`**\n\n"
            f"[🍿🎬 {query.upper()}]\n({tgraph_link})"
        )

        await txt.delete()
        res = await event.reply(
            final_msg,
            buttons=[[Button.url("❓How To Open❓", "https://t.me/iP_Update/8")]],
            link_preview=False
        )
        await asyncio.sleep(Config.AUTO_DELETE_TIME)
        await event.delete()
        return await res.delete()

    except Exception as e:
        print("Error:", e)
        await txt.delete()
        res = await event.reply("**Error while searching!**")
        await asyncio.sleep(Config.AUTO_DELETE_TIME)
        await event.delete()
        return await res.delete()


# -------------------------- Start Bot --------------------------

print("Bot Started Successfully!")
print()
print(f"Join @{Config.UPDATES_CHANNEL_USERNAME}")

tbot.run_until_disconnected()

print(f"Join @{Config.UPDATES_CHANNEL_USERNAME}")

tbot.run_until_disconnected()
