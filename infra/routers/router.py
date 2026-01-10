from pyexpat.errors import messages

import aiogram
from aiogram.types import CallbackQuery, Message
from aiogram import Router, F
from aiogram.filters import Command
from commands.create_document import samples
from infra.keyboards.keyboard import get_sample_menu

router = Router()

indexes = [True for i in range(len(samples))]

@router.message(Command("start"))
def start_menu(message: Message):
    message.answer("Здравствуй!\nЯ помогу тебе с написанием шаблонных отчетов по работе. "
                   "Выбери, какие шаблоны ты хочешь добавить:", reply_markup=get_sample_menu(indexes))


@router.callback_query(F.data.startswith("sample"))
def process_sample(cb: CallbackQuery):
    index = int(F.data.split()[1])
    indexes[index] = False
    cb.message.answer("Отлично!\nМожешь выбрать еще шаблоны из списка или закончить отчет.", reply_markup=get_sample_menu(indexes))
    cb.answer()
