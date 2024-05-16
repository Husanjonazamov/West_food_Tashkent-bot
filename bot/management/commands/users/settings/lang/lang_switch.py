from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.management.commands.app import dp

from asgiref.sync import sync_to_async
from asyncio import create_task

from bot.management.commands.state import UpdateRegister
from bot.management.commands.utils import texts, buttons

from bot.models import User


async def lang_task(callback_query: types.CallbackQuery, state: FSMContext):
    """
    set user language for regsiter form state
    """

    # get user selected language
    user_id = callback_query.from_user.id
    lang = callback_query.data
    user = await sync_to_async(User.objects.get)(user_id=user_id)
    # set user language in state
    await state.set_data({
        "lang": lang
    })
    user_from_id = user.user_id
    state_data = await state.get_data()
    lang = state_data['lang']
    user.lang = lang
    await sync_to_async(user.save)()
    await callback_query.message.delete()
    # send contact buttons
    if user.lang == 'uz':
        await callback_query.message.answer(
            text=texts.lang_switch_handler_uz,
            reply_markup=buttons.MAIN_MENU(lang)
        )
    elif user.lang == 'cr':
        await callback_query.message.answer(
            text=texts.lang_switch_handler_cr,
            reply_markup=buttons.MAIN_MENU(lang)
        )
    elif user.lang == 'ru':
        await callback_query.message.answer(
            text=texts.lang_switch_handler_ru,
            reply_markup=buttons.MAIN_MENU(lang)
        )

    # change state to phone number
    await state.finish()


@dp.callback_query_handler(state=UpdateRegister.lang)
async def lang(callback_query: types.CallbackQuery, state: FSMContext):
    create_task(lang_task(callback_query, state))
