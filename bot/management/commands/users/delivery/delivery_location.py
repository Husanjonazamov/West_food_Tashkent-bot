from aiogram.dispatcher.storage import FSMContext
from aiogram.types import Message
from bot.management.commands.loader import dp, bot
from asyncio import create_task
from asgiref.sync import sync_to_async
from bot.management.commands.services.services import getBasketList
from bot.management.commands.users.delivery.delivery_phone import phone_number
from bot.management.commands.utils.functions import calculate_distance
from bot.models import User
from config.settings import KITCHEN_LAN, KITCHEN_LON
from ...state import Delivery
from utils.channel_id import ORDER_SEND_CHAT
from ...utils import texts, buttons

async def delivery_location_task(message: Message, state: FSMContext):
    user_id = message.from_user.id
    
    try:
        user = await sync_to_async(User.objects.get)(user_id=user_id)
    except:
        raise Exception("User topilmadi")

    data = await state.get_data()
    phone = data.get('phone')
    basket = getBasketList(user_id)

    distance = calculate_distance(
        message.location.latitude,
        message.location.longitude,
        KITCHEN_LAN,
        KITCHEN_LON,
    )

    # send message curier
    await bot.send_message(
        chat_id=ORDER_SEND_CHAT,
        text=texts.NEW_DELIVERY(
            distance=distance,
            basket=basket, phone=phone
            ),
        reply_markup=buttons.NEW_DELIVERY(user_id, distance)
    )

    # send message succes fuly delivery
    await message.answer(texts.ORDER_SUCCES_SEND_ADMIN[user.lang], reply_markup=buttons.MAIN_MENU(lang=user.lang))

@dp.message_handler(content_types=['location'], state=Delivery.location)
async def delivery_location(message: Message, state: FSMContext):
    await create_task(delivery_location_task(message, state))