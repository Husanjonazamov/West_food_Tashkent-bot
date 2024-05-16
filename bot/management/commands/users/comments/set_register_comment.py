from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram import Bot
from ...utils.buttons import MAIN_MENU
from asyncio import create_task
from ...loader import dp, bot
from aiogram import Bot
from bot.management.commands.utils import texts
from utils.env import env
from asgiref.sync import sync_to_async
from bot.models import User
from ...state import Comments
from utils.channel_id import COMMENT_SEND_ID


async def set_register_comment_task(message: Message, state: FSMContext):
    user_id = message.from_user.id
    data = await state.get_data()
    name = data.get('name')
    comment_msg = data.get('comment_at')
    try:
        user = await sync_to_async(User.objects.get)(user_id=user_id)
    except:
        raise Exception("User topilmadi")

    if (user.lang == 'uz'):
        if message.text == '✅ Ha':
            comment_an = (f"🧑 Murojatchining ismi: {name}\n\n Fikr: {comment_msg}")
            await bot.send_message(COMMENT_SEND_ID, f"{comment_an}")
            await message.answer(texts.comment_attribution_uz, parse_mode='HTML', reply_markup=MAIN_MENU())
        elif message.text == '❌ Yoq':
            this_state = await state.get_state()
            if this_state == 'None':
                await message.answer(texts.comment_cancel_uz, parse_mode='HTML')
            await message.answer(texts.comment_cancel_current_uz, parse_mode='HTML', reply_markup=MAIN_MENU())
            await state.finish()
        else:
            await message.answer(texts.comment_error_uz, parse_mode='HTML')

    elif (user.lang == 'cr'):
        if message.text == '✅ Ҳа':
            data = await state.get_data()
            comment_an = (f"🧑 Murojatchining ismi: {name}\n\n Fikr: {comment_msg}")
            await bot.send_message(COMMENT_SEND_ID, f"{comment_an}")
            await message.answer(texts.comment_attribution_cr, parse_mode='HTML', reply_markup=MAIN_MENU())
        elif message.text == '❌ Ёқ':
            this_state = await state.get_state()
            if this_state == 'None':
                await message.answer(texts.comment_cancel_cr, parse_mode='HTML')
            await message.answer(texts.comment_cancel_current_cr, parse_mode='HTML', reply_markup=MAIN_MENU())
            await state.finish()
        else:
            await message.answer(texts.comment_error_cr, parse_mode='HTML')

    elif (user.lang == 'ru'):
        if message.text == '✅ Ha':
            data = await state.get_data()
            comment_an = (f"🧑 Murojatchining ismi: {name}\n\n Fikr: {comment_msg}")
            await bot.send_message(COMMENT_SEND_ID, f"{comment_an}")
            await message.answer(texts.comment_attribution_ru, parse_mode='HTML', reply_markup=MAIN_MENU())
        elif message.text == '❌ нет':
            this_state = await state.get_state()
            if this_state == 'None':
                await message.answer(texts.comment_cancel_ru, parse_mode='HTML')
            await message.answer(texts.comment_cancel_current_ru, parse_mode='HTML', reply_markup=MAIN_MENU())
            await state.finish()
        else:
            await message.answer(texts.comment_error_ru, parse_mode='HTML')
    await state.finish()

@dp.message_handler(content_types=['text'], state=Comments.register_commit)
async def register_comment_answer(message: Message, state: FSMContext):
    create_task(set_register_comment_task(message, state))