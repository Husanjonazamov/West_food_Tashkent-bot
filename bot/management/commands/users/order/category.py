
from aiogram import types
from aiogram.dispatcher import FSMContext

from asgiref.sync import sync_to_async
from asyncio import create_task

from bot.management.commands.recyclable.main_menu import main_menu
from bot.management.commands.utils import buttons, texts
from bot.management.commands.app import dp
from bot.models import User

from foods.models import Category, Food


async def category_task(message: types.Message, state: FSMContext):
    """
    Bu functsiya ma'lumotlar bazasidagi ovqat categoriyalarini 
    chiqarib beradi
    """
    # user id
    user_id = message.from_user.id

    # userni olish yoki error chiqarib berish
    try:
        user = await sync_to_async(User.objects.get)(user_id=user_id)    
    except:
        raise Exception("User topilmadi")
    
    # categoryani ba'lumotlar ba'zasidan olish
    category = await sync_to_async(Category.objects.all)()

    # userga categoriyalarni jo'natish
    await message.answer(
        text=texts.CATEGORY[user.lang],
        reply_markup=buttons.CATEGORY_BUTTONS(user.lang, category)
        )

@dp.message_handler(
        lambda message: message.text.startswith((
                            buttons.BUYURTMA_BUTTON_UZ,
                            buttons.BUYURTMA_BUTTON_CR,
                            buttons.BUYURTMA_BUTTON_RU)
                            )
        )

async def category(message: types.Message, state: FSMContext):
    create_task(category_task(message, state))
