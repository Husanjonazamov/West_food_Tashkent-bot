from aiogram.dispatcher.storage import FSMContext

from bot.management.commands.loader import dp, bot

from asyncio import create_task
from aiogram.types import CallbackQuery

from bot.management.commands.utils import texts

async def deliver_decline_staus_send_user_task(call: CallbackQuery, state: FSMContext):

    data_split = call.data.split('-')

    status = data_split[0].replace("decline_status:", "")    
    user_id = data_split[1].replace("user_id:", "")    
    lang = data_split[2].replace("lang:", "")    

    await call.message.delete()

    status_message = texts.NEW_DELIVER_ERROR[status][lang]
    
    await bot.send_message(        
        chat_id=user_id,
        text=status_message
    )


@dp.callback_query_handler(lambda callbask_query: callbask_query.data.startswith("decline_status:"))
async def deliver_decline_staus_send_user(callbask_query: CallbackQuery, state: FSMContext):
    create_task(deliver_decline_staus_send_user_task(callbask_query, state))
