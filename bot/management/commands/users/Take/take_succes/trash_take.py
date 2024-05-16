from aiogram.dispatcher.storage import FSMContext
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from bot.management.commands.loader import dp, bot
from asyncio import create_task
from asgiref.sync import sync_to_async
from aiogram.types import CallbackQuery
from bot.management.commands.utils.functions import cleanBaskeAndSetRating
from bot.models import UserPhones, User
from config.settings import ORDER_SEND_CHAT
from ...registrations import phone
from ....state import Delivery
from ....utils import texts, buttons


async def handle_take_succes_task(call: CallbackQuery, state: FSMContext):
    data_split = call.data.split('-')
    message_id = data_split[0].replace("trash_take:", "")
    user_id = data_split[1].replace("user_id:", "")

    create_task(cleanBaskeAndSetRating(user_id=user_id))
    
    await bot.send_message(
        chat_id=user_id,
        text=texts.THAKS_SERVICES
    )
    await bot.delete_message(chat_id=ORDER_SEND_CHAT, message_id=message_id)
    

@dp.callback_query_handler(lambda callbask_query: callbask_query.data.startswith("trash_take:"))
async def handle_take_succes(callbask_query: CallbackQuery, state: FSMContext):
    create_task(handle_take_succes_task(callbask_query, state))
