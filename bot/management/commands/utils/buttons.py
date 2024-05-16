from aiogram.types import Message
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, \
                            ReplyKeyboardMarkup, KeyboardButton,\
                            ReplyKeyboardRemove

from django.db import models
from asgiref.sync import sync_to_async
from bot.management.commands.utils.functions import calc_delivered_time
from bot.models import User

# MAIN MENU UZ BUTTONS
BUYURTMA_BUTTON_UZ = '📦 Buyurtma berish'
FIKR_BUTTON_UZ = '✍️ Fikr bildirish'
BUYURTMALARIM_BUTTON_UZ = '📝 Mening Buyurmalarim'
SOZLAMALAR_BUTTON_UZ = '⚙️ Sozlamalar'
SHARTLAR_BUTTON_UZ = "ℹ️ Ma'lumot"

# MAIN MENU CR BUTTONS
BUYURTMA_BUTTON_CR = '📦 Буюртма бериш'  # Заказать
FIKR_BUTTON_CR = '✍️ Фикр билдириш'  # Предложить идею
BUYURTMALARIM_BUTTON_CR = '📝 Менинг Буюрмаларим'  # Мои заказы
SOZLAMALAR_BUTTON_CR = '⚙️ Созламалар'  # Настройки
SHARTLAR_BUTTON_CR = "ℹ️ Маълумот"  # Условия использования

# MAIN MENU RU BUTTONS
BUYURTMA_BUTTON_RU = '📦 Заказать'  
FIKR_BUTTON_RU = '✍️ Предложить идею'  
BUYURTMALARIM_BUTTON_RU = '📝 Мои Заказы'  
SOZLAMALAR_BUTTON_RU = '⚙️ Настройки'  
SHARTLAR_BUTTON_RU = "ℹ️ информация"

def DELIVER_SPEED(user_id, dis):    
    del_speed_3 = calc_delivered_time(dis, 3)
    del_speed_7 = calc_delivered_time(dis, 7)
    del_speed_20 = calc_delivered_time(dis, 20)
    del_speed_45 = calc_delivered_time(dis, 45)
    
    # send_deliver:-user_id:{}-del_time
    return InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [InlineKeyboardButton(f"🏃‍♂️ 1km/s - 5 km/s = {del_speed_3}", callback_data=f"s_deliver:-user_id:{user_id}-del_time:{del_speed_3}")],
        [InlineKeyboardButton(f"🚴 5km/s - 10 km/s = {del_speed_7}", callback_data=f"s_deliver:-user_id:{user_id}-del_time:{del_speed_7}")],
        [InlineKeyboardButton(f"🛵 10km/s - 30 km/s = {del_speed_20}", callback_data=f"s_deliver:-user_id:{user_id}-del_time:{del_speed_20}")],
        [InlineKeyboardButton(f"🚚 30km/s - 60 km/s = {del_speed_45}", callback_data=f"s_deliver:-user_id:{user_id}-del_time:{del_speed_3}")],
    ])


def REMOVE_TAKE(message_id, user_id):
    return InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [InlineKeyboardButton("🗑 Olib tashlash", callback_data=f"trash_take:{message_id}-user_id:{user_id}")]
    ])

def NEW_DELIVERY(user_id, distance):
    return InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [InlineKeyboardButton("✅ Qabul qilish", callback_data=f"y_new_d:-user_id:{user_id}-dis:{distance}")],
        [InlineKeyboardButton("❌ Rad etish", callback_data=f"n_new_d:-user_id:{user_id}")]
    ])

def NEW_COMMENT(user_id, distance):
    return InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [InlineKeyboardButton("✅ Qabul qilish", callback_data=f"y_new_d:-user_id:{user_id}-dis:{distance}")],
        [InlineKeyboardButton("❌ Rad etish", callback_data=f"n_new_d:-user_id:{user_id}")]
    ])
    
def NEW_TAKE(user_id):
    return InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [InlineKeyboardButton("✅ Qabul qilish", callback_data=f"t_succes:-user_id:{user_id}")],
        [InlineKeyboardButton("❌ Rad etish", callback_data=f"n_new_d:-user_id:{user_id}")]
    ])

