#  fikr yuborish tugmasining bo'lanish

from bot.management.commands.utils.functions import calculate_distance
from config.settings import KITCHEN_LAN, KITCHEN_LON


comment_name_uz = """
🖋 Ismingizni kiriting
"""

comment_name_cr = """
🖋 Исмингизни киритиш
"""

comment_name_ru = """
🖋 Введите свое имя
"""

comment_attribution_uz = \
"""
<b>✅ Yuborgan izohingiz adminga jo'natilda, ajratgan vaqtingiz uchun raxmat.</b>
"""

comment_attribution_cr = \
"""
<b>✅ Юборган изоҳингиз админга жўнатилда, ажратган вақтингиз учун рахмат.</b>
"""

comment_attribution_ru = \
"""
<b>✅ Комментарий, который вы отправляете, отправляется администратору, спасибо за уделенное время.</b>
"""

comment_cancel_uz = \
"""
<b>🛑Bekor qilish uchun ariza mavjud emas!</b>
"""


comment_cancel_cr =\
"""
<b>🛑Бекор қилиш учун ариза мавжуд емас!</b>
"""

comment_cancel_ru = \
"""
<b>🛑 Заявки на отмену работы нет!</b>
"""


comment_cancel_current_uz =\
"""
<b>🛑Joriy fikr bekor qilindi</b>
"""


comment_cancel_current_cr = \
"""
<b>🛑Жорий фикр бекор қилинди</b>
"""

comment_cancel_current_ru = \
"""
<b>🛑текущая идея отменена</b> 
"""

comment_error_uz = \
"""
<b>🤝 Iltimos pastdagi tugmalardan birini tanlang</b>
"""

comment_error_cr = \
"""
<b>🤝 Илтимос пастдаги тугмалардан бирини танланг</b>
"""

comment_error_ru = \
"""
<b>🤝 Пожалуйста, выберите одну из кнопок ниже</b>
"""


SUCCES_TAKE_UZ = """
<b>
✅ Buyurtma tasdiqlandi

Buyurtmangizni belgilang vaqta olib keting
Bizni tanlaganingiz uchun rahmat ☺️
</b>
"""

SUCCES_TAKE_CR = """
<b>
✅ Буюртма тасдиқланди

Буюртмангизни белгиланг вақта олиб кетинг
Бизни танлаганингиз учун раҳмат ☺️
</b>
"""

SUCCES_TAKE_RU = """
<b>
✅ Подтвержденный заказ

Отметьте свой заказ забрать время
Спасибо, что выбрали нас ☺ ️ 
</b>
"""


SUCCES_TAKE = {
    'uz': SUCCES_TAKE_UZ,
    'cr': SUCCES_TAKE_CR,
    'ru': SUCCES_TAKE_RU,
}

THAKS_SERVICES_UZ = """
<b>
👨🏻‍🍳 Bizning xizmatdamizdan foydalanganingiz uchun rahmat
Yoqimli ishtaxa hurmatli mijoz
</b>
"""

THAKS_SERVICES = {
    'uz': "Xabar yuborildi",
    'cr': "Xabar yuborildi",
    'ru': "Xabar yuborildi",
}

DELIVER_SPEED = """
<b>
🏃‍♂️ Kurierni tezligni belgilang
</b>
"""

ACCEPT_DELIVERY_UZ = """
<b>
✅ Buyurtmalaringiz yuborildi

🛵 Maxsulotlaringizni {} daqialardan so'ng yetib boradi
</b>
"""

ACCEPT_DELIVERY_CR = """
<b>
✅ Буюртмаларингиз юборилди

🛵 Махсулотларингизни {} дақиалардан сўнг етиб боради
</b>
"""

ACCEPT_DELIVERY_RU = """
<b>
✅ Ваши заказы отправлены

🛵 Товары поступят к вам после {} отправки в Dacia
</b>
"""

ACCEPT_DELIVERY = {
    'uz': ACCEPT_DELIVERY_UZ,
    'cr': ACCEPT_DELIVERY_CR,
    'ru': ACCEPT_DELIVERY_RU,
}


ORDER_SUCCES_SEND_ADMIN_UZ = """
<b>
✅ Sizning buyurtma yuborildi 
adminlarimiz tez orada javob berishadi
</b>
"""

