import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(
        description="""Утилита для работы с файлами TEC.
        Загрузка данных их файла в структуру данных."""
    )

    parser.add_argument(
        '-tec_file',
        type=Path, action='store',
        dest='tec_file', default='',
        help='Файл с данными TEC (.dat).'
    )

    args = parser.parse_args()
    print(args.tec_file)
    
    with open(args.tec_file, 'r') as tec_file:
        for line in tec_file.readlines():
            print(line, end='')


if __name__ == '__main__':
    main()
