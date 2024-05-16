from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from ...loader import dp, bot
from asgiref.sync import sync_to_async
from bot.models import User
from ...utils import buttons
from ...utils import texts
from ...state import Comments
from asyncio import create_task



async def set_name_task(message: Message, state: FSMContext):
    name = message.text
    await state.set_data(
        {
            'name': name,
        }
    )
    user_id = message.from_user.id

    try:
        user = await sync_to_async(User.objects.get)(user_id=user_id)
    except:
        raise Exception("User topilmadi")

    if (user.lang == "uz"):
        await message.answer(texts.comment_uz)
    elif (user.lang == "cr"):
        await message.answer(texts.comment_cr)
    elif (user.lang == "ru"):
        await message.answer(texts.comment_ru)

    await state.set_state(Comments.comment)


@dp.message_handler(content_types=['text'], state=Comments.name)
async def func(message: Message, state: FSMContext):
    await create_task(set_name_task(message, state))