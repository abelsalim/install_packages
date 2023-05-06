# Install Package
Install Package é um script que auxilia na instalação em massa de pacotes no
archlinux ao utilizar os gerenciadores de pacotes __pacman__ e __yay__, e
embora com um breve comando possamos realizar essa mesma instalação com o
__pacman__, o mesmo não ocorre com o __yay__, visto que o motivo se dá pelo
fato da instalação parar repentinamente com a execução ao utilizar o
`--noconfirm`e pode ser variante de acordo com os pacotes pré-instalados ou
as configurações locais.

## Utilizando o script

### Help
```
usage: install_package.py [-h] [-g GERENCIADOR] [-l LISTA] [-u]

Script de instalação em massa para lista de pacotes para o pacman e yay

options:
  -h, --help            show this help message and exit

  -g GERENCIADOR, --gerenciador GERENCIADOR
                        Gerenciador de pacotes para utilização

  -l LISTA, --lista LISTA
                        Lista com os pacotes instaláveis

  -u, --upgrade         Realiza upgrade do sistema
```

### Utilização do script
Para utilização básica será necessário repassar o gerenciador de pacotes
desejado (__pacman__ ou __yay__) e também a lista de pacotes contida em um
arquivo de texto.

`python install_packages/install_package.py -g yay -l pacotes_amostra/yay.txt`

Como opção podemos realizar a atualização do sistema antes de instalar os
pacotes, para isso basta repassar o parâmetro `-u` ou `--upgrade`.

```
python install_packages/install_package.py -g yay -l pacotes_amostra/yay.txt -u
```

> Embora seja extremamente recomendado realizar o upgrade de pacotes do sistema
> antes de realizar qualquer instalação, o parâmetro é opcional, visto que
> caso um erro venha ocorre na instalação que tenha realizado previamente um
> upgrade, não será mais necessário ser realizado na segunda instalação.

### Utilização sem script
Para realizar a mesma operação sem o script basta inserir o seguintes
parâmetros para os gerenciadores de pacotes:

#### Com yay
`yay -S --needed - < lista_de_pacotes.txt`

#### Com pacman
`pacman -S --needed - < lista_de_pacotes.txt`

### Porque utilizar?
O pacman funciona perfeitamente com os parâmetros repassados, porém isso nem
sempre ocorre com os pacotes AUR quando utilizamos o yay.

#### Utilizando o yay
É retornado que um arquivo está fechado e a execução é finalizada.

```
➜  install_packages yay -S --needed --noconfirm - < yay.txt
AUR Explicit (1): python-odoorpc-0.8.0-1
Sync Make Dependency (1): python-sphinx-7.0.0-1
:: PKGBUILD up to date, skipping download: python-odoorpc
  1 python-odoorpc                           (Arquivos de Build Existem)
==> Limpar e construir quais pacotes?
==> [N]Nenhum [A]Todos [Ab]Abortar [I]Instalados [No]Não Instalados ou (1 2 3, 1-3, ^4)
==>  -> read /dev/stdin: file already closed
```

> NOTA: Esse tipo de erro ocorre quando realizamos a instalação repassando o
> parâmetro `--noconfirm`, mas aparentemente as configurações ou pacotes
> pré-instalados também influenciam, ou seja, o erro nem sempre vai aparecer
> para todos os usuários.

#### Utilizando o pacman
A instalação é realizada com Êxito.