def DECLINE_DELIVERY_STATUS(user_id, lang='uz'): 
    return InlineKeyboardMarkup(row_width=1, inline_keyboard=[
    [InlineKeyboardButton("Maxsulot qolmadi", callback_data=f"decline_status:empty_food-user_id:{user_id}-lang:{lang}")],
    [InlineKeyboardButton("Kurier yetishmasligi", callback_data=f"decline_status:empty_kurier-user_id:{user_id}-lang:{lang}")],
    [InlineKeyboardButton("Nomalum xatolik", callback_data=f"decline_status:other-user_id:{user_id}-lang:{lang}")],
])

def MAIN_MENU(lang='uz'):
    if lang == 'uz':
        return ReplyKeyboardMarkup(
            keyboard=[
                [
                    BUYURTMA_BUTTON_UZ
                ],
                [
                    FIKR_BUTTON_UZ,
                    BUYURTMALARIM_BUTTON_UZ
                ],
                [
                    SOZLAMALAR_BUTTON_UZ,
                    SHARTLAR_BUTTON_UZ
                ],
            ],
            resize_keyboard=True
        )
    
    if lang == 'cr':
        return ReplyKeyboardMarkup(
            keyboard=[
                [
                    BUYURTMA_BUTTON_CR
                ],
                [
                    FIKR_BUTTON_CR,
                    BUYURTMALARIM_BUTTON_CR
                ],
                [
                    SOZLAMALAR_BUTTON_CR,
                    SHARTLAR_BUTTON_CR
                ],
            ],
            resize_keyboard=True
        )
    
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                BUYURTMA_BUTTON_RU
            ],
            [
                FIKR_BUTTON_RU,
                BUYURTMALARIM_BUTTON_RU
            ],
            [
                SOZLAMALAR_BUTTON_RU,
                SHARTLAR_BUTTON_RU
            ],
        ],
        resize_keyboard=True
    )

def GET_CATEGORY(lang='uz'):
    if lang == 'uz':
        return InlineKeyboardMarkup(row_width=1, inline_keyboard=[
            [
                InlineKeyboardButton(text="🍽 Buyurtma berish", callback_data="category_redirect:"),
            ]
        ])
    elif lang == 'cr':
        return InlineKeyboardMarkup(row_width=1, inline_keyboard=[
            [
                InlineKeyboardButton(text="🍽 Буюртма бериш", callback_data="category_redirect:"),
            ]
        ])
    else:
        return InlineKeyboardMarkup(row_width=1, inline_keyboard=[
            [
                InlineKeyboardButton(text="🍽 Заказать", callback_data="category_redirect:"),
            ]
        ])

def COUNTER_MENU(food_id, category_id, count, lang='uz'):
    calc_buttons = [
        [
            InlineKeyboardButton(text="+1", callback_data=f"food:{food_id}/category:{category_id}/number:1"),
            InlineKeyboardButton(text="+2", callback_data=f"food:{food_id}/category:{category_id}/number:2"),
            InlineKeyboardButton(text="+3", callback_data=f"food:{food_id}/category:{category_id}/number:3"),
        ],
        [
            InlineKeyboardButton(text="-1", callback_data=f"food:{food_id}/category:{category_id}/number:-1"),
            InlineKeyboardButton(text="-2", callback_data=f"food:{food_id}/category:{category_id}/number:-2"),
            InlineKeyboardButton(text="-3", callback_data=f"food:{food_id}/category:{category_id}/number:-3"),
        ],
    ]
    
    if lang == 'uz':
        calc_buttons.append([
                InlineKeyboardButton(text="⬅️ Orqaga", callback_data="category:" + category_id),
            ])
        calc_buttons.append([
                InlineKeyboardButton(text="🛒 Savatcha qo'shish", callback_data=f"basket:start-food:{food_id}-category:{category_id}-number:{count}"),
            ])

    elif lang == 'cr':
        calc_buttons.append([
                InlineKeyboardButton(text="⬅️ Орқага", callback_data="category:" + category_id),
            ])
        calc_buttons.append([
                InlineKeyboardButton(text="🛒 Саватча қўшиш", callback_data=f"basket:{food_id},{count}"),
            ])
    else:
        calc_buttons.append([
                InlineKeyboardButton(text="⬅️ Назад", callback_data="category:" + category_id),
            ])
        calc_buttons.append([
                InlineKeyboardButton(text="🛒 Добавить в корзину", callback_data=f"basket:{food_id}-count:{count}"),
            ])
            
    return InlineKeyboardMarkup(inline_keyboard=calc_buttons)

    
REGISTER_BUTTON = "📝 Ro'yxatdan o'tish"
REGISTER = ReplyKeyboardMarkup(
    keyboard=[
        [
            REGISTER_BUTTON
        ]
    ],
     resize_keyboard=True
)

