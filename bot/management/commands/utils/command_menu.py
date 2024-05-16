from aiogram.dispatcher.storage import FSMContext
from aiogram.types import Message
from bot.models import User
from . import texts
from ..loader import dp, bot
from asyncio import create_task
from asgiref.sync import sync_to_async



async def contect_handler_task(message: Message, state: FSMContext):
    user_id = message.from_user.id
    try:
        user = await sync_to_async(User.objects.get)(user_id=user_id)
    except:
        print('___')

    if (user.lang=='uz'):
        await message.answer(texts.contact_uz, parse_mode='HTML')
    elif (user.lang=='cr'):
        await message.answer(texts.contact_cr, parse_mode='HTML')
    elif (user.lang=='ru'):
        await message.answer(texts.contact_ru, parse_mode='HTML')




@dp.message_handler(state="*", commands=['contact'])
async def contect_handler(message: Message, state: FSMContext):
    await create_task(contect_handler_task(message, state))
