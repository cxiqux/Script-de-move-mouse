# Move Mouse

Aplicação simples em **Python** com interface gráfica que automatiza
pequenos movimentos do mouse e realiza cliques periódicos para evitar o
estado de inatividade do computador.

A cada **10 segundos**, o programa move levemente o cursor e executa um
clique, mantendo a sessão ativa.

------------------------------------------------------------------------

## Funcionalidades

-   Exibe um cronômetro com o tempo restante
-   Move o mouse automaticamente e realiza clique
-   Interface gráfica com CustomTkinter
-   Botão Iniciar Automação
-   Botão Parar Automação
-   Execução em segundo plano usando thread

------------------------------------------------------------------------

## Requisitos

-   Python 3.9 ou superior
-   Bibliotecas:

``` bash
pyautogui
customtkinter
```

No macOS ou Linux pode ser necessário conceder permissões de
acessibilidade.

------------------------------------------------------------------------

# Como Executar (Modo Desenvolvimento)

## 1. Criar ambiente virtual

### PowerShell

``` bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### CMD

``` bash
python -m venv .venv
.\.venv\Scripts\activate.bat
```

------------------------------------------------------------------------

## 2. Instalar dependências

``` bash
pip install pyautogui customtkinter
```

------------------------------------------------------------------------

## 3. Executar o programa

``` bash
python movemouse.py
```

------------------------------------------------------------------------

# Gerar Executável (.exe)

O projeto possui arquivo `.spec`, então utilize o PyInstaller.

## 1. Instalar PyInstaller

``` bash
pip install pyinstaller
```

## 2. Gerar executável

``` bash
pyinstaller movemouse.spec
```

O executável será criado dentro da pasta:

    dist/

------------------------------------------------------------------------

## Estrutura do Projeto

    move-mouse/
    │
    ├── movemouse.py
    ├── movemouse.spec
    ├── build/
    ├── dist/
    └── README.md

------------------------------------------------------------------------

## Como Funciona

1.  O cronômetro inicia em 10 segundos.
2.  Ao chegar a zero:
    -   move o mouse levemente
    -   retorna à posição original
    -   realiza um clique
3.  O ciclo reinicia automaticamente.
4.  Ao clicar em "Parar Automação", o processo é interrompido.

------------------------------------------------------------------------

## Avisos

-   O programa controla o mouse automaticamente.
-   Evite deixá-lo sobre botões sensíveis.
-   Não utilize durante jogos ou tarefas que dependam do cursor.

------------------------------------------------------------------------

## Sugestão de .gitignore

    .venv/
    __pycache__/
    *.pyc
    build/
    dist/
    *.toc
    *.pyz
    *.zip

------------------------------------------------------------------------

## Autor

Caique Feitosa
