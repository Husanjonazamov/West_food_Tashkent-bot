from aiogram import types
from aiogram.dispatcher import FSMContext

from asgiref.sync import sync_to_async
from asyncio import create_task

from bot.management.commands.recyclable.main_menu import main_menu
from bot.management.commands.state import Register, Delivery
from bot.management.commands.utils import texts, buttons
from bot.management.commands.app import dp
from bot.models import User


async def set_phone_task(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    try:
        user = await sync_to_async(User.objects.get)(user_id=user_id)
    except:
        raise Exception("User topilmadi")

    if (user.lang == "uz"):
        await state.update_data(phone=message.text)
        # phone validator
        if len(message.text) > 8:
            if not ("0" in message.text or
                    "1" in message.text or
                    "2" in message.text or
                    "3" in message.text or
                    "4" in message.text or
                    "5" in message.text or
                    "6" in message.text or
                    "7" in message.text or
                    "8" in message.text or
                    "9" in message.text):
                await message.answer(texts.phone_rule_uz)
            else:
                await state.set_state(Delivery.location)
                await message.answer(texts.location_uz, reply_markup=buttons.LOCATION_UZ)
        else:
            await message.answer(texts.phone_nomer_len_rule_uz)
    elif (user.lang == "cr"):
        await state.update_data(phone=message.text)
        if len(message.text) > 8:
            if not ("0" in message.text or
                    "1" in message.text or
                    "2" in message.text or
                    "3" in message.text or
                    "4" in message.text or
                    "5" in message.text or
                    "6" in message.text or
                    "7" in message.text or
                    "8" in message.text or
                    "9" in message.text):
                await message.answer(texts.phone_rule_cr)
            else:
                await state.set_state(Delivery.location)
                await message.answer(texts.location_cr, reply_markup=buttons.LOCATION_CR)
        else:
            await message.answer(texts.phone_nomer_len_rule_cr)
    elif (user.lang == "ru"):
        await state.update_data(phone=message.text)
        # phone validator
        if len(message.text) > 8:
            if not ("0" in message.text or
                    "1" in message.text or
                    "2" in message.text or
                    "3" in message.text or
                    "4" in message.text or
                    "5" in message.text or
                    "6" in message.text or
                    "7" in message.text or
                    "8" in message.text or
                    "9" in message.text):
                await message.answer(texts.phone_rule_ru)
            else:
                await state.set_state(Delivery.location)
                await message.answer(texts.location_ru, reply_markup=buttons.LOCATION_RU)

        else:
            await message.answer(texts.phone_nomer_len_rule_ru)


@dp.message_handler(state=Delivery.phone, content_types=['text'])
async def phone_number(message: types.Message, state: FSMContext):
    create_task(set_phone_task(message, state))