ORDER_SUCCES_SEND_ADMIN_CR = """
<b>
✅ Сизнинг буюртма юборилди
админларимиз тез орада жавоб беришади
</b>
"""

ORDER_SUCCES_SEND_ADMIN_RU = """
<b>
✅ Ваш заказ отправлен 
наши админы скоро ответят
</b>
"""

ORDER_SUCCES_SEND_ADMIN = {
    "uz":ORDER_SUCCES_SEND_ADMIN_UZ,
    "cr":ORDER_SUCCES_SEND_ADMIN_CR,
    "ru":ORDER_SUCCES_SEND_ADMIN_RU
}

DELIVERY_DECLINE = "⚠️ Buyurtma nima sababdan bekor qilindi?"

NEW_DELIVER_ERROR_EMPTY_FOOD_UZ = """
<b>
Siz buyurtma qilgan maxsulotlar qolmaganligi saabali hozirda  buyurtmani yetkazib berolmaumiz 😔
Uzur so'raymiz xurmatli mijoz ❗️
</b>
"""

NEW_DELIVER_ERROR_EMPTY_FOOD_CR = """
<b>
Сиз буюртма қилган махсулотлар қолмаганлиги саабали ҳозирда буюртмани етказиб беролмаумиз 😔
хурматли мижоз❗️
</b>
"""

NEW_DELIVER_ERROR_EMPTY_FOOD_RU = """
<b>
Что не осталось товаров, которые вы заказали saabali в настоящее время мы не можем доставить заказ 😔
Уважаемый клиент ❗️
</b>
"""

NEW_DELIVER_ERROR_EMPTY_KURIER_UZ = """
<b>
Ayni vaqta bo'sh kurierlarimiz bo'lmaganligi sababli buyurtmani yetkazib berolmymiz. 😔
iltimos birozdan so'ng urinib ko'ring ❗️
</b>
"""

NEW_DELIVER_ERROR_EMPTY_KURIER_CR = """
<b>
Айни вақта бўш куриерларимиз бўлмаганлиги сабабли буюртмани етказиб беролмймиз. 😔
илтимос бироздан сўнг уриниб кўринг ❗️
</b>
"""

NEW_DELIVER_ERROR_EMPTY_KURIER_RU = """
<b>
Поскольку на данный момент у нас нет свободных курьеров, мы не можем доставить заказ. 😔
пожалуйста, попробуйте немного позже ❗ ️ 
</b>
"""

NEW_DELIVER_ERROR_OTHER_UZ = """
<b>
Noma'lum xatolik yuz berganligi sababli buyurtmani yetkazib berolmymiz. 😔
iltimos birozdan so'ng urinib ko'ring ❗️
</b>
"""

NEW_DELIVER_ERROR_OTHER_CR = """
<b>
Номаълум хато юз берганлиги сабабли сотиб олиб беролмаймиз. 😔
илтимос бироздан сўнг синаб кўринг ва текширинг.
</b>
"""

NEW_DELIVER_ERROR_OTHER_RU = """
<b>
Мы не можем доставить заказ из-за неизвестной ошибки. 😔
пожалуйста, сообщите об этом чуть позже ❗️
</b>
"""

NEW_DELIVER_ERROR = {
    'empty_food':{
        'uz':NEW_DELIVER_ERROR_EMPTY_FOOD_UZ,
        'cr':NEW_DELIVER_ERROR_EMPTY_FOOD_CR,
        'ru':NEW_DELIVER_ERROR_EMPTY_FOOD_RU,
    },
    'empty_kurier':{
        'uz':NEW_DELIVER_ERROR_EMPTY_KURIER_UZ,
        'cr':NEW_DELIVER_ERROR_EMPTY_KURIER_CR,
        'ru':NEW_DELIVER_ERROR_EMPTY_KURIER_RU,
    },
    'other':{
        'uz':NEW_DELIVER_ERROR_OTHER_UZ,
        'cr':NEW_DELIVER_ERROR_OTHER_CR,
        'ru':NEW_DELIVER_ERROR_OTHER_RU,
    }
}

