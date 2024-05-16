from aiogram.dispatcher.storage import FSMContext
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from bot.management.commands.loader import dp
from asyncio import create_task
from asgiref.sync import sync_to_async
from aiogram.types import CallbackQuery
from bot.models import User, UserPhones
from ...state import TakeAway
from ...utils import texts, buttons


async def take_task(call: CallbackQuery, state: FSMContext):
    user_id = call.from_user.id
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





    if (user.lang == "uz"):
        await call.message.answer(texts.PHONE_UZ, reply_markup=phone_list_user_uz)
    elif (user.lang == "cr"):
        await call.message.answer(texts.PHONE_CR, reply_markup=phone_list_user_cr)
    elif (user.lang == "ru"):
        await call.message.answer(texts.PHONE_RU, reply_markup=phone_list_user_ru)

    await TakeAway.phone.set()
@dp.callback_query_handler(lambda callbask_query: callbask_query.data.startswith("away:"), state="*")
async def change_basket(callbask_query: CallbackQuery, state: FSMContext):
    create_task(take_task(callbask_query, state))