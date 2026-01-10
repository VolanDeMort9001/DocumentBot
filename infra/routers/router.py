from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import Command
from commands.create_document import samples, create_doc
from infra.keyboards.keyboard import get_sample_menu

router = Router()

indexes = [True for i in range(len(samples))]

@router.message(Command("start"))
async def start_menu(message: Message) -> None:
    global indexes
    indexes = [True] * len(samples)
    await message.answer("Здравствуй!\nЯ помогу тебе с написанием шаблонных отчетов по работе\n"
                   "Выбери, какие шаблоны ты хочешь добавить:", reply_markup=get_sample_menu(indexes))


@router.callback_query(F.data.startswith("sample"))
async def process_sample(cb: CallbackQuery) -> None:
    index = int(cb.data.split()[1])
    indexes[index] = False
    await cb.message.edit_text("Отлично!\nМожешь выбрать еще шаблоны из списка или закончить отчет.", reply_markup=get_sample_menu(indexes))
    await cb.answer()

@router.callback_query(F.data == "create_summary")
async def summary(cb: CallbackQuery) -> None:
    create_doc(indexes)
    await cb.message.edit_text("Ваш отчет создается...")
    await cb.message.answer_document(
        FSInputFile("/Users/aleknazarov9001/PycharmProjects/DocumentBot/infra/ABS_отчет.docx"),
        caption="Ваш отчет готов! Для создания нового документа напишите /start"
    )
    await cb.answer()
