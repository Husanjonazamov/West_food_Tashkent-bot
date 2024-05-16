from aiogram import types
from aiogram.dispatcher import FSMContext

from asgiref.sync import sync_to_async
from asyncio import create_task
from bot.management.commands.recyclable.main_menu import main_menu
from bot.management.commands.services.services import getBasketList
from bot.management.commands.users.backet.get_basket import basket_list_task
from bot.management.commands.utils import buttons, texts
from bot.management.commands.state import Register
from bot.management.commands.app import dp
from bot.models import Basket, User


# @dp.callback_query_handler(lambda message: message.data.startswith("get_backet:"))
# async def busket_redircetor(callback_query: types.CallbackQuery, state: FSMContext):
#     await callback_query.message.delete()
#     user_id = callback_query.from_user.id
#     callback_query.message.from_user.id = user_id    
#     create_task(basket_list_task(callback_query.message, state))


async def change_basket_task(callbask_query: types.CallbackQuery, state: FSMContext):
    """
    Foydalanuchini savatchaga o'tqazib yuborish
    """
    await callbask_query.message.delete()
    user_id = callbask_query.from_user.id
    callbask_query.message.from_user.id = user_id
    await basket_list_task(callbask_query.message, state=state)


@dp.callback_query_handler(lambda callbask_query: callbask_query.data.startswith("backet_to_basket:"))
async def change_basket(callbask_query: types.CallbackQuery, state: FSMContext):
    create_task(change_basket_task(callbask_query, state))
