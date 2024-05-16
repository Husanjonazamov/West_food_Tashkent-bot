from aiogram import types
from aiogram.dispatcher import FSMContext

from asgiref.sync import sync_to_async
from asyncio import create_task

from bot.management.commands.recyclable.main_menu import main_menu
from bot.management.commands.state import UpdateRegister
from bot.management.commands.utils import texts, buttons
from bot.management.commands.app import dp
from bot.models import User, UserPhones


async def phone_number_task(message: types.Message, state: FSMContext):
    """
    set user phone number for regsiter form state
    """
    user_id = message.from_user.id
    user = await sync_to_async(User.objects.get)(user_id=user_id)
    state_data = await state.get_data()
    lang = user.lang

    # get user phone number
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
                await message.answer(texts.phone_nomer_len_rule_cr)
    # new phone for user
    user_id = message.from_user.id
    phone = message.text
    user_phone = await sync_to_async(UserPhones.objects.get)(user_id=user_id)
    # set user language in state
    await state.set_data({
        "phone": phone
    })
    state_data = await state.get_data()
    phone = state_data['phone']
    user_phone.phone = phone
    await sync_to_async(user_phone.save)()

    # send contact buttons
    if user.lang == 'uz':
        await message.answer(
            text=texts.phone_switch_handler_uz,
            reply_markup=buttons.MAIN_MENU(lang)
        )
    elif user.lang == 'cr':
        await message.answer(
            text=texts.phone_switch_handler_cr,
            reply_markup=buttons.MAIN_MENU(lang)
        )
    elif user.lang == 'ru':
        await message.answer(
            text=texts.phone_switch_handler_ru,
            reply_markup=buttons.MAIN_MENU(lang)
        )

    # finish state
    await state.finish()


@dp.message_handler(state=UpdateRegister.phone, content_types=['text', 'contact'])
async def phone_number(message: types.Message, state: FSMContext):
    create_task(phone_number_task(message, state))
