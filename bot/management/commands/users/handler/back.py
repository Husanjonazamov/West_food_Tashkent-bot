from aiogram.types import Message
from aiogram import Bot
from aiogram.dispatcher import FSMContext
from ...utils import buttons, texts
from asyncio import create_task
from ...loader import dp
from asgiref.sync import sync_to_async
from bot.models import User



async def back_task(message: Message, state: FSMContext):

    user_id = message.from_user.id

    try:
        user = await sync_to_async(User.objects.get)(user_id=user_id)
    except:
        raise Exception("User topilmadi")
    if (user.lang == 'uz'):
        await message.answer(texts.back_uz, reply_markup=buttons.MAIN_MENU(lang='uz'))

    elif (user.lang == 'cr'):
        await message.answer(texts.back_cr, reply_markup=buttons.MAIN_MENU(lang='cr'))

    elif (user.lang == 'ru'):
        await message.answer(texts.back_ru, reply_markup=buttons.MAIN_MENU(lang='ru'))
    await state.finish()

@dp.message_handler(state='*', text=buttons.ORTGA_MAIN_BUTTON_UZ, content_types=['text'])
async def back_uz(message: Message, state: FSMContext):
    create_task(back_task(message, state))

@dp.message_handler(state='*', text=buttons.ORTGA_MAIN_BUTTON_CR, content_types=['text'])
async def back_cr(message: Message, state: FSMContext):
    create_task(back_task(message, state))

@dp.message_handler(state='*', text=buttons.ORTGA_MAIN_BUTTON_RU, content_types=['text'])
async def back_ru(message: Message, state: FSMContext):
    create_task(back_task(message, state))