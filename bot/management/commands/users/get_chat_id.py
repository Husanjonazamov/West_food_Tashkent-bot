
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

async def get_chat_id_task(message: types.Message, state: FSMContext):
    """
    /chatid command
    """ 
    
    # chat id
    chatid = message.chat.id
    
    await message.answer(text=f"<code>{chatid}</code>")

@dp.message_handler(state='*', commands=['chatid',])
async def send_welcome(message: types.Message, state: FSMContext):
    create_task(get_chat_id_task(message, state))
