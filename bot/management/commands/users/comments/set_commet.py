from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from ...loader import dp, bot
from ...utils import buttons
from aiogram import Bot
from ...utils import texts
from asgiref.sync import sync_to_async
from bot.models import User
from ...state import Comments
from asyncio import create_task




async def set_comment_task(message: Message, state: FSMContext):
    user_id = message.from_user.id

    try:
        user = await sync_to_async(User.objects.get)(user_id=user_id)
    except:
        raise Exception("User topilmadi")
    if (user.lang == 'uz'):
        await state.update_data(comment_at=message.text)
        data = await state.get_data()
        comment_an = (f"Murojatchi {data.get('name')}\n"
                      f"📨 Izoh: ({data.get('comment_at')}")
        await message.answer(f"<b>🚀 Izohingizni Yuboraveraymi?</b>\n\n{comment_an}\n\n Pastdagi so'rovlardan birini yuboring 👇", parse_mode='HTML', reply_markup=buttons.REFFERAL_REQUEST_UZ)

    if (user.lang == 'cr'):
        await state.update_data(comment_at=message.text)
        data = await state.get_data()
        comment_an = (f"Мурожатчи {data['name']}\n"
                      f"📨 Изоҳ: ({data.get('comment_at')}")
        await message.answer(f"<b>🚀 Изоҳингизни Юбораверайми?</b>\n\n{comment_an}\n\n Пастдаги сўровлардан бирини юборинг 👇", parse_mode='HTML', reply_markup=buttons.REFFERAL_REQUEST_CR)
    await state.set_state(Comments.register_commit)

    if (user.lang == 'ru'):
        await state.update_data(comment_at=message.text)
        data = await state.get_data()
        comment_an = (f"Заявитель {data['name']}\n"
                      f"📨 Примечание: ({data.get('comment_at')}")
        await message.answer(f"<b>🚀 могу Я отправить ваш комментарий?</b>\n\n{comment_an}\n\n отправить один из следующих запросов 👇", parse_mode='HTML', reply_markup=buttons.REFFERAL_REQUEST_RU)






@dp.message_handler(content_types=['text'], state=Comments.comment)
async def comment(message: Message, state: FSMContext):
    create_task(set_comment_task(message, state))