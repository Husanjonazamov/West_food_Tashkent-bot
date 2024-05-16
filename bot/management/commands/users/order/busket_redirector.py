from aiogram import types
from aiogram.dispatcher import FSMContext

from asyncio import create_task

from bot.management.commands.app import dp
from bot.management.commands.users.backet.get_basket import basket_list_task

@dp.callback_query_handler(lambda message: message.data.startswith("get_backet:"))
async def busket_redircetor(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.delete()
    user_id = callback_query.from_user.id
    callback_query.message.from_user.id = user_id    
    create_task(basket_list_task(callback_query.message, state))