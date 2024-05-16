from aiogram.types import Message
from aiogram import Bot
from aiogram.dispatcher import FSMContext
from bot.management.commands.utils import buttons, texts
from asyncio import create_task
from bot.management.commands.loader import dp, bot
from asgiref.sync import sync_to_async
from bot.models import User, UserPhones
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from bot.management.commands.state import UpdateRegister
from bot.management.commands.state import UpdateRegister
from aiogram.types import CallbackQuery
from django.db import transaction


async def lang_switch_task(message: Message, state: FSMContext):
    user_id = message.from_user.id

    try:
        user = await sync_to_async(User.objects.get)(user_id=user_id)
        user_phone = await sync_to_async(UserPhones.objects.get)(user_id=user_id)
    except:
        raise Exception("User topilmadi")

    phone_list_user_uz = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=user_phone.phone)
            ],
            [
                KeyboardButton(text='🔙 Ortga')
            ]
        ],
        resize_keyboard=True
    )
    phone_list_user_cr = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=user_phone.phone)
            ],
            [
                KeyboardButton(text='🔙 Ортга')
            ]
        ],
        resize_keyboard=True
    )
    phone_list_user_ru = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=user_phone.phone)
            ],
            [
                KeyboardButton(text='🔙 Назад')
            ]
        ],
        resize_keyboard=True
    )



    if (user.lang == 'uz'):
        await message.answer(texts.phone_switch_uz, parse_mode='HTML', reply_markup=phone_list_user_uz)
        await state.set_state(UpdateRegister.phone)
    elif (user.lang == 'cr'):
        await message.answer(texts.phone_switch_cr, parse_mode='HTML', reply_markup=phone_list_user_cr)
        await state.set_state(UpdateRegister.phone)

    elif (user.lang == 'ru'):
        await message.answer(texts.phone_switch_ru, parse_mode='HTML', reply_markup=phone_list_user_ru)
        await state.set_state(UpdateRegister.phone)


@dp.message_handler(
        lambda message: message.text.startswith(buttons.PHONE_SWITCH_UZ) or \
                message.text.startswith(buttons.PHONE_SWITCH_CR) or \
                    message.text.startswith(buttons.PHONE_SWITCH_RU)
        )
async def lang_switch(message: Message, state: FSMContext):
    create_task(lang_switch_task(message, state))