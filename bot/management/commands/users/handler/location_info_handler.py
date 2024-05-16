from aiogram.dispatcher.storage import FSMContext
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from bot.management.commands.loader import dp, bot
from asyncio import create_task
from asgiref.sync import sync_to_async
from aiogram.types import CallbackQuery
from bot.models import UserPhones, User
from ..registrations import phone
from ...state import Delivery
from ...utils import texts, buttons


async def delivery_task(message: Message, state: FSMContext):
    user_id = message.from_user.id

    try:
        user = await sync_to_async(User.objects.get)(user_id=user_id)
        user_phone = await sync_to_async(UserPhones.objects.get)(user_id=user_id)
    except:
        raise Exception("User topilmadi")


    if (user.lang == "uz"):
        await message.answer(texts.location_info_uz, reply_markup=buttons.BACK_UZ)
    elif (user.lang == "cr"):
        await message.answer(texts.location_info_uz, reply_markup=buttons.BACK_UZ)
    elif (user.lang == "ru"):
        await message.answer(texts.location_info_uz, reply_markup=buttons.BACK_UZ)


@dp.message_handler(state='*', text="🕹 Manzilni ko'rish", content_types=['text'])
async def change_basket(message: Message, state: FSMContext):
    create_task(delivery_task(message, state))

