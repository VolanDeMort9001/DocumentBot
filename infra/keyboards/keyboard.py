from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from commands.create_document import MO_sample_list, CO_sample_list


def choose_format() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text="МО", callback_data="MO"), InlineKeyboardButton(text="СО", callback_data="CO")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_MO_sample_menu(indexes: list[bool]) -> InlineKeyboardMarkup:
    #Создание документа
    buttons = [
        [InlineKeyboardButton(text=MO_sample_list[i][1], callback_data=str(f"MO_sample {i}"))] for i in range(len(indexes)) if indexes[i]
    ]
    if not all(indexes):
        buttons.append([InlineKeyboardButton(text="Закончить отчет", callback_data="create_MO_summary")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_CO_sample_menu(indexes: list[bool]) -> InlineKeyboardMarkup:
    #Создание документа
    buttons = [
        [InlineKeyboardButton(text=CO_sample_list[i][1], callback_data=str(f"CO_sample {i}"))] for i in range(len(indexes)) if indexes[i]
    ]
    if not all(indexes):
        buttons.append([InlineKeyboardButton(text="Закончить отчет", callback_data="create_CO_summary")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)