from application.bot import bot
from aiogram import types

from datetime import datetime, timedelta
from application.database.db import db


async def url_is_find(message) -> None:
    """
    Function is delete message and restrict chat member.
    :param message: message info from telegram
    :return: None
    """
    reason = "Adverting"

    await message.delete()
    db.add_note(
        chat_id=message.chat.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        from_user_id=message.from_user.id,
        message=message.text,
        reason=reason,
    )

    warns = db.response_to_check_warns(message.chat.id, message.from_user.id)
    answer_message = f"{message.from_user.first_name} ({message.from_user.id}) have {warns} warns. Reason: {reason}"

    if warns >= 3:
        answer_message = f"{message.from_user.first_name} ({message.from_user.id}) have {warns} warns. Reason: {reason}"
        await bot.restrict_chat_member(
            message.chat.id,
            message.from_user.id,
            types.ChatPermissions(
                can_send_messages=False,
                can_send_audios=False,
                can_send_documents=False,
                can_send_photos=False,
                can_send_videos=False,
                can_send_video_notes=False,
                can_send_voice_notes=False,
                can_send_polls=False,
                can_send_other_messages=False,
                can_add_web_page_previews=False,
                can_change_info=False,
                can_invite_users=False,
                can_pin_messages=False,
                can_manage_topics=False,
            ),
            until_date=datetime.now() + timedelta(days=3),
        )
    await message.answer(answer_message)
