from aiogram.types import Message
from aiogram import Bot
from aiogram.dispatcher import FSMContext
from ...utils import buttons, texts
from asyncio import create_task
from ...loader import dp, bot
from asgiref.sync import sync_to_async
from bot.models import User



async def settings_answer_task(message: Message, state: FSMContext):
    user_id = message.from_user.id
    try:
        user = await sync_to_async(User.objects.get)(user_id=user_id)
        lang = user.lang
    except:
        raise Exception("User topilmadi")
    if (user.lang == 'uz'):
        await message.answer(texts.settings_text_uz, parse_mode='HTML', reply_markup=buttons.SETTINGS_MENYU_UZ)

    elif (user.lang == 'cr'):
        await message.answer(texts.settings_text_cr, parse_mode='HTML', reply_markup=buttons.SETTINGS_MENYU_CR)

    elif (user.lang == 'ru'):
        await message.answer(texts.settings_text_ru, parse_mode='HTML', reply_markup=buttons.SETTINGS_MENYU_RU)

@dp.message_handler(
        lambda message: message.text.startswith(buttons.SOZLAMALAR_BUTTON_UZ) or \
                message.text.startswith(buttons.SOZLAMALAR_BUTTON_CR) or \
                    message.text.startswith(buttons.SOZLAMALAR_BUTTON_RU)
        )
async def settings_answer(message: Message, state: FSMContext):
    create_task(settings_answer_task(message, state))