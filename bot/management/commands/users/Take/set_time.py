from aiogram.dispatcher.storage import FSMContext
from aiogram.types import Message
from bot.management.commands.loader import dp, bot
from asyncio import create_task
from asgiref.sync import sync_to_async

from bot.management.commands.services.services import getBasketList
from bot.models import User
from utils.channel_id import ORDER_SEND_CHAT
from ...state import TakeAway
from ...utils import texts, buttons


async def time_task(message: Message, state: FSMContext):
    user_id = message.from_user.id

    await state.update_data(time=message.text)

    try:
        user = await sync_to_async(User.objects.get)(user_id=user_id)
    except:
        raise Exception("User topilmadi")

    data = await state.get_data()

    basket = getBasketList(user_id)
    
    # send message curier
    await bot.send_message(
        chat_id=ORDER_SEND_CHAT,
        text=texts.NEW_TAKE(
            basket=basket, phone=data['phone']
            ),
        reply_markup=buttons.NEW_TAKE(user_id)
    )
    
    await message.answer(texts.ORDER_SUCCES_SEND_ADMIN[user.lang], reply_markup=buttons.BACK_UZ)


    await state.finish()

@dp.message_handler(content_types=['text'], state=TakeAway.time)
async def time_answer(message: Message, state: FSMContext):
    await create_task(time_task(message, state))