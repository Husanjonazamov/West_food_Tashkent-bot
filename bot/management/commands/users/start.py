
from aiogram import types
from aiogram.dispatcher import FSMContext

from asgiref.sync import sync_to_async
from asyncio import create_task

from bot.management.commands.recyclable.main_menu import main_menu
from bot.management.commands.utils import buttons, texts
from bot.management.commands.state import Register
from bot.management.commands.app import dp, bot
from bot.models import User
from config.settings import ORDER_SEND_CHAT

async def send_welcome_task(message: types.Message, state: FSMContext):
    """
    This handler will be called when client send `/start` or `/help` commands.
    """ 

    # user id
    user_id = message.from_user.id

    # get or set register user
    try:
        user = await sync_to_async(User.objects.get)(user_id=user_id)
        await main_menu(message, state, user)

        await state.finish()
        
        return
    except:

        await message.answer(
            text=texts.LANGS,
            reply_markup=buttons.LANG
            )
        
    # set language state
    await Register.lang.set()


@dp.message_handler(state='*', commands=['start', 'help'])
async def send_welcome(message: types.Message, state: FSMContext):
    create_task(send_welcome_task(message, state))
