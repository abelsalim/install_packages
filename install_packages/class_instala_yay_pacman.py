# -*- coding: utf-8 -*-

import os
import sys
import pwd

from subprocess import run, PIPE
from utils import logger
from constantes import (
    ATUALIZA,
    INSTALA,
    UPGRADE,
    LISTA_NAO_INFORMADA,
    GERENCIADOR_NAO_INFORMADO,
    GERENCIADOR_NAO_EXECUTADO,
    GERENCIADOR_DESCONHECIDO,
    LISTA_VAZIA,
    ERRO_AO_LER_ARQUIVO,
    PACOTE_NAO_ENCONTRADO,
    ATUALIZANDO_REPOSITORIOS,
    ATUALIZANDO_PACOTES,
    INSTALANDO_PACOTES,
    INSTALACAO_CONCLUIDA,
    STDERR
)


class InstallPackages:

    def __init__(self, lista=None, gerenciador=None):
        self.lista = lista
        self.lista_de_pacotes = []
        self.gerenciador = gerenciador
        self.usuario = self.get_user()
        self.log = logger()

    def get_user(self):
        username = pwd.getpwuid(os.getuid())
        return username.pw_name

    def ler_arquivo(self, arquivo):
        try:
            with open(arquivo, 'r') as file:
                self.lista_de_pacotes = file.read().split('\n')

        except FileNotFoundError:
            self.log.error(ERRO_AO_LER_ARQUIVO)
            sys.exit(3)

    @property
    def tem_gerenciador(self):
        if not self.gerenciador:
            self.log.error(GERENCIADOR_NAO_INFORMADO)
            sys.exit(3)

    @property
    def tem_lista(self):
        if not self.lista:
            self.log.error(LISTA_NAO_INFORMADA)
            sys.exit(3)

        else:
            self.ler_arquivo(self.lista)

            if not self.lista_de_pacotes:
                self.log.error(LISTA_VAZIA)
                sys.exit(3)

    def tratamento_de_permissoes(self):
        if self.gerenciador == 'pacman' and self.usuario == 'root':
            return True

        elif self.gerenciador == 'yay' and self.usuario != 'root':
            return True

        elif self.gerenciador == 'pacman' and self.usuario != 'root':
            self.log.error(GERENCIADOR_NAO_EXECUTADO.format('pacman', 'root'))

        elif self.gerenciador == 'yay' and self.usuario == 'root':
            self.log.error(GERENCIADOR_NAO_EXECUTADO.format('yay', 'root'))

        else:
            self.log.error(GERENCIADOR_DESCONHECIDO.format(self.gerenciador))

        sys.exit(3)

    @property
    def atualiza_repositorios(self):
        self.log.info(ATUALIZANDO_REPOSITORIOS)
        run(ATUALIZA.format(self.gerenciador), shell=True)

    @property
    def upgrade_de_pacotes(self):
        self.log.info(ATUALIZANDO_PACOTES)
        run(UPGRADE.format(self.gerenciador), shell=True)

    def instale(self, pacote):
        instalou = run(
            INSTALA.format(self.gerenciador, pacote),
            shell=True,
            stderr=PIPE,
            universal_newlines=True
        )

        if instalou.returncode and self.gerenciador == 'pacman':
            self.log.error(PACOTE_NAO_ENCONTRADO.format(pacote))
            sys.exit(3)

        elif STDERR in instalou.stderr and self.gerenciador == 'yay':
            self.log.error(PACOTE_NAO_ENCONTRADO.format(pacote))
            sys.exit(3)

    @property
    def instala_pacotes(self):
        if self.lista_de_pacotes:
            self.log.info(INSTALANDO_PACOTES)
            for pacote in self.lista_de_pacotes:
                if pacote:
                    self.instale(pacote)
            self.log.info(INSTALACAO_CONCLUIDA)


if __name__ == '__main__':
    pass
