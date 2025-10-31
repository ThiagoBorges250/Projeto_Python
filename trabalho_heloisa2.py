# Sistema de Controle de Alunos e Notas (versão simplificada)

alunos = {}  # Dicionário principal: guarda nome do aluno como chave e uma tupla com as notas como valor

while True:  # Loop infinito que mantém o sistema rodando até o usuário escolher sair
    print("""  # Exibe o menu principal de opções na tela
===== MENU =====
1 - Cadastrar aluno
2 - Registrar notas
3 - Listar alunos e médias
4 - Buscar aluno
5 - Aprovados e Reprovados
0 - Sair
================
""")

    opcao = input("Escolha uma opção: ")  # Recebe a opção do usuário como string

    # Sair do sistema
    if opcao == "0":  # Se o usuário digitar 0, o programa será encerrado
        print(">>> Encerrando o sistema... Até logo! <<<")
        break  # Sai do laço while e finaliza o programa

    # Cadastrar aluno
    elif opcao == "1":  # Se o usuário escolher a opção 1
        n_alunos = int(input("Digite a quantidade de alunos que serão cadastrados: "))  # Converte o número digitado em inteiro
        for i in range(0, n_alunos):  # Repete o cadastro de acordo com a quantidade informada
            nome = input("Digite o nome do aluno: ").capitalize()  # Lê o nome e deixa a primeira letra maiúscula
            if nome in alunos:  # Verifica se o nome já está no dicionário
                print("Aluno já cadastrado!")  # Se estiver, exibe mensagem de aviso
            else:
                alunos[nome] = ()  # Cria o aluno no dicionário com uma tupla vazia de notas
                print(f"Aluno {nome} cadastrado com sucesso!")  # Confirma o cadastro

    # Registrar notas
    elif opcao == "2":  # Se o usuário escolher a opção 2
        nome = input("Digite o nome do aluno: ").capitalize()  # Solicita o nome do aluno
        if nome not in alunos:  # Verifica se o aluno está cadastrado
            print("Aluno não encontrado! Cadastre-o primeiro.")  # Caso não esteja, exibe aviso
        else:
            notas = []  # Cria uma lista temporária para armazenar as notas
            for i in range(3):  # Solicita 3 notas
                nota = float(input(f"Digite a {i+1}ª nota de {nome}: "))  # Converte o valor digitado para float
                notas.append(nota)  # Adiciona a nota na lista
            alunos[nome] = tuple(notas)  # Converte a lista em tupla e salva no dicionário
            print(f"Notas registradas para {nome}!")  # Confirma o registro das notas

    # Listar alunos e médias
    elif opcao == "3":  # Se o usuário escolher a opção 3
        if not alunos:  # Verifica se o dicionário está vazio
            print("Nenhum aluno cadastrado.")  # Caso não haja alunos, mostra mensagem
        else:
            print(">>> Lista de Alunos e Médias <<<")  # Cabeçalho da listagem
            for nome, notas in alunos.items():  # Percorre cada aluno e suas notas
                if notas:  # Verifica se o aluno tem notas registradas
                    media = sum(notas) / len(notas)  # Calcula a média das notas
                    print(f"{nome}: Notas {notas} | Média = {media:.2f}")  # Exibe nome, notas e média formatada
                else:
                    print(f"{nome}: sem notas registradas.")  # Caso não tenha notas
            print()  # Linha em branco para separar visualmente a saída

    # Buscar aluno específico
    elif opcao == "4":  # Se o usuário escolher a opção 4
        nome = input("Digite o nome do aluno: ").capitalize()  # Solicita o nome e padroniza a capitalização
        if nome in alunos:  # Verifica se o aluno está no dicionário
            notas = alunos[nome]  # Obtém as notas do aluno
            if notas:  # Se o aluno tiver notas registradas
                media = sum(notas) / len(notas)  # Calcula a média
                print(f"{nome} Notas: {notas} | Média: {media:.2f}")  # Exibe as informações completas
            else:
                print(f"{nome} está cadastrado, mas sem notas ainda.")  # Caso o aluno não tenha notas
        else:
            print("Aluno não encontrado.")  # Caso o nome não exista no dicionário

    # Mostrar aprovados e reprovados
    elif opcao == "5":  # Se o usuário escolher a opção 5
        if not alunos:  # Verifica se há alunos cadastrados
            print("Nenhum aluno cadastrado.")  # Caso não haja, mostra aviso
        else:
            print(">>>> Aprovados e Reprovados <<<<")  # Cabeçalho da seção
            for nome, notas in alunos.items():  # Percorre todos os alunos e suas notas
                if notas:  # Se o aluno tiver notas
                    media = sum(notas) / len(notas)  # Calcula a média
                    status = "Aprovado" if media >= 7 else "Reprovado"  # Define o status conforme a média
                    print(f"{nome}: Média {media:.2f} -> {status}")  # Exibe o nome, média e status final
                else:
                    print(f"{nome}: sem notas registradas.")  # Caso o aluno ainda não tenha notas
            print()  # Linha em branco para espaçamento entre blocos


