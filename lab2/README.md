# Laboratório 2
## Sistemas Distribuídos - UFRJ (ICP-367)

### Aplicação cliente/servidor básica

> O objetivo deste Laboratorio é desenvolver uma aplicação distribuída para aplicar os conceitos estudados sobre arquitetura de software e arquitetura de sistema; servidores multiplexados e concorrentes; e seguir praticando com a programação usando sockets.

## Atividade 1

1. O estilo arquitetural que escolhi para desenvolver o código foi a de cliente/servidor

2. Desenvolvi tres (3) componentes `cli.py, srv.py` e `dicionario.py`.
    - `cli.py`
        + Nessa aplicação temos toda a interface de comunicação com o usuario cliente, que, por meio de comandos, consegue fazer as alterações e consultas no servidor.
        + Nessa aplicação temos tres comandos, que o usuario seleciona. `1`, para adicionar um par chave:valor, `2`, para consultar uma chave e `fim` para finalizar a conexão.
        + Para enviar as mensagens ao servidor, o cliente encapsula os dados de acordo com o tipo de ação que o usuário escolheu.
    - `srv.py`
        + Essa aplicação realiza todos os processamentos para as mensagens enviadas pelo cliente e disponibiliza uma interface para um administrador fazer a remoção de uma chave do dicionario. 
        + Essa camanda também é responsavel pelo carregamento dos dados do dicionario de um arquivo no servidor.
    - `dicionario.py`
        + Nesse aquivos ficam os métodos para a permanencia dos dados no servidor.

## Atividade 2

1. O lado do cliente ficará apenas o `cli.py`.

2. Do lado do servidor ficarão os arquivos de `srv.py` e `dicionario.py`. E eventualmente o arquivo `.json` que sera utilizado para a permanencia do dicionario.

3. As mensagens enviadas pelo cliente serão no formato `CDM[]`, onde CMD poderá ser ADD, para adicionar um par chave valor no formato `ADD[chave:valor]` ou `CON[chave]` para uma consulta. Esse encapsulamentos é feito de forma automatica pelo código e o usuario digitará apenas a chave e o valor que ele deseja adicionar ou consultar.
    - O usuário deverá editar as constantes `HOST` e `PORTA` para o host e porta definido no servidor para conseguir se conectar. Caso o cliente se conecte com sucesso, o programa irá imprimir na tela os comandos disponiveis para uso, e aguardará um input. Caso o cliente não se conecte, ele irá avisar o usuario e terminar o programa.
    - O administrador do servidor, poderá utilizar o comando `REM[chave]` na interface do servidor para remover uma chave do dicionario.