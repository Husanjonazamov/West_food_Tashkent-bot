
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from asyncio import create_task
from asgiref.sync import sync_to_async


from bot.management.commands.services.services import getBasketList
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from bot.management.commands.app import dp, bot
from bot.management.commands.utils import texts, buttons
from bot.models import Basket, User
from foods.models import Food

async def basket_task(callback_query: types.CallbackQuery, state: FSMContext):

    await callback_query.message.delete()

    user_id = int(callback_query.from_user.id)
    user_id = callback_query.from_user.id
    message_id = callback_query.message.message_id
    data_split = callback_query.data.split("-")
    food_id = data_split[1].replace("food:", "")

    try:
        category_id = data_split[2].replace("category:", "")
        number = int(data_split[3].replace("number:", ""))
    except IndexError:
        print("data_split listida yetarli elementlar mavjud emas")

    try:
        food = await sync_to_async(Food.objects.get)(id=food_id)
    except:
        raise Exception("Food topilmadi")

    try:
        user = await sync_to_async(User.objects.get)(user_id=user_id)
    except:
        raise Exception("User topilmadi")

    try:
        get_food_for_basket = await sync_to_async(Basket.objects.get)(user__user_id=user_id, food__id=food_id)
        get_food_for_basket.count = number
        await sync_to_async(get_food_for_basket.save)()
    except:
        await sync_to_async(Basket.objects.create)(
            user=user,
            food=food,
            count=number
            )

    await callback_query.message.answer(
        text=texts.SUCCES_BASKET[user.lang],
        reply_markup=buttons.SUCCES_BASKET(lang=user.lang)
        )
    

    # end all state machines
    await state.finish()



@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith("basket:"))
async def basket(callback_query: types.CallbackQuery, state: FSMContext):
    create_task(basket_task(callback_query, state))