UZ_BUTTON = "🇺🇿 O'zbekcha"
CR_BUTTON = "🇺🇿 Ўзбекча"
RU_BUTTON = "🇷🇺 Русский"


LANG = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=UZ_BUTTON,
                callback_data="uz"
            )
        ],
        [
            InlineKeyboardButton(
                text=CR_BUTTON,
                callback_data='cr'
            )
        ],
        [
            InlineKeyboardButton(
                text=RU_BUTTON,
                callback_data="ru"
            )
        ],
    ]
)
TIL_SOZLAMALARI_BUTTON_UZ = "🔄 Tilni o'zgartirish"
TIL_SOZLAMALARI_BUTTON_CR = "🔄 Тилни ўзгартириш"
TIL_SOZLAMALARI_BUTTON_RU = "🔄 Смена языка"

PHONE_SWITCH_UZ = "📞 Telifon raqamni o'zgartirish"
PHONE_SWITCH_CR = "📞 Телифон рақамни ўзгартириш"
PHONE_SWITCH_RU = "📞 Смена номера телефона"

ORTGA_BUTTON_UZ = "🔙 Ortga"
ORTGA_BUTTON_CR = "🔙 Ортга"
ORTGA_BUTTON_RU = "🔙 Назад"


SETTINGS_MENYU_UZ = ReplyKeyboardMarkup(
    keyboard=[
        [
            TIL_SOZLAMALARI_BUTTON_UZ,
        ],
        [
            PHONE_SWITCH_UZ
        ],
        [
            ORTGA_BUTTON_UZ
        ]
    ],
    resize_keyboard=True
)

SETTINGS_MENYU_CR = ReplyKeyboardMarkup(
    keyboard=[
        [
            TIL_SOZLAMALARI_BUTTON_CR,
        ],
        [
            PHONE_SWITCH_CR
        ],
        [
            ORTGA_BUTTON_CR
        ]
    ],
    resize_keyboard=True
)

SETTINGS_MENYU_RU = ReplyKeyboardMarkup(
    keyboard=[
        [
            TIL_SOZLAMALARI_BUTTON_RU,
        ],
        [
            PHONE_SWITCH_RU
        ],
        [
            ORTGA_BUTTON_RU
        ]
    ],
    resize_keyboard=True
)

ORTGA_MAIN_BUTTON_UZ = '🔙 Ortga'
ORTGA_MAIN_BUTTON_CR = '🔙 Ортга'
ORTGA_MAIN_BUTTON_RU = '🔙 Назад'




BACK_UZ = ReplyKeyboardMarkup(
    keyboard=[
        [
            ORTGA_MAIN_BUTTON_UZ
        ],
    ],
    resize_keyboard=True,
)

BACK_CR = ReplyKeyboardMarkup(
    keyboard=[
        [
            ORTGA_MAIN_BUTTON_CR
        ],
    ],
    resize_keyboard=True,
)

BACK_RU = ReplyKeyboardMarkup(
    keyboard=[
        [
            ORTGA_MAIN_BUTTON_RU
        ],
    ],
    resize_keyboard=True,
)

HA_BUTTON_UZ = "✅ Ha"
YOQ_BUTTON_UZ = "❌ Yoq"
ORTGA_BUTTON_UZ = "🔙 Ortga"

HA_BUTTON_CR = "✅ Ҳа"
YOQ_BUTTON_CR = "❌ Ёқ"
ORTGA_BUTTON_CR = "🔙 Ортга"

HA_BUTTON_RU = "✅ Ha"
YOQ_BUTTON_RU = "❌ нет"
ORTGA_BUTTON_RU = "🔙 назад"


REFFERAL_REQUEST_UZ = ReplyKeyboardMarkup(
    keyboard=[
        [
            HA_BUTTON_UZ,
            YOQ_BUTTON_UZ
        ],
        [
            ORTGA_BUTTON_UZ
        ]
    ],
    resize_keyboard=True,
)

REFFERAL_REQUEST_CR = ReplyKeyboardMarkup(
    keyboard=[
        [
            HA_BUTTON_CR,
            YOQ_BUTTON_CR
        ],
        [
            ORTGA_BUTTON_CR
        ]
    ],
    resize_keyboard=True,
)

REFFERAL_REQUEST_RU = ReplyKeyboardMarkup(
    keyboard=[
        [
            HA_BUTTON_RU,
            YOQ_BUTTON_RU
        ],
        [
            ORTGA_BUTTON_RU
        ]
    ],
    resize_keyboard=True,
)