def NEW_DELIVERY(**kwargs):
    new_order_message_text = ""
    total_price = 0
    
    for i in kwargs['basket']:
        price = i['count'] * i['food']['price']
        total_price += price

        new_order_message_text += f"{i['count']} X {i['food']['price']} so'm = {price}\n"

    new_order_message_text += f"\n\n"
    new_order_message_text += f"🛵 {kwargs['distance']:.2f} kilometer\n"
    new_order_message_text += f"💵 {total_price} so'm\n"
    new_order_message_text += f"📞 {kwargs['phone']}"

    return new_order_message_text

def NEW_DELIVERY(**kwargs):
    new_order_message_text = ""
    total_price = 0
    
    for i in kwargs['basket']:
        price = i['count'] * i['food']['price']
        total_price += price

        new_order_message_text += f"{i['count']} X {i['food']['price']} so'm = {price}\n"

    new_order_message_text += f"\n\n"
    new_order_message_text += f"🛵 {kwargs['distance']:.2f} kilometer\n"
    new_order_message_text += f"💵 {total_price} so'm\n"
    new_order_message_text += f"📞 {kwargs['phone']}"

    return new_order_message_text

def NEW_DELIVERY(**kwargs):
    new_order_message_text = ""
    total_price = 0
    
    for i in kwargs['basket']:
        price = i['count'] * i['food']['price']
        total_price += price

        new_order_message_text += f"{i['count']} X {i['food']['price']} so'm = {price}\n"

    new_order_message_text += f"\n\n"
    new_order_message_text += f"🛵 {kwargs['distance']:.2f} kilometer\n"
    new_order_message_text += f"💵 {total_price} so'm\n"
    new_order_message_text += f"📞 {kwargs['phone']}"

    return new_order_message_text



def NEW_TAKE(**kwargs):
    new_order_message_text = ""
    total_price = 0
    
    for i in kwargs['basket']:
        price = i['count'] * i['food']['price']
        total_price += price

        new_order_message_text += f"{i['count']} X {i['food']['price']} so'm = {price}\n"

    new_order_message_text += f"\n\n"
    new_order_message_text += f"💵 {total_price} so'm\n"
    new_order_message_text += f"📞 {kwargs['phone']}"

    return new_order_message_text


EMPTY_BASKET_UZ = """
<b>
Sizning savatchangiz bo'sh 😔
</b>
"""

EMPTY_BASKET = {
    "uz":EMPTY_BASKET_UZ,
    "ru":EMPTY_BASKET_UZ,
    "cr":EMPTY_BASKET_UZ,
}

comment_uz = """
Fikringizni kiriting
"""

comment_cr = """
Фикрингизни киритинг
"""

comment_ru = """
Введите свое мнение
"""

#  fikr yuborish tugmasining tugallanish


# Setting tugmasining bo'shlanish'

settings_text_uz = """
<b>Ma'lumotlarni o'zgartirish uchun quyidagi tugmalardan foydalanishingiz mumkin 👇</b>
"""

settings_text_cr = """
<b>Маълумотларни ўзгартириш учун қуйидаги тугмалардан фойдаланишингиз мумкин 👇</b>
"""

settings_text_ru = """
<b>Вы можете использовать следующие кнопки для изменения данных 👇</b>
"""

# Setting tugmasining tugallanish'

# ortga qaytish tugmasini bo'shlanishi'

back_uz = """
Asosiy menyuga qaytdingiz
"""

back_cr = """
Asosiy menyuga qaytdingiz
"""

back_ru = """
Asosiy menyuga qaytdingiz
"""

# ortga qaytish tugmasini tuggalanish'


# userlani ro'yhatdan o'tkazish bo'shlanishi'

LANGS = \
"""
<b>
Iltimos tilni tanlang
Илтимос тилни танланг
Пожалуйста, выберите язык
</b>
"""


PHONE_UZ = \
"""
📞 Iltimos telefon raqamingizni 

905650213

shaklida yuboring
yoki telefon raqamingiz ulashish tugmasini bosing
"""

PHONE_CR = \
"""
📞 Илтимос telefon рақамингизни 

905650213

шаклида юборинг
ёки telefon рақамингиз улашиш тугмасини босинг
"""

PHONE_RU = \
"""
📞 Пожалуйста ваш номер телефона 

905650213

отправить в виде
или нажмите кнопку поделиться своим номером телефона
"""

PHONE = {
    "uz": PHONE_UZ,
    "cr": PHONE_CR,
    "ru": PHONE_RU,
}

update_lang = \
"""
Til o'zgartirildi
"""



