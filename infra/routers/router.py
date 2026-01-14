from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import Command
from commands.create_document import MO_sample_list, CO_sample_list, create_doc
from infra.keyboards.keyboard import get_MO_sample_menu, get_CO_sample_menu, choose_format

router = Router()

MO_indexes = [True for i in range(len(MO_sample_list))] #Хранилище индексов оставшихся шаблонов отчетов МО
CO_indexes = [True for i in range(len(CO_sample_list))] #Хранилище индексов оставшихся шаблонов отчетов СО

@router.message(Command("start"))
async def start_menu(message: Message) -> None:
    global CO_indexes
    global MO_indexes
    MO_indexes = [True] * len(MO_sample_list)
    CO_indexes = [True] * len(CO_sample_list)
    await message.answer("Здравствуй!\nЯ помогу тебе в создании шаблонного отчета.", reply_markup=choose_format())
    
@router.callback_query(F.data == "CO")
    # Стартовое меню для начала создания отчета СО
async def CO_choose_menu(cb: CallbackQuery):
    global MO_indexes
    MO_indexes = [True] * len(MO_sample_list)
    await cb.message.edit_text("Отлично! Создадим шаблонный отчет СО.\n"
                                 "Выбери, какие шаблоны ты хочешь добавить:",
                                 reply_markup=get_CO_sample_menu(CO_indexes))

@router.callback_query(F.data.startswith("CO_sample"))
async def process_CO_samples(cb: CallbackQuery) -> None:
    # Обновленное меню с возможностью завершения отчета СО и с несколькими пропавшими шаблонами
    global MO_indexes
    MO_indexes = [True] * len(MO_sample_list)
    index = int(cb.data.split()[1])
    CO_indexes[index] = False
    await cb.message.edit_text("Отлично!\nМожешь выбрать еще шаблоны из списка или закончить отчет.",
                               reply_markup=get_CO_sample_menu(CO_indexes))
    await cb.answer()

@router.callback_query(F.data == "MO")
async def MO_choose_menu(cb: CallbackQuery):
    #Стартовое меню для начала создания отчета МО
    global CO_indexes
    CO_indexes = [True] * len(CO_sample_list)
    await cb.message.edit_text("Отлично! Создадим шаблонный отчет МО.\n"
                                 "Выбери, какие шаблоны ты хочешь добавить:", 
                                 reply_markup=get_MO_sample_menu(MO_indexes))

@router.callback_query(F.data.startswith("MO_sample"))
async def process_MO_samples(cb: CallbackQuery) -> None:
    #Обновленное меню с возможностью завершения отчета МО и с несколькими пропавшими шаблонами
    global MO_indexes
    CO_indexes = [True] * len(CO_sample_list)
    index = int(cb.data.split()[1])
    MO_indexes[index] = False
    await cb.message.edit_text("Отлично!\nМожешь выбрать еще шаблоны из списка или закончить отчет.", 
                               reply_markup=get_MO_sample_menu(MO_indexes))
    await cb.answer()

@router.callback_query(F.data == "create_MO_summary")
async def MO_summary(cb: CallbackQuery) -> None:
    #Создание и отправка документа
    create_doc(MO_indexes)
    await cb.message.edit_text("Ваш отчет создается...")
    await cb.message.answer_document(
        FSInputFile("/Users/aleknazarov9001/PycharmProjects/DocumentBot/infra/ABS_отчет.docx"),
        caption="Ваш отчет готов! Для создания нового документа нажмите /start"
    )
    await cb.answer()

@router.callback_query(F.data == "create_CO_summary")
async def CO_summary(cb: CallbackQuery) -> None:
    #Создание и отправка документа
    create_doc(CO_indexes)
    await cb.message.edit_text("Ваш отчет создается...")
    await cb.message.answer_document(
        FSInputFile("/Users/aleknazarov9001/PycharmProjects/DocumentBot/infra/ABS_отчет.docx"),
        caption="Ваш отчет готов! Для создания нового документа нажмите /start"
    )
    await cb.answer()
