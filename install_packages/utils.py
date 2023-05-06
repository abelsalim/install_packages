# -*- coding: utf-8 -*-

import argparse
import logging

from colorlog import ColoredFormatter
from constantes import (
    DESCRICAO,
    ARGS_GERRENCIADOR,
    ARGS_LISTA,
    LOGGER_COLOR
)


def argumentos_altera_status_venda():
    parser = argparse.ArgumentParser(description=DESCRICAO)
    parser.add_argument('-g', '--gerenciador', help=ARGS_GERRENCIADOR)
    parser.add_argument('-l', '--lista', help=ARGS_LISTA)
    parser.add_argument(
        '-u', '--upgrade', action='store_true', 
        help='Realiza upgrade do sistema'
    )

    return parser.parse_args()


def logger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    formatter = ColoredFormatter(
        '%(asctime)s | %(log_color)s %(levelname)-8s%(reset)s | '
        '%(blue)s%(message)s',
        reset=True,
        log_colors=LOGGER_COLOR,
        style='%'
    )

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    return logger


if __name__ == '__main__':
    pass
