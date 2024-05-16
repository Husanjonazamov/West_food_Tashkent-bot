from aiogram.dispatcher.storage import FSMContext
from aiogram.types import Message
from ...loader import dp, bot
from bot.management.commands.utils import texts, buttons
from asyncio import create_task


async def handle_information(message: Message, state: FSMContext):
    await message.answer(texts.information, reply_markup=buttons.information_uz, parse_mode='HTML')


@dp.message_handler(state="*", text=buttons.SHARTLAR_BUTTON_UZ ,content_types=['text'])
async def information(message: Message, state: FSMContext):
    await create_task(handle_information(message, state))