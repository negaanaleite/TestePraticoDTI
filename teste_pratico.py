import datetime
tarefas = []

while True: 
    #Exibir menu
    print("----- Menu ----")
    print("1. Adicionar Lembretes")
    print("2. Visualizar todos os lembretes")
    print("3. Visualizar apenas os próximos lembretes")
    print("4. Sair")

    #Opção do Usuário

    opcao = input("Escolha a opção desejada")

    #Adicionar Tarefas

    if opcao == '1':
        nome_tarefa = input("Nome do lembrete? ")
        data_tarefa = input("Insira a data do evento neste formato dd/mm/aaaa: ")

        data = datetime.datetime(data_tarefa, "%d/%m/%Y")

        # Criar um dicionário com o nome e a data do lembrete
        item = {
            'tarefa': nome_tarefa, 'data': data_tarefa
        }
        # Adicionar o dicionário à lista de lembretes
        tarefas.append(item)

        print("Lembrete Adicionado!")

    #Para visualizar todos os lembretes 
    elif opcao == '2':
        print("Lista de lembretes")
        
        for item in tarefas:
            print(item["nome_tarefa"], "-", item["data_tarefa"])

    #Visualizar apenas os proximos lembretes
    elif opcao == '3':
        agora = datetime.datetime.now()
        tarefas_recentes =[]
        for item in tarefas:
            if item [data_tarefa]> agora:
                tarefas_recentes.append(item)
        print("Listas dos proximos Lembretes")
        for item in tarefas_recentes:
             print(item["nome_tarefa"], "-", item["data_tarefa"])

    #Sair do Programa
    elif opcao =='4':
        print(" Obrigada por usar nosso programa!")
        break 
    #Opção invalida 
    else:
        print(" Opção invalida. Digite um numero de 1 a 4")
        





