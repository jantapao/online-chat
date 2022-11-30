# Online Chat

Repositório referente ao Terceiro Trabalho da disciplina de Redes de Computadores do curso de Engenharia de Computação da Universidade Federal de Mato Grosso do Sul.

## Alunos

[Keven Augusto Queiroz Bezerra](https://github.com/kevenaugusto)
[Pedro Francisco de Mello Sousa](https://github.com/jantapao)

## Requisitos

[Python 3.10.6](https://www.python.org/downloads/release/python-3106/)

## Tabela de Conteúdo

 - [Bibliotecas](#bibliotecas)
 - [Execução](#execu%C3%A7%C3%A3o)
 - [Exemplos](#exemplos)

## Bibliotecas

Para a correta execução da aplicação, é necessário a instalação de algumas bibliotecas:

 - [Signal](https://docs.python.org/3/library/signal.html)
 - [Socket](https://docs.python.org/3/library/socket.html)
 - [Readchar](https://pypi.org/project/readchar/)

## Execução

Para executar no Windows:

```python main.py [tipo] [host] [porta]```

Para executar no Unix:

```python3 main.py [tipo] [host] [porta]```

**Tipos:**

 1. Servidor
 2. Client (sender)
 3. Client (receiver)

**Host:** o IP onde a aplicação se conectará.
**Porta:** a porta para conexão da aplicação.

## Exemplos

```python3 main.py 1 192.168.100.186 5005```

```python main.py 3 192.168.100.186 5005```
