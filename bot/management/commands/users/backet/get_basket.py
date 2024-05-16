from aiogram import types
from aiogram.dispatcher import FSMContext

from asgiref.sync import sync_to_async
from asyncio import create_task
from bot.models import UserPhones
from bot.management.commands.loader import bot
from bot.management.commands.recyclable.main_menu import main_menu
from bot.management.commands.services.services import getBasketList
from bot.management.commands.utils import buttons, texts
from bot.management.commands.state import Register
from bot.management.commands.app import dp
from bot.models import Basket, User
from utils.env import env


@sync_to_async
def get_baskets_async(user_id):
    return Basket.objects.filter(user__user_id=user_id)


async def basket_list_task(message: types.Message, state: FSMContext):
    """
    Foydalanuchi savatchasindagi mahsulotlarni olish
    """
    user_id = message.from_user.id

    # change this code
    # basket_list_send_chat_id = env.str('CHANNEL_ID')
    # await bot.send_message(chat_id=basket_list_send_chat_id, text=message_text)

    # get user
    try:
        user = await sync_to_async(User.objects.get)(user_id=user_id)
    except:
        raise Exception("User topilmadi")

        
    basket = getBasketList(user_id=user_id)
    
    if 'detail' in basket:
        await message.answer(texts.EMPTY_BASKET[user.lang], reply_markup=buttons.GET_CATEGORY(lang=user.lang))
        return

    message_text = ""
    message_buttons = types.InlineKeyboardMarkup(row_width=2)

    if user.lang == 'uz':
        message_text = texts.your_basket_uz
        for i in basket:
            message_text += f"<b>{i['food']['name_uz']} X {i['count']} = {i['count'] * i['food']['price']}</b>\n"
            message_buttons.add(types.InlineKeyboardButton(
                text=i['food']['name_uz'],
                callback_data=f"change_basket_item:{i['id']}-change_to:"
            ))

    elif user.lang == 'cr':
        message_text = texts.your_basket_cr
        for i in basket:
            message_text += f"<b>{i['food']['name_cr']} X {i['count']} = {i['count'] * i['food']['price']}</b>"
            message_buttons.add(types.InlineKeyboardButton(
                text=i['food']['name_cr'],
                callback_data=f"change_basket_item:{i['id']}-change_to:"
            ))

    else:
        message_text = texts.your_basket_ru
        for i in basket:
            message_text += f"<b>{i['food']['name_ru']} X {i['count']} = {i['count'] * i['food']['price']}</b>"
            message_buttons.add(types.InlineKeyboardButton(
                text=i['food']['name_ru'],
                callback_data=f"change_basket_item:{i['id']}-change_to:"
            ))

    if user.lang == 'uz':
        message_buttons.add(
            types.InlineKeyboardButton(
                text='🚗 Yetkazib berish',
                callback_data='delivery:'
            ),
            types.InlineKeyboardButton(
                text='🚶 Olib ketish',
                callback_data='away:'
            ),
        )
    elif user.lang == 'cr':
        message_buttons.add(
            types.InlineKeyboardButton(
                text='🚗 Етказиб бериш',
                callback_data='delivery:'
            ),
            types.InlineKeyboardButton(
                text='🚶 Олиб кетиш',
                callback_data='away:'
            ),
        )
    else:
        message_buttons.add(
            types.InlineKeyboardButton(
                text='🚗 Доставка',
                callback_data='delivery:'
            ),
            types.InlineKeyboardButton(
                text='🚶 Работа на вынос',
                callback_data='away:'
            ),
        )

    await message.answer(text=message_text, reply_markup=message_buttons)


@dp.message_handler(lambda message: message.text.startswith((
        buttons.BUYURTMALARIM_BUTTON_UZ,
        buttons.BUYURTMALARIM_BUTTON_CR,
        buttons.BUYURTMALARIM_BUTTON_RU,
))
                    )
async def basket_list(message: types.Message, state: FSMContext):
    create_task(basket_list_task(message, state))
