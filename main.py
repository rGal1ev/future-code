from aiogram import Bot, Dispatcher
from asyncio import run
from aiogram.filters import CommandStart, CommandObject, Command
from aiogram.types import Message, InlineKeyboardButton, CallbackQuery, BufferedInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram import F

from io import BytesIO
from works import works
from random import sample
from tests import first_module_test

TOKEN = "6910497477:AAGADRjvLUPxLTf0EAH4_0u2QAT5xNhT37E"
dp = Dispatcher()


class Form(StatesGroup):
    work_id = State()
    name = State()


def string_to_io_bytes(string):
    content = string.encode('utf-8')

    io_bytes = BytesIO()
    io_bytes.write(content)
    io_bytes.seek(0)

    return io_bytes


@dp.message(CommandStart())
async def handle_start(message: Message):
    builder = InlineKeyboardBuilder()

    for work in works:
        builder.row(InlineKeyboardButton(
            text=work.get("name"),
            callback_data=str(work.get("id"))
        ))

    await message.answer("📃 *Выберите работу*\n\nДля получения всех самостоятельных /all\n\nДля того, чтобы получить ответ на вопросы аттестации первого модуля используйте команду /q номер-вопроса", reply_markup=builder.as_markup())


@dp.callback_query(F.data)
async def handle_work(callback: CallbackQuery, state: FSMContext):
    work_id = int(callback.data)

    await state.update_data(work_id=work_id)
    await state.set_state(Form.name)
    await callback.message.answer("🏌️‍♂️ *Напишите свое имя*")
    await callback.answer()


@dp.message(Form.name)
async def handle(message: Message, state: FSMContext):
    data = await state.update_data(name=message.text)
    await state.clear()

    if data.get("work_id") != "all":
        work_to_process = None

        for work in works:
            if work.get("id") == data.get("work_id"):
                work_to_process = work

        random_tasks = sample(work_to_process.get("tasks"), work_to_process.get("task_count"))
        random_tasks_bytes = ' '.join(random_tasks).encode("UTF-8")

        await message.answer(text=f"*Самостоятельная работа {data.get('work_id')}*\n\n*Случайных заданий:* `{len(random_tasks)}`\n*Указанное имя:* `{data.get('name')}`\n\n*Если есть логин и пароль*, отправить [сюда](https://online-vstu.ru/login/)\n*Если нет*, то [сюда](https://almetpt.ru/moodle/)",
                             disable_web_page_preview=True)

        await message.answer(text=f"```python{' '.join(random_tasks)}\n```")

        await message.answer_document(BufferedInputFile(random_tasks_bytes, filename=f"Самостоятельная {work_to_process.get('id')} {data.get('name')}.py"))

    else:
        await message.answer(
            text=f"*{len(works)} Самостоятельных работ*\n*Указанное имя:* `{data.get('name')}`\n\n*Если есть логин и пароль*, отправить задания [сюда](https://online-vstu.ru/login/)\n*Если нет*, то [сюда](https://almetpt.ru/moodle/)",
            disable_web_page_preview=True)

        for work in works:
            random_tasks = sample(work.get("tasks"), work.get("task_count"))
            random_tasks_bytes = ' '.join(random_tasks).encode("UTF-8")

            await message.answer_document(BufferedInputFile(random_tasks_bytes, filename=f"Самостоятельная {work.get('id')} {data.get('name')}.py"))


@dp.message(Command("all"))
async def handle_all_works(message: Message, state: FSMContext):
    await state.update_data(work_id="all")

    await state.set_state(Form.name)
    await message.answer("🏌️‍♂️ *Напишите свое имя*\n\n_Получение всех самостоятельных_")


@dp.message(Command("q"))
async def handle_test_question(message: Message, command: CommandObject):
    question_id = int(command.args)
    answer = None

    for question in first_module_test:
        if question.get("id") == question_id:
            answer = question.get("answer")

    if answer is None:
        await message.answer("*Вопроса с таким номер нет в тесте*")
        return

    await message.answer(f"👁️ *Ответ на {question_id} вопрос*\nСкопируйте или допишите ответ на сайте")
    await message.answer(f"```python\n{answer}```")


async def main() -> None:
    bot = Bot(TOKEN, parse_mode="Markdown")
    await dp.start_polling(bot)


if __name__ == "__main__":
    run(main())
