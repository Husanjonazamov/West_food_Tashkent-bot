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
from asgiref.sync import sync_to_async


async def handle_take_succes_task(call: CallbackQuery, state: FSMContext):
    data_split = call.data.split('-')
    user_id = data_split[1].replace("user_id:", "")
    old_message_text = call.message.text
    message_id = call.message.message_id
    
    try:
        user = await sync_to_async(User.objects.get)(user_id=user_id)
    except:
        raise Exception("User topilmadi")
    
    await bot.send_message(
        chat_id=user_id,
        text=texts.SUCCES_TAKE[user.lang]
    )
    
    await call.message.edit_text(
        text=old_message_text + "\n\n" + "✅ Buyurtma tasdiqlandi",
        reply_markup=buttons.REMOVE_TAKE(message_id, user_id)
    )

@dp.callback_query_handler(lambda callbask_query: callbask_query.data.startswith("t_succes:"))
async def handle_take_succes(callbask_query: CallbackQuery, state: FSMContext):
    create_task(handle_take_succes_task(callbask_query, state))
