
import os
from config.settings import MEDIA_ROOT, MEDIA_URL
from django.contrib.staticfiles.storage import staticfiles_storage

from aiogram import types
from aiogram.dispatcher import FSMContext

from asgiref.sync import sync_to_async
from asyncio import create_task

from bot.management.commands.recyclable.main_menu import main_menu
from bot.management.commands.utils import buttons, texts
from bot.management.commands.state import Register
from bot.management.commands.app import dp
from bot.models import User

from foods.models import Category, Food


async def category_task(callback_query: types.CallbackQuery, state: FSMContext):
    """
    Tanlangan categoriyadagi ovqatlarni userga jo'natish
    """

    # eski habarni o'chirib tashlash
    # categoriyalarni o'chirib tashlash
    await callback_query.message.delete()
    
    # user id
    user_id = callback_query.from_user.id
    
    # tanlangan categoriya id ni olish
    category_id = callback_query.data.replace("category:", "")
    
    # userni olish yoki hatolik chiqarish
    try:
        user = await sync_to_async(User.objects.get)(user_id=user_id)    
    except:
        raise Exception("User topilmadi")
    
    # tanlangan categoriyani olish. categoriya rasmini olish uchun
    category = await sync_to_async(Category.objects.get)(id=category_id)    
    # tanlangan categoriya bo'yicha maxsulotlarni olish
    foods = await sync_to_async(Food.objects.filter)(category__id=category_id)    
    
    with open(category.image.path, "rb") as buffer:
        await callback_query.message.answer_photo(
            photo=buffer.read(),
            caption=texts.FOODS[user.lang],
            reply_markup=buttons.FOODS(lang=user.lang, foods=foods, category_id=category_id)
        )
    
    # end all state machines
    await state.finish()
    

@dp.callback_query_handler(lambda message: message.data.startswith("category:"))
async def category(callback_query: types.CallbackQuery, state: FSMContext):
    create_task(category_task(callback_query, state))