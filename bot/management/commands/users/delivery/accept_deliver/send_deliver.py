from aiogram.dispatcher.storage import FSMContext
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import CallbackQuery

from asyncio import create_task

from bot.management.commands.utils.functions import cleanBaskeAndSetRating
from foods.models import Food
from bot.management.commands.loader import dp, bot
from asgiref.sync import sync_to_async
from bot.management.commands.services.services import clearBasketItem, getBasketList
from bot.models import UserPhones, User
from ...registrations import phone
from ....state import Delivery
from ....utils import texts, buttons


async def y_new_d_task(call: CallbackQuery, state: FSMContext):
    # send_deliver:-user_id:{}-delivered_time

    data_split = call.data.split('-')

    user_id = data_split[1].replace("user_id:", "")
    delivered_time = data_split[2].replace("del_time:", "")
    
    try:
        user = await sync_to_async(User.objects.get)(user_id=user_id)
    except:
        raise Exception("User topilmadi")
    
    create_task(cleanBaskeAndSetRating(user_id=user_id))
    
    await call.message.delete()

    # clear user basket
    clearBasketItem(user_id)
    
    await bot.send_message(
        chat_id=user_id,
        text=texts.ACCEPT_DELIVERY[user.lang].format(delivered_time)
    )
    
    

@dp.callback_query_handler(lambda callbask_query: callbask_query.data.startswith("s_deliver:"))
async def y_new_d(callbask_query: CallbackQuery, state: FSMContext):
    create_task(y_new_d_task(callbask_query, state))
