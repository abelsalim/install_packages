# -*- coding: utf-8 -*-

from utils import argumentos_altera_status_venda
from class_instala_yay_pacman import InstallPackages


def main(objeto, faz_upgrade):
    '''
    Função que realiza instalação de lista de pacotes com pacman ou yay
    '''

    objeto.tem_gerenciador

    objeto.tem_lista

    objeto.tratamento_de_permissoes()

    objeto.atualiza_repositorios

    if faz_upgrade:
        objeto.upgrade_de_pacotes

    objeto.instala_pacotes


if __name__ == '__main__':
    args = argumentos_altera_status_venda()
    install = InstallPackages(lista=args.lista, gerenciador=args.gerenciador)

    main(install, args.upgrade)
