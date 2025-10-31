# Mini Sistema de Controle de Estoque

# Lista que armazenará todos os produtos cadastrados
produtos = []  

# Conjunto (set) usado para armazenar códigos já cadastrados
# Isso evita que dois produtos tenham o mesmo código
codigos_cadastrados = set()  

# Tupla com as categorias pré-definidas de produtos
categorias = ("Alimentos", "Limpeza", "Bebidas")  


def cadastrar_produto():
    """
    Função responsável por cadastrar um novo produto no sistema.
    Solicita os dados do produto, verifica duplicidades e valida as entradas.
    """
    print("=== Cadastro de Produto ===")
    try:
        # Solicita o código do produto (deve ser numérico)
        codigo = int(input("Digite o código do produto: "))
        # Verifica se o código já foi cadastrado
        if codigo in codigos_cadastrados:
            print("Código já cadastrado! Tente outro.")
            return
    except ValueError:
        # Caso o usuário digite algo que não seja número
        print("Código inválido! Digite apenas números.")
        return
    
    # Solicita o nome do produto e padroniza com a primeira letra maiúscula
    nome = input("Digite o nome do produto: ").strip().capitalize()

    try:
        # Solicita o preço e a quantidade do produto
        preco = float(input("Digite o preço do produto: R$ "))
        quantidade = int(input("Digite a quantidade em estoque: "))
    except ValueError:
        # Caso o usuário digite valores não numéricos
        print("Valor inválido! Use números válidos para preço e quantidade.")
        return
    
    # Exibe as categorias disponíveis para o usuário escolher
    print("\nCategorias disponíveis:")
    for i, cat in enumerate(categorias):
        print(f"{i + 1} - {cat}")
    try:
        # Usuário escolhe a categoria pelo número
        opc = int(input("Escolha a categoria (1-3): "))
        categoria = categorias[opc - 1]
    except (ValueError, IndexError):
        # Caso a opção seja inválida, a categoria será "Outros"
        print("Categoria inválida! O produto será cadastrado como 'Outros'.")
        categoria = "Outros"

    # Criação do dicionário com as informações do produto
    produto = {
        "codigo": codigo,
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade,
        "categoria": categoria
    }

    # Adiciona o produto à lista e o código ao conjunto de controle
    produtos.append(produto)
    codigos_cadastrados.add(codigo)
    print(f"Produto '{nome}' cadastrado com sucesso!\n")


def listar_produtos():
    """
    Exibe todos os produtos cadastrados no sistema.
    Caso não existam produtos, mostra uma mensagem de aviso.
    """
    print("\n=== Lista de Produtos ===")
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    # Percorre e exibe cada produto da lista
    for p in produtos:
        print(f"Código: {p['codigo']} | Nome: {p['nome']} | Preço: R${p['preco']:.2f} | "
              f"Qtd: {p['quantidade']} | Categoria: {p['categoria']}")
    print()


def buscar_produto():
    """
    Busca um produto pelo nome e exibe suas informações.
    Se o produto não for encontrado, exibe uma mensagem.
    """
    print("=== Buscar Produto ===")
    nome = input("Digite o nome do produto: ").strip().capitalize()
    encontrado = False

    # Procura o produto na lista
    for p in produtos:
        if p["nome"] == nome:
            print(f"Produto encontrado:")
            print(f"Código: {p['codigo']} | Preço: R${p['preco']:.2f} | "
                  f"Qtd: {p['quantidade']} | Categoria: {p['categoria']}")
            encontrado = True
            break

    if not encontrado:
        print("Produto não encontrado.")


def atualizar_produto():
    """
    Atualiza os dados de um produto existente, identificado pelo código.
    O usuário pode alterar nome, preço e quantidade.
    """
    print("=== Atualizar Produto ===")
    try:
        codigo = int(input("Digite o código do produto que deseja atualizar: "))
    except ValueError:
        print("Código inválido!")
        return

    # Procura o produto correspondente ao código
    for p in produtos:
        if p["codigo"] == codigo:
            print(f"Produto atual: {p}")

            # Permite alterar o nome (ou manter o atual com enter)
            p["nome"] = input("Novo nome (enter para manter o atual): ") or p["nome"]

            try:
                # Permite alterar preço e quantidade
                novo_preco = input("Novo preço (enter para manter): ")
                if novo_preco:
                    p["preco"] = float(novo_preco)

                nova_qtd = input("Nova quantidade (enter para manter): ")
                if nova_qtd:
                    p["quantidade"] = int(nova_qtd)
            except ValueError:
                # Caso o usuário digite valores inválidos
                print("Valor inválido, mantendo dados antigos.")

            print("Produto atualizado com sucesso!")
            return

    # Caso o código não corresponda a nenhum produto
    print("Produto não encontrado.")


def excluir_produto():
    """
    Exclui um produto do sistema com base em seu código.
    Remove tanto da lista quanto do conjunto de códigos.
    """
    print("=== Excluir Produto ===")
    try:
        codigo = int(input("Digite o código do produto que deseja excluir: "))
    except ValueError:
        print("Código inválido!")
        return

    # Busca o produto pelo código
    for p in produtos:
        if p["codigo"] == codigo:
            produtos.remove(p)
            codigos_cadastrados.remove(codigo)
            print(f"Produto '{p['nome']}' removido com sucesso!")
            return

    print("Produto não encontrado.")


# === MENU PRINCIPAL ===
# Loop principal do programa que exibe as opções e chama as funções correspondentes
while True:
    print("=== MENU PRINCIPAL ===")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto")
    print("4 - Atualizar produto")
    print("5 - Excluir produto")
    print("0 - Fechar sistema")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Opção inválida! Digite um número.")
        continue

    # Chama a função conforme a opção escolhida
    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        buscar_produto()
    elif opcao == 4:
        atualizar_produto()
    elif opcao == 5:
        excluir_produto()
    elif opcao == 0:
        print("Saindo do sistema... até logo!")
        break
    else:
        print("Opção inexistente! Tente novamente.")