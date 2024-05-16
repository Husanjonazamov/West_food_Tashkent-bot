
from aiogram import types
from aiogram.dispatcher import FSMContext

from asgiref.sync import sync_to_async
from asyncio import create_task

from bot.management.commands.recyclable.main_menu import main_menu
from bot.management.commands.services.services import getBasketList
from bot.management.commands.utils import buttons, texts
from bot.management.commands.state import Register
from bot.management.commands.app import dp, bot
from bot.models import User, Basket

from foods.models import Category, Food


async def count_task(callback_query: types.CallbackQuery, state: FSMContext):
    """
    Tanlangan ovqatni user savatchasidan bor yo'qligini tekshiriladi.
    Agar bor bo'lsa davomidan qo'shib ketilinadi 😃
    """
    
    # user id
    user_id = callback_query.from_user.id

    # callback_data ni bo'laklash
    # data = f"food:{i.id}-category:{category_id}"
    data_split = callback_query.data.split("/")
    print(data_split)

    
    # food id'ni olish
    food_id = data_split[0].replace("food:", "")
    
    # message id'ni olish
    message_id = callback_query.message.message_id

    # categoriya id'ni olish 
    category_id = data_split[1].replace("category:", "")

    number = int(data_split[2].replace("number:", ""))

    # user id'ni olish yoki xatolik chiqarib berish
    try:
        user = await sync_to_async(User.objects.get)(user_id=user_id)    
    except:
        raise Exception("User topilmadi")
    
    try:
        count = callback_query.message.caption.split('\n')[1].replace("x", '')
        count = int(count) + number
    except:
        try:
            get_food_for_basket = await sync_to_async(Basket.objects.get)(user__user_id=user_id, food__id=food_id)
            count = get_food_for_basket.count
        except:
            count = 1

    #food id ni ma'lumotlar ba'zasidan olish
    food = await sync_to_async(Food.objects.get)(id=food_id)    
    
    # food name foydalanuvchi tanlagan til bo'ycha
    if user.lang == "uz":
        food_name = food.name_uz
    if user.lang == "cr":
        food_name = food.name_cr
    elif user.lang == "ru":
        food_name = food.name_ru


    print('------------------')
    print(food.img.path)
    print('------------------')

    if count < 0:
        await callback_query.answer("Siz mahsulot sonini minusda kiritdiz. Siz tentakmisizmi?")
    # change message photo ....
    else:
        with open(food.img.path, "rb") as buffer:
            local_media = types.InputFile(buffer)
            photo = types.InputMediaPhoto(media=local_media,
                caption=texts.COUNT.format(
                        food_name,
                        count,
                        count, food.price, count * food.price
                    ),
                )
            await bot.edit_message_media(
                chat_id=user_id,
                message_id=message_id,
                media=photo,
                reply_markup=buttons.COUNTER_MENU(food_id, category_id, count, lang=user.lang),
                )
        

    # barcha statelarni tugatish
    await state.finish()
    

@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith("food:"))
async def count(callback_query: types.CallbackQuery, state: FSMContext):
    create_task(count_task(callback_query, state))