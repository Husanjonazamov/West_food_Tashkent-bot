
from aiogram import types
from aiogram.dispatcher import FSMContext

from asyncio import create_task

from bot.management.commands.app import dp
from .category import category

@dp.callback_query_handler(lambda message: message.data.startswith("category_redirect:"))
async def category_redirect(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.delete()
    user_id = callback_query.from_user.id
    callback_query.message.from_user.id = user_id    
    create_task(category(callback_query.message, state))