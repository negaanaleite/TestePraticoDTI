from teste_pratico import adicionar_lembretes, exibir_todos_lembretes, exibir_proximos_lembretes, excluir_lembretes

while True: 
    
    print("\n------------------")
    print("       Menu")
    print("------------------")
    print("1 - Adicionar lembrete")
    print("2 - Visualizar todos os lembretes")
    print("3 - Visualizar próximos lembretes")
    print("4 - Excluir lembrete")
    print("0 - Sair")

    opcao = input("\nDigite a opção desejada: ")

    if opcao == "1":
        adicionar_lembretes()
    elif opcao == "2":
        exibir_todos_lembretes()
    elif opcao == "3":
       exibir_proximos_lembretes()
    elif opcao == "4":
        excluir_lembretes()
    elif opcao == '0':
        print("Obrigada por usar nosso programa!")
        break 
    