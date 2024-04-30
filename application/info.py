from application.database.db import db


async def post_info(message):
    if message.chat.type != "private":
        server_name = message.chat.title
        count_of_messages = message.message_id
        all_warns = db.all_warns(message.chat.id)

        await message.answer(
            f"{server_name}\n\nCount messages: {count_of_messages}\nCount of warns: {all_warns}"
        )
