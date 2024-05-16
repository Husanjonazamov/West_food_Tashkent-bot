from aiogram import types
from aiogram.dispatcher import FSMContext

from asgiref.sync import sync_to_async
from asyncio import create_task

from utils.env import env
from ...loader import bot
from bot.management.commands.recyclable.main_menu import main_menu
from bot.management.commands.services.services import getBasketList, getBasketItem, changeBasketItem
from bot.management.commands.utils import buttons, texts
from bot.management.commands.state import Register
from bot.management.commands.app import dp
from bot.models import Basket, User
from bot.management.commands.state import Delivery 


async def change_basket_task(callbask_query: types.CallbackQuery, state: FSMContext):
    """
    Foydalanuchi savatchasindagi mahsulotlarni o'zgartirish
    """
    user_id = callbask_query.from_user.id
    data_split = callbask_query.data.split("-")
    basket_id = int(data_split[0].replace("change_basket_item:", ""))
    change_to = data_split[1].replace("change_to:", "")

    changeBasketItem(basket_id=basket_id, action=change_to)
    basket_item = getBasketItem(basket_id=basket_id)
    try:
        user = await sync_to_async(User.objects.get)(user_id=user_id)
    except:
        raise Exception("User topilmadi")

    if user.lang == "uz":
        await callbask_query.message.edit_text(
            text=f"{basket_item['food']['name_uz']} X {basket_item['count']} = {basket_item['count'] * basket_item['food']['price']}",
                    reply_markup=types.InlineKeyboardMarkup(row_width=2, inline_keyboard=[
                [
                    types.InlineKeyboardButton(
                        text='-',
                        callback_data=f"change_basket_item:{basket_id}-change_to:decr"
                    ),
                    types.InlineKeyboardButton(
                        text='+',
                        callback_data=f"change_basket_item:{basket_id}-change_to:incr"
                    )
                ],
                [
                    types.InlineKeyboardButton(
                        text='🔙 Orqaga',
                        callback_data='backet_to_basket:'
                    )
                ]
            ])
        )


    if user.lang == "cr":
        await callbask_query.message.edit_text(
            text=f"{basket_item['food']['name_uz']} X {basket_item['count']} = {basket_item['count'] * basket_item['food']['price']}",

            reply_markup=types.InlineKeyboardMarkup(row_width=2, inline_keyboard=[
                [
                    types.InlineKeyboardButton(
                        text='-',
                        callback_data=f"change_basket_item:{basket_id}-change_to:decr"
                    ),
                    types.InlineKeyboardButton(
                        text='+',
                        callback_data=f"change_basket_item:{basket_id}-change_to:incr"
                    )
                ],
                [
                    types.InlineKeyboardButton(
                        text='🔙 Орқага',
                        callback_data='backet_to_basket:'
                    )
                ]
            ])
        )

    else:
        await callbask_query.message.edit_text(
            text=f"{basket_item['food']['name_ru']} X {basket_item['count']} = {basket_item['count'] * basket_item['food']['price']}",
            reply_markup=types.InlineKeyboardMarkup(row_width=2, inline_keyboard=[
                [
                    types.InlineKeyboardButton(
                        text='-',
                        callback_data=f"change_basket_item:{basket_id}-change_to:decr"
                    ),
                    types.InlineKeyboardButton(
                        text='+',
                        callback_data=f"change_basket_item:{basket_id}-change_to:incr"
                    )
                ],
                [
                    types.InlineKeyboardButton(
                        text='🔙 Назад',
                        callback_data='backet_to_basket:'
                    )
                ]
            ])
        )


@dp.callback_query_handler(lambda callbask_query: callbask_query.data.startswith("change_basket_item:"))
# @dp.message_handler(content_types=['text'], state=Delivery.basket_eater)
async def change_basket(callbask_query: types.CallbackQuery, state: FSMContext):
    create_task(change_basket_task(callbask_query, state))



