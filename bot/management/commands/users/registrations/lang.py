
from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.management.commands.app import dp

from asgiref.sync import sync_to_async
from asyncio import create_task

from bot.management.commands.state import Register
from bot.management.commands.utils import texts, buttons

from bot.models import User


async def lang_task(callback_query: types.CallbackQuery, state: FSMContext):
    """
    set user language for regsiter form state
    """

    # get user selected language
    lang = callback_query.data
    
    # set user language in state
    await state.set_data({
        "lang":lang
    })

    # send contact buttons
    await callback_query.message.answer(
        text=texts.PHONE[lang],
        reply_markup=buttons.CONTACT[lang],
        )
    
    # change state to phone number
    await Register.next()


@dp.callback_query_handler(state=Register.lang)
async def lang(callback_query: types.CallbackQuery, state: FSMContext):
    create_task(lang_task(callback_query, state))
