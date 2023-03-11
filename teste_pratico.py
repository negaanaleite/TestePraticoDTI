from datetime import datetime, timedelta

lembretes = []

def adicionar_lembretes():
    nome = input("Digite o nome do lembrete: ")
    data_lem = input("Digite a data do lembrete (formarto: dd/mm/aaaa): ")
    data = datetime.strptime(data_lem, "%d/%m/%Y")
    if data.date() < datetime.today().date():
        print("A data do lembrete deve ser a partir de hoje")
    else:
        lembrete = (nome, data)
        lembretes.append(lembrete)
        print("Lembrete adicionado com sucesso")

def exibir_todos_lembretes():
    print("-- Todos os Lembretes --")
    for lembrete in lembretes:
        print(f"{lembrete[1].strftime('%d/%m/%Y')} - {lembrete[0]}")

def exibir_proximos_lembretes():
    print("Proximos Lembretes")
    hoje = datetime.today().date()
    data_daqui_dois_dias = hoje + timedelta(days=2)
    for lembrete in lembretes:
        if lembrete[1].date() >= hoje and lembrete[1].date() <= data_daqui_dois_dias: 
            print(f"{lembrete[1].strftime('%d/%m/%Y')} - {lembrete[0]}")

def excluir_lembretes():
    opcao = input("\nDeseja excluir um lembrete específico (1) ou todos os lembretes (2)? ")

    if opcao == "1":
        for i, lembrete in enumerate(lembretes):
            print(f"{i+1}. {lembrete[1].strftime('%d/%m/%Y')} - {lembrete[0]}")
        indice = int(input("Digite o índice do lembrete que deseja excluir: ")) - 1
        if indice < 0 or indice >= len(lembretes):
            print("Índice inválido.")
        else:
            del lembretes[indice]
            print("Lembrete excluído com sucesso!")
    elif opcao == "2":
        lembretes.clear()
        print("Todos os lembretes foram excluídos.")
    else:
        print("Opção inválida.")


    