# CONTACT_BUTTON = KeyboardButton(text="Запросить контакт", request_contact=True)
# CONTACT = ReplyKeyboardMarkup(resize_keyboard=True).add(CONTACT_BUTTON)

CONTACT = {
    "uz": ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="📞 Jo'natish", request_contact=True)
            ]
        ],
        resize_keyboard=True
    ),
    "cr": ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="📞 Жўнатиш", request_contact=True)
            ]
        ],
        resize_keyboard=True
    ),
    "ru": ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="📞 Отправить", request_contact=True)
            ]
        ],
        resize_keyboard=True
    )
}

def SUCCES_BASKET(lang='uz'):
    if (lang=='uz'):
        return InlineKeyboardMarkup(row_width=1, inline_keyboard=[
            [
                InlineKeyboardButton(text="🛒 Savatchaga o'tish", callback_data="get_backet:")
            ],
            [
                InlineKeyboardButton(text="🍟 Haridni davom etish", callback_data="category_redirect:")
            ]
        ])

    if (lang=='ск'):
        return InlineKeyboardMarkup(row_width=1, inline_keyboard=[
            [
                InlineKeyboardButton(text="🛒 Саватчага ўтиш", callback_data="get_backet:")
            ],
            [
                InlineKeyboardButton(text="🍟 Ҳаридни давом етиш", callback_data="category_redirect:")
            ]
        ])
        
    return InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [
            InlineKeyboardButton(text="🛒 Перейти в корзину", callback_data="get_backet:")
        ],
        [
            InlineKeyboardButton(text="🍟 Продолжение покупки", callback_data="category_redirect:")
        ]
    ])

LOCATION_UZ = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🕹 Manzilni yuborish", request_location=True)
            ]
        ],
        resize_keyboard=True
    )

LOCATION_CR = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🕹 Манзилни юбориш", request_location=True)
            ]
        ],
        resize_keyboard=True
    )

LOCATION_RU = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🕹 Отправить адрес", request_location=True)
            ]
        ],
        resize_keyboard=True
    )



TAKE_PHONE_UZ = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="📞 Jo'natish", request_contact=True)
            ]
        ],
        resize_keyboard=True
    )

TAKE_PHONE_CR = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="📞 Жўнатиш", request_contact=True)
            ]
        ],
        resize_keyboard=True
    )

TAKE_PHONE_RU = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="📞 Отправить", request_contact=True)
            ]
        ],
        resize_keyboard=True
    )

def CATEGORY_BUTTONS(lang='uz', category=None):
    categoey_buttons_array = []
    if (lang == "uz"):
        for i in category:
            categoey_buttons_array.append(
                InlineKeyboardButton(text=i.name_uz, callback_data="category:" + str(i.id)),
            )
    elif (lang == "cr"):
        for i in category:
            categoey_buttons_array.append(
                InlineKeyboardButton(text=i.name_cr, callback_data="category:" + str(i.id)),
            )
    else:
        for i in category:
            categoey_buttons_array.append(
                InlineKeyboardButton(text=i.name_ru, callback_data="category:" + str(i.id)),
            )
            
    categoey_buttons = InlineKeyboardMarkup(row_width=2)
    categoey_buttons.add(*categoey_buttons_array)
            
    return categoey_buttons




def FOODS(lang='uz', foods=None, category_id=None):
    foods_buttons_list = []
    
    if (lang == "uz"):
        for i in foods:
            foods_buttons_list.append(
                InlineKeyboardButton(text=i.name_uz, callback_data=f"food:{i.id}/category:{category_id}/number:1"),
            )
    elif (lang == "cr"):
        for i in foods:
            foods_buttons_list.append(
                InlineKeyboardButton(text=i.name_cr, callback_data=f"food:{i.id}/category:{category_id}/number:1"),
            )
    else:
        for i in foods:
            foods_buttons_list.append(
                InlineKeyboardButton(text=i.name_ru, callback_data=f"food:{i.id}/category:{category_id}/number:1"),
            )
    
    foods_buttons = InlineKeyboardMarkup(row_width=2)
    foods_buttons.add(*foods_buttons_list)
    foods_buttons.add(
        InlineKeyboardButton(text="⬅️ Orqaga", callback_data="category_redirect:"),
    )

    return foods_buttons


information_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🕹 Manzilni ko'rish")
        ]
    ],
    resize_keyboard=True
)






