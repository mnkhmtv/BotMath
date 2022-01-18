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


@dp.message_handler(commands='go')
async def process_start_command(message: types.Message):
    await message.reply(
            "Для того, чтобы получить файл со всеми формулами жми /formula. Для того, чтобы решить задачи/примеры жми /task"
    )


@dp.message_handler(commands='back')
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
    mypath = "./Темы/"
    for dirname in os.listdir(mypath):
        names = dirname.split(".")
        list_of_dirs.append(names[1])
    # не выводит кнопки, вроде с циклом все ок..
    # нажимая на кнопку с темой рандомным образом выбирается задача,
    # НО к ней еще нужно привязать кнопку с ответом на нее..
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1)
    row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in list_of_dirs)
    keyboard_markup.add(*row_btns)
    await message.reply('Выберите нужную тему или нажми /back чтобы вернуться в главное менюю', reply_markup=keyboard_markup)


@dp.message_handler(commands='answer')
async def process_start_command(message: types.Message):
    ist_of_dirs: list = list()
    mypath = "./Темы/Ответы/"
    # здесь нужно достать спарсенные ответы на задачи (как?)


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