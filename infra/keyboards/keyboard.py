from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from commands.create_document import samples



def get_sample_menu(indexes: list[bool]) -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text=samples[i][1], callback_data=str(f"sample {i}"))] for i in range(len(indexes)) if indexes[i]
    ]
    if not all(indexes):
        buttons.append([InlineKeyboardButton(text="Закончить отчет", callback_data="create_summary")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)