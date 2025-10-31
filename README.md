#Projetos em Python — Sistema de Controle de Estoque e Sistema de Alunos

Este repositório contém dois projetos desenvolvidos em **Python** com o objetivo de praticar a lógica de programação, estruturas de dados e controle de fluxo.  
Ambos os sistemas utilizam menus interativos e permitem o gerenciamento de informações de forma simples e funcional.

---

##Projeto 1 — Mini Sistema de Controle de Estoque (`trabalho_heloisa1.py`)

###Descrição
O **Mini Sistema de Controle de Estoque** permite cadastrar, listar, buscar, atualizar e excluir produtos de uma loja.  
Cada produto possui código, nome, preço, quantidade e categoria.  
O sistema utiliza **listas**, **dicionários**, **tuplas** e **conjuntos (sets)** para garantir o controle adequado das informações, evitando duplicidades de código.

###Funcionalidades
- **Cadastrar Produto:** registra um novo produto com validação de código único.  
- **Listar Produtos:** exibe todos os produtos cadastrados.  
- **Buscar Produto:** permite procurar um produto pelo nome.  
- **Atualizar Produto:** altera informações de um produto já existente.  
- **Excluir Produto:** remove um produto do sistema.  
- **Encerrar Sistema:** finaliza o programa de forma segura.

###Estruturas Utilizadas
- **Listas:** para armazenar todos os produtos.  
- **Dicionários:** para guardar as informações de cada produto.  
- **Sets:** para evitar repetição de códigos.  
- **Tuplas:** para armazenar categorias fixas.  

###Execução
Basta rodar o arquivo no terminal:
```bash
python trabalho_heloisa1.py

#**Sistema de Controle de Alunos e Notas**

##**Descrição**
O **Sistema de Controle de Alunos e Notas** é uma aplicação desenvolvida em **Python** que permite gerenciar o cadastro de alunos, registrar suas notas e calcular automaticamente suas médias.  
Com ele, é possível consultar alunos individualmente e identificar facilmente quem está **aprovado** ou **reprovado**.

O projeto foi criado com o objetivo de exercitar a **lógica de programação**, o **uso de dicionários e tuplas**, além do **controle de fluxo** utilizando **estruturas condicionais e repetitivas**.

---

##**Funcionalidades Principais**
-   **Cadastrar Alunos:** adiciona novos alunos ao sistema.  
-   **Registrar Notas:** armazena três notas para cada aluno.  
-   **Listar Alunos e Médias:** exibe todos os alunos com suas notas e médias calculadas.  
-   **Buscar Aluno:** consulta individual de notas e média.  
-   **Aprovados e Reprovados:** mostra o status final de cada aluno (**média ≥ 7** é **aprovado**).  
-   **Sair:** encerra o programa com segurança.

---

##**Estruturas Utilizadas**
| **Tipo de Estrutura** | **Função no Programa** |
|------------------------|-------------------------|
| **Dicionário (`dict`)** | Armazena os alunos e suas notas. |
| **Tupla (`tuple`)** | Guarda as notas de cada aluno (imutáveis). |
| **Laços (`for` e `while`)** | Controlam a execução contínua e repetição de ações. |
| **Condicionais (`if`, `else`, `elif`)** | Determinam o fluxo do programa com base em decisões. |
| **Tratamento de erros (`try/except`)** | Garante estabilidade caso o usuário digite valores inválidos. |

---

##**Como Executar o Sistema**
1. Certifique-se de ter o **Python 3.10+** instalado.  
2. Baixe o arquivo **`trabalho_heloisa2.py`**.  
3. No terminal, execute o comando:
   ```bash
   python trabalho_heloisa2.py



👩‍💻 Autores

Desenvolvido por Thiago Borges e Kessedy Rodrigues
como parte de práticas de programação em Python.
