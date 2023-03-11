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

        data = datetime.datetime.strptime(data_tarefa, "%d/%m/%Y")

        # Criar um dicionário com o nome e a data do lembrete
        item = {
            'tarefa': nome_tarefa, 'data': data
        }
        # Adicionar o dicionário à lista de lembretes
        tarefas.append(item)

        print("Lembrete Adicionado!")

    #Para visualizar todos os lembretes 
    elif opcao == '2':
        print("Lista de lembretes")
        
        for item in tarefas:
            print(item["tarefa"], "-", item["data"])

    #Visualizar apenas os proximos lembretes
    elif opcao == '3':
        agora = datetime.datetime.now()
        data_daqui_dois_dias = agora + datetime.timedelta(days=2)
        tarefas_recentes = []
        for item in tarefas:
            if item["data"] > agora and item["data"] <  data_daqui_dois_dias:
                tarefas_recentes.append(item)
        print("Listas dos proximos Lembretes")
        for item in tarefas_recentes:
             print(item["tarefa"], "-", item["data"])

    #Sair do Programa
    elif opcao =='4':
        print(" Obrigada por usar nosso programa!")
        break 
    #Opção invalida 
    else:
        print(" Opção invalida. Digite um numero de 1 a 4")
        