SUCCES_BASKET = {
    'uz':"<b>✅ Sizning maxsulotlaringiz savatga qo'shildi</b>",
    'cr':"<b>✅ Сизнинг махсулотларингиз саватга қўшилди</b>",
    'ru':"<b>✅ ваши товары добавлены в корзину</b>",
}

PHONE_ERROR_UZ =\
"""
<b>
❗️ Iltimos telefon raqamingizni to'g'ri kiriting

<code>1. Faqat raqamlardan foydalanish kerak</code>
<code>2. Uzunligi 9 ta raqamdan iborat bo'lishi kerak</code>
<code>3. Bo'sh joylar bo'lmasin</code>
</b>
"""

PHONE_ERROR_CR =\
"""
<b>
❗️ Илтимос telefon рақамингизни тўғри киритинг

<cоде>1. Фақат рақамлардан фойдаланиш керак</cоде>
<cоде>2. Узунлиги 9 та рақамдан иборат бўлиши керак</cоде>
<cоде>3. Бўш жойлар бўлмасин</cоде></b>
</b>
"""
PHONE_ERROR_RU =\
"""
<b>
❗ ️ Пожалуйста, введите свой номер телефона правильно

<code>1. Нужно использовать только цифры< / code>
<code>2. Длина должна быть 9 цифр< / code>
<code>3. Нет пробелов< / code>
</b>
"""

PHONE_ERROR = {
    'uz':PHONE_ERROR_UZ,
    'cr':PHONE_ERROR_CR,
    'ru':PHONE_ERROR_RU,
}

# userlani ro'yhatdan o'tkazish tugallanishi'

# Asosiy menyuni bo'shlanishi'

MAIN_MENU_UZ = \
"""
<b>
Xayrli kun {}
</b>
"""

MAIN_MENU_CR = """
Хайрли кун {}
"""

MAIN_MENU_RU = """
Добрый день {}
"""

MAIN_MENU = {
    'uz':MAIN_MENU_UZ,
    'cr':MAIN_MENU_CR,
    'ru':MAIN_MENU_RU,
}

lang_switch_handler_uz = \
"""
✅ Til muffaqiyatli almashtirildi

📝 Asosiy menyuga qaytingiz
"""

lang_switch_handler_cr = \
"""
✅ Тил муффақиятли алмаштирилди

📝 Асосий менюга қайтингиз
"""

lang_switch_handler_ru = \
"""
✅ Язык успешно заменен

📝 Вернуться в Главное меню
"""

phone_switch_handler_uz = \
"""
✅ Telifon raqam muffaqiyatli almashtirildi

📝 Asosiy menyuga qaytingiz
"""

phone_switch_handler_cr = \
"""
✅ Телифон рақам муффақиятли алмаштирилди

📝 Асосий менюга қайтингиз
"""

phone_switch_handler_ru = \
"""
✅ Телефон номер успешно заменен

📝 Вернуться в Главное меню
"""


# Asosiy menyuni tugallanishi'

# Categoryalarni bo'shlanishi'

CATEGORY_UZ = \
"""
<b>
Iltimos kategoriyani tanlang
</b>
"""

CATEGORY_CR = \
"""
<b>
Илтимос категорияни танланг
</b>
"""
CATEGORY_RU = \
"""
<b>
Пожалуйста, выберите категорию
</b>
"""

CATEGORY = {
    'uz':CATEGORY_UZ,
    'cr':CATEGORY_CR,
    'ru':CATEGORY_RU
}

FOODS = {
    "uz": "<b>Toifani va miqdorni tanlang 👇</b>",
    "cr": "<b>Тоифани ва микдорни танланг 👇</b>",
    "ru": "<b>Выберите еду и количество 👇</b>",
}




COUNT = \
"""
<b>🍟 {}</b>
<b>{}x</b>
{} X {} = {}
"""
# Categoryalarni tuggalanishi'
# phone switch

phone_switch_uz = \
"""
📞 Telifon Raqamni o'zgartirish uchun pastadagi tugmani bosing yoki yangi raqam kiriting
"""

phone_switch_cr = \
"""
📞 Телифон Рақамни ўзгартириш учун пастадаги тугмани босинг ёки янги рақам киритинг
"""

phone_switch_ru = \
"""
📞 Телефон нажмите кнопку в петле или введите новый номер, чтобы изменить номер
"""


