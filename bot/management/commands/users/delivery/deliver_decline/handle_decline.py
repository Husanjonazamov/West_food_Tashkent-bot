from aiogram.dispatcher.storage import FSMContext
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from bot.management.commands.loader import dp
from asyncio import create_task
from asgiref.sync import sync_to_async
from aiogram.types import CallbackQuery
from bot.models import UserPhones, User
from ...registrations import phone
from ....state import Delivery
from ....utils import texts, buttons


async def delivery_decline_task(call: CallbackQuery, state: FSMContext):
    data_split = call.data.split('-')
    user_id = data_split[1].replace("user_id:", "")
    
    try:
        user_phone = await sync_to_async(UserPhones.objects.get)(user_id=user_id)
        user = await sync_to_async(User.objects.get)(user_id=user_id)
    except:
        raise Exception("User topilmadi")
    
    await call.message.edit_text(
        text=texts.DELIVERY_DECLINE,
        reply_markup=buttons.DECLINE_DELIVERY_STATUS(
            user_id=user_id,
            lang=user.lang
            )
        )



@dp.callback_query_handler(lambda callbask_query: callbask_query.data.startswith("n_new_d:"))
async def deliver_decline(callbask_query: CallbackQuery, state: FSMContext):
    create_task(delivery_decline_task(callbask_query, state))
