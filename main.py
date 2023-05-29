# -*- coding: utf-8 -*-

import os
from collections import Counter
import logging
import sys
from typing import List

logger = logging.getLogger("logger")
console_out = logging.StreamHandler(stream=sys.stdout)
logging.basicConfig(
    handlers=[console_out],
    level=logging.INFO,
    format='%(asctime)s / %(levelname)s / %(message)s',
    datefmt='%H:%M:%S'
)


def count_symbols(string: str) -> List[tuple]:
    """The function returns a list of tuples in which the character
    is indicated and how many times it occurs in the text"""
    dict_counter = Counter(string)
    del dict_counter["\n"]
    del dict_counter[" "]
    return dict_counter.most_common()


def open_text(path: str) -> None:
    """Function for reading a file"""
    try:
        with open(path, 'r') as file:
            read_file = file.read()
            logger.info("Файл прочитан, идет анализ. Ожидайте ....")
            len_text: int = len(read_file)
            _histogram: list = count_symbols(read_file)

            for item in _histogram:
                print(f"{item[0]} -- {round(item[1] / len_text * 100, 4)}%")
    except (UnicodeDecodeError, UnicodeError):
        logger.error("Файл закодирован не в utf-8 (")
        return


def search_file(file, path="/") -> None:
    """Function to search for a file in the system"""
    logger.info("Идет поиск файла ожидайте...")
    for parent_path, _, files in os.walk(path):
        if file in files:
            path_to_file: str = os.path.join(parent_path, file)
            logger.info("Файл найден и отправлен на чтение.")
            open_text(path_to_file)
            break
    else:
        logger.error("Файл не найден, проверьте правильность ввода!")


def input_file() -> None:
    """Function to get file name"""
    logger.info("Сейчас необходимо будет ввести имя файла.")
    file: str = input("Введите имя файла: ")
    search_file(file)


if __name__ == "__main__":
    input_file()