# endswitch



# tilni almashtirish tugmasini bo'shlanishi'

lang_switch_uz = """
Tilni almashtirish
"""

lang_switch_cr = """
Тилни алмаштириш
"""

lang_switch_ru = """
Переключение языка
"""

# tilni almashtirish tugmasini tugallanishi'

location_uz = """
Manzilni kiriting
"""

location_cr = """
Манзилни киритинг
"""

location_ru = """
Введите адрес
"""

order_delivery_uz = """
Sizning buyurtmangiz Adminga jo'natildi
"""

order_delivery_cr = """
Сизнинг буюртмангиз Админга жўнатилди
"""

order_delivery_ru = """
Ваш заказ был отправлен администратору
"""

take_time_uz = """
<b>
Olib ketish vaqtini kiriting.
Misol uchun ➡️ <i>12:00</i>
</b>
"""

take_time_cr = """
Олиб кетиш вақтини киритинг
Мисол учун ➡️ <i>12:00</i>
"""

take_time_ru = """
<b>
Введите время получения.
Напримерol ➡️ <i>12:00</i>
</b>
"""

phone_rule_uz = """
📝 Iltimos raqamda kiriting
"""
phone_rule_cr = """
📝 Илтимос рақамда киритинг
"""
phone_rule_ru = """
📝 Введите номер
"""

phone_nomer_len_rule_uz = """
📞Telifon raqam eng kamida 9 ta sondan iborat bo'lish kerak❌
"""

phone_nomer_len_rule_cr = """
📞Телифон рақам енг камида 9 та сондан иборат бўлиш керак❌
"""

phone_nomer_len_rule_ru = """
📞Телефон номер должен состоять как минимум из 9 цифр❌
"""

your_basket_uz = \
"""
<b>🛒 Sizning maxsulotlaringiz</b> \n
"""


your_basket_cr = \
"""
<b>🛒 Сизнинг маҳсулотларингиз</b> \n
"""

your_basket_ru = \
"""
<b>🛒 Ваши продукты</b> \n
"""

contact_uz = \
"""
<b>☎️ Biz bilan bog'lanish uchun quyidagi raqamga telifon qilishingiz mumkin.!\n📞  940014741</b>
"""

contact_cr = \
"""
<b>☎️ Биз билан боғланиш учун қуйидаги рақамга телифон қилишингиз мумкин.!\н📞 940014741</b>
"""

contact_ru = \
"""
<b>☎ ️ Вы можете позвонить по следующему номеру, чтобы связаться с нами.!\n📞 940014741</b>
"""

information = \
"""
Milliondan ortiq mijozlar tashrif buyurgan! 

West Restorani haqida qisqacha,west restorani 2005 yildan o'z foalyatini boshlagan bo'lib, shu vaqt ichida milliondan ortiq tashrif buyuruvchilarga xizmat ko'rsatishga muvaffaq bo'ldik va nafaqat poytaxt aholisi, balki uning mehmonlari uchun ham diqqatga sazovor markazga aylandik!
West restoraning Manzili  Toshkent, Mirobod ko'chasi 1-etaj joylashgan. 
📞 Biz bilan bog'lanish uchun +998938870000

🕰 Ish soatlari

Dushanba: 11:00 – 01:00
Seshanba: 11:00 – 01:00
Chorshanba: 11:00 – 01:00
Payshanba: 11:00 – 01:00
Juma: 11:00 – 01:00
Shanba: 11:00 – 01:00
Yakshanba: 11:00 – 01:00



📝 O'ziga xos jihatlari!

🚗 Taomni tez va sifatli yetkazib berish
🚶‍♂️ Olib ketishingiz uchun o'z vaqtida  tayyorlab qo'yish
✅ Hamyonbop va sifatli taomlar!

Aniqroq ma'lumot va Manzilni ko'rish uchun pastdagi Malumotlarni ko'rish tugmasini bosing!

"""

location_info_uz = \
"""
https://yandex.uz/maps/10335/tashkent/house/YkAYdAFoT0QCQFprfX54dnpgZA==/?ll=69.268648%2C41.297337&z=19.22
"""



error_count_uz = \
"""
❌ Kechirasiz mahsulot sonini xato kiritingiz  qaytadan urinib ko'ring
"""



