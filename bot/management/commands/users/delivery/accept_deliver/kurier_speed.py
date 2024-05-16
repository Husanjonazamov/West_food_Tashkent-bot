from aiogram.dispatcher.storage import FSMContext
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from bot.management.commands.loader import dp, bot
from asyncio import create_task
from asgiref.sync import sync_to_async
from aiogram.types import CallbackQuery
from bot.models import UserPhones, User
from ...registrations import phone
from ....state import Delivery
from ....utils import texts, buttons


async def y_new_d_task(call: CallbackQuery, state: FSMContext):

    data_spelit = call.data.split('-')
    user_id = data_spelit[1].replace("user_id:", "")

    dis = float(data_spelit[2].replace("dis:", ""))
    
    await call.message.edit_text(
        text=texts.DELIVER_SPEED,
        reply_markup=buttons.DELIVER_SPEED(user_id, dis)
    )

@dp.callback_query_handler(lambda callbask_query: callbask_query.data.startswith("y_new_d:"))
async def y_new_d(callbask_query: CallbackQuery, state: FSMContext):
    create_task(y_new_d_task(callbask_query, state))
