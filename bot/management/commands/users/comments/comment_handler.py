from aiogram.dispatcher.storage import FSMContext
from aiogram.types import Message
from bot.management.commands.loader import dp
from asyncio import create_task
from asgiref.sync import sync_to_async

from bot.models import User
from ...state import Comments
from ...utils import texts, buttons


async def set_commit_task(message: Message, state: FSMContext):
    user_id = message.from_user.id

    try:
        user = await sync_to_async(User.objects.get)(user_id=user_id)
    except:
        raise Exception("User topilmadi")

    if (user.lang == "uz"):
        await message.answer(texts.comment_name_uz, reply_markup=buttons.BACK_UZ)
    elif (user.lang == "cr"):
        await message.answer(texts.comment_name_cr, reply_markup=buttons.BACK_CR)
    elif (user.lang == "ru"):
        await message.answer(texts.comment_name_ru, reply_markup=buttons.BACK_RU)

    await Comments.name.set()

@dp.message_handler(
        lambda message: message.text.startswith(buttons.FIKR_BUTTON_UZ) or \
                message.text.startswith(buttons.FIKR_BUTTON_CR) or \
                    message.text.startswith(buttons.FIKR_BUTTON_RU)
        )
async def func(message: Message, state: FSMContext):
    await create_task(set_commit_task(message, state))

