# kerakli handlerlarni chaqirib olish
from aiogram import types
from aiogram.dispatcher import FSMContext


from asgiref.sync import sync_to_async

from bot.management.commands.app import dp
from bot.management.commands.utils import texts, buttons
from bot.models import User



async def main_menu(message: types.Message, state: FSMContext, user=None):
    """
    Foydalanuvchi botga start bosgandagi menyu
    """
    # foydalanuvchini ismi va id sini olish
    first_name = message.from_user.first_name
    user_id = message.from_user.id
    user = user if user else await sync_to_async(User.objects.get)(user_id=user_id)
    
    # foydalanuvchiga javob qaytarish
    await message.answer(
        text=texts.MAIN_MENU[user.lang].format(first_name),
        reply_markup=buttons.MAIN_MENU(lang=user.lang),
    )

    # barcha statelarni tugalanishi
    await state.finish()

async def main_menu_callback(callback_query: types.CallbackQuery, state: FSMContext, user=None):
    """
    Foydalanuvchi botga start bosgandagi menyu_callback
    """
    # foydalanuvchini ismi va id sini olish
    first_name = callback_query.from_user.first_name
    user_id = callback_query.from_user.id
    user = user if user else await sync_to_async(User.objects.get)(user_id=user_id)
    
    # foydalanuvchiga javob qaytarish
    await callback_query.message.answer(
        text=texts.MAIN_MENU[user.lang].format(first_name),
        reply_markup=buttons.MAIN_MENU(lang=user.lang),
    )

    # end all state machines
    await state.finish()

     