```
➜  install_packages sudo pacman -S --needed --noconfirm - < pacman.txt
resolvendo dependências...
procurando pacotes conflitantes...

Pacotes (2) libpipeline-1.5.7-1  man-db-2.11.2-1

Tamanho total download:   1,12 MiB
Tamanho total instalado:  2,34 MiB

:: Continuar a instalação? [S/n] 
:: Obtendo pacotes...
 man-db-2.11.2-1-x86_64                                           1110,5 KiB   712 KiB/s 00:02 [########################################################] 100%
 libpipeline-1.5.7-1-x86_64                                         33,6 KiB   163 KiB/s 00:00 [########################################################] 100%
 Total (2/2)                                                      1144,1 KiB   537 KiB/s 00:02 [########################################################] 100%
(2/2) verificando chaves no chaveiro                                                           [########################################################] 100%
(2/2) verificando integridade do pacote                                                        [########################################################] 100%
(2/2) carregando arquivos do pacote                                                            [########################################################] 100%
(2/2) verificando conflitos de arquivos                                                        [########################################################] 100%
(2/2) verificando espaço em disco disponível                                                   [########################################################] 100%
:: Processando alterações do pacote...
(1/2) instalando libpipeline                                                                   [########################################################] 100%
(2/2) instalando man-db                                                                        [########################################################] 100%
Dependências opcionais para man-db
    gzip [instalado]
ldconfig: Arquivo /usr/lib/libKF5Package.so está vazio, não verificado.
ldconfig: Arquivo /usr/lib/libKF5Package.so.5 está vazio, não verificado.
ldconfig: Arquivo /usr/lib/libKF5Package.so.5.105.0 está vazio, não verificado.
ldconfig: Arquivo /usr/lib/libKF5Syndication.so está vazio, não verificado.
ldconfig: Arquivo /usr/lib/libKF5Syndication.so.5 está vazio, não verificado.
ldconfig: Arquivo /usr/lib/libKF5Syndication.so.5.105.0 está vazio, não verificado.
ldconfig: Arquivo /usr/lib/libKF5NewStuff.so está vazio, não verificado.
ldconfig: Arquivo /usr/lib/libKF5NewStuff.so.5 está vazio, não verificado.
ldconfig: Arquivo /usr/lib/libKF5NewStuff.so.5.105.0 está vazio, não verificado.
ldconfig: Arquivo /usr/lib/libKF5NewStuffCore.so está vazio, não verificado.
ldconfig: Arquivo /usr/lib/libKF5NewStuffCore.so.5 está vazio, não verificado.
ldconfig: Arquivo /usr/lib/libKF5NewStuffCore.so.5.105.0 está vazio, não verificado.
ldconfig: Arquivo /usr/lib/libKF5NewStuffWidgets.so está vazio, não verificado.
ldconfig: Arquivo /usr/lib/libKF5NewStuffWidgets.so.5 está vazio, não verificado.
ldconfig: Arquivo /usr/lib/libKF5NewStuffWidgets.so.5.105.0 está vazio, não verificado.
ldconfig: Arquivo /usr/lib/libKF5Style.so está vazio, não verificado.
ldconfig: Arquivo /usr/lib/libKF5Style.so.5 está vazio, não verificado.
ldconfig: Arquivo /usr/lib/libKF5Style.so.5.105.0 está vazio, não verificado.
ldconfig: Arquivo /usr/lib/libHShslua-2.2.1-IBgTFeTUiWk45dztigBgc4-ghc9.0.2.so está vazio, não verificado.
ldconfig: Arquivo /usr/lib/libHShslua-module-doclayout-1.0.4-3WN06KZMlde9YjFuKpsDbj-ghc9.0.2.so está vazio, não verificado.
ldconfig: Arquivo /usr/lib/libHShslua-module-path-1.0.3-KbQeXpWEZnNLbBDWkUrHFO-ghc9.0.2.so está vazio, não verificado.
ldconfig: Arquivo /usr/lib/libHShslua-module-version-1.0.3-G0pQ5HmQtDWCYZQNgeBoKZ-ghc9.0.2.so está vazio, não verificado.
ldconfig: Arquivo /usr/lib/libHSpandoc-lua-marshal-0.2.2-BLn5eyQSdWs20CVzBZnTjo-ghc9.0.2.so está vazio, não verificado.
ldconfig: Arquivo /usr/lib/libHSpandoc-lua-engine-0.1-IAhEyR0KCwVFtiT33CWsYU-ghc9.0.2.so está vazio, não verificado.
ldconfig: /usr/lib/libevdi.so.1 não é um link simbólico

:: Executando hooks pós-transação...
(1/3) Reloading system manager configuration...
(2/3) Creating temporary files...
(3/3) Arming ConditionNeedsUpdate...
```

### Tratamentos no código

- * Verifica se o argumento gerenciador foi informado;
- * Verifica se o argumento lista foi informado;
- * Verifica se a lista tem conteúdo;
- * Verifica permissões de acesso (pacman=root, yay=user);
- * Verifica se o gerenciador é válido (pacman ou yay);
- * Verifica se o argumento upgrade foi repassado;
- * Verifica se o pacote é válido para instalação;
