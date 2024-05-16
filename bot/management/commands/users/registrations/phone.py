
from aiogram import types
from aiogram.dispatcher import FSMContext

from asgiref.sync import sync_to_async
from asyncio import create_task

from bot.management.commands.recyclable.main_menu import main_menu
from bot.management.commands.state import Register
from bot.management.commands.utils import texts
from bot.management.commands.app import dp
from bot.models import User, UserPhones



async def phone_number_task(message: types.Message, state: FSMContext):
    """
    set user phone number for regsiter form state
    """

    user_id = message.from_user.id
    state_data = await state.get_data()
    lang = state_data['lang']

    # get user phone number
    if 'contact' in message:
        phone = message.contact.phone_number
    else:
        phone = message.text

        # phone validator
        if not phone.isdigit() and \
              len(phone) < 9:
            await message.answer(text=texts.PHONE_ERROR[lang])
            return
        phone = "+998" + phone
    
    # new phone for user
    newphone = await sync_to_async(UserPhones.objects.create)(
        phone=phone,
        user_id=user_id,
    )
    
    # create new user
    newuser = await sync_to_async(User.objects.create)(
        user_id=user_id,
        lang=lang
    )
    
    # send welcome message
    await main_menu(message, state)
    
    # finish state
    await state.finish()
    

@dp.message_handler(state=Register.phone, content_types=['text', 'contact'])
async def phone_number(message: types.Message, state: FSMContext):
    create_task(phone_number_task(message, state))
