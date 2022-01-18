from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InputFile

import logging

from config import TOKEN

import os
from os.path import isfile, join

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)



@dp.message_handler(commands=["start"])
async def process_start_command(message: types.Message):
    await message.reply(
        "Привет! Меня зовут MathHelp и я могу помочь тебе с подготовкой к ЕГЭ по математике!\nНажми /go, чтобы начать"
    )
    #list_of_dirs: list = list()
    #mypath = "./maths/"
    #for dirname in os.listdir(mypath):
    #    names = dirname.split("-")
    #    list_of_dirs.append((names[1], "folder:" + names[0]))

    #keyboard_markup = types.InlineKeyboardMarkup(row_width=1)
    #row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in list_of_dirs)
    #keyboard_markup.add(*row_btns)
    #await message.reply('Нажми go, чтобы начать или help - он поможет тебе освоиться здесь', reply_markup=keyboard_markup)


@dp.message_handler(commands='go')
async def process_start_command(message: types.Message):
    await message.reply(
            "Для того, чтобы получить файл со всеми формулами жми /formula. Для того, чтобы решить задачи/примеры жми /task"
    )



@dp.message_handler(commands='formula')
async def process_start_command(message: types.Message):
    list_of_dirs: list = list()
    mypath = "./формула/"
    for dirname in os.listdir(mypath):
        names = dirname.split("-")
        list_of_dirs.append((names[1], "folder:" + names[0]))

    keyboard_markup = types.InlineKeyboardMarkup(row_width=1)
    row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in list_of_dirs)
    keyboard_markup.add(*row_btns)
    await message.reply('Основные формулы', reply_markup=keyboard_markup)


@dp.message_handler(commands='task')
async def process_start_command(message: types.Message):
    list_of_dirs: list = list()
    mypath = "./задания/"
    for dirname in os.listdir(mypath):
        names = dirname.split(".")
        list_of_dirs.append((names[1], "folder:" + names[0]))

    keyboard_markup = types.InlineKeyboardMarkup(row_width=1)
    row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in list_of_dirs)
    keyboard_markup.add(*row_btns)
    await message.reply('Выберите нужную тему', reply_markup=keyboard_markup)

#@dp.callback_query_handler()
#async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
#    buttons: list = list()
#    answer_data = query.data
#    await query.answer(f"You answered with {answer_data!r}")
#    keyboard_markup = types.InlineKeyboardMarkup(row_width=1)
#    print(f"{answer_data=}")

#    _tpath = answer_data.split(":")

#    if _tpath[0] == "folder":
#        paths = _deocde_to_paths(answer_data)
#        dir_name = "/".join(paths)
#        tg_path = [x.split("-")[0] for x in paths[1:]]
#
#        buttons = _get_listdir(dir_name, tg_path)
#
#        row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in buttons)
#        keyboard_markup.add(*row_btns)
#        await bot.edit_message_reply_markup(
#            query.from_user.id,
#            message_id=query.message.message_id,
#            # "Выбери тему",
#            reply_markup=keyboard_markup,
#        )

#    elif _tpath[0] == "file":
#        paths = _deocde_to_paths(answer_data)
#        file_name = "/".join(paths)

#        dir_name = "/".join(paths[:-1])
#        tg_path = [x.split("-")[0] for x in paths[1:-1]]

#        buttons = _get_listdir(dir_name, tg_path)

#        row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in buttons)

#        keyboard_markup.add(*row_btns)
#       fl = InputFile(file_name)
#        await bot.send_document(
#            query.from_user.id,
#            document=fl,
#            reply_markup=keyboard_markup,
#        )


def _get_listdir(path: str, tg_path: list) -> list:
    buttons = list()
    for cf in os.listdir(path):
        _path = os.path.join(path, cf)
        if os.path.isfile(_path):
            buttons.append(("⬇️ " + cf, "file:" + ":".join(tg_path) + ":" + cf))
        else:
            names = cf.split("-")
            buttons.append(("📁 " + names[1], "folder:" + ":".join(tg_path) + ":" + names[0]))
    return buttons


def _deocde_to_paths(answer_data: str) -> list:
    tpath = answer_data.split(":")
    paths = ["maths"]
    _fpath = tpath[1:]
    for d in _fpath:
        try:
            dir_name = list(filter(lambda x: x.startswith(f"{d}-"), os.listdir("/".join(paths))))[0]
            print(f"{d}->{dir_name}")
            paths.append(dir_name)
        except:
            paths.append(d)
    return paths


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)