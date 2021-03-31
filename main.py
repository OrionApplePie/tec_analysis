import argparse
import errno
import os
from pathlib import Path

import pandas as pd

# Параметры которые нужны
NEEDED_PARAMETERS = (
    "hmax",
    "FiltWindow",
    "Time Range",
    "Minimum duration of series",
    "time step"
)


def get_params(filename=""):
    """Функция для сбора параметров из файла .dat
    из строк в начале файла начинающихся с символа #.
    Возвращает словарь.
    """
    if not filename:
        raise ValueError("Filename is needed.")

    if not os.path.isfile(filename):
        raise FileNotFoundError(
            errno.ENOENT,
            os.strerror(errno.ENOENT),
            filename
        )

    params = []

    with open(filename, 'r') as tec_file:
        for line in tec_file.readlines():
            if line.strip().startswith("#"):  # это параметр
                param = line.strip()[1:]
                param = param.split("=")
                if len(param) != 2:  # заголовки пропускаем
                    continue
                param = tuple(el.strip() for el in param)
                params.append(param)
    
    params = dict(params)

    # оставляем только нужные параметры
    return {
        key: params[key]
        for key
        in NEEDED_PARAMETERS
    }


def main():
    parser = argparse.ArgumentParser(
        description="""Утилита для работы с файлами TEC.
        Загрузка данных их файла в структуру данных."""
    )

    parser.add_argument(
        '-tec_file',
        type=Path, action='store',
        dest='tec_file', default=Path(''),
        help='Файл с данными TEC (.dat).'
    )

    args = parser.parse_args()

    params = get_params(args.tec_file)
    print(params)

    headers = (
        "tsn", "time", "el", "az",
        "latp", "lonp", "tec",
        "tec_filtered", "validity"
    )

    dataframe = pd.read_csv(
        filepath_or_buffer=args.tec_file,
        delim_whitespace=True,  # разделитель - пробел(ы)
        comment="#",  # пропускаем комменты
        names=headers, # задание заголовков из списка
    )
    print(dataframe)


if __name__ == '__main__':
    main()
