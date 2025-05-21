# 1. Entenda o que precisa fazer
# Seu programa precisa mostrar um menu com opções para o usuário.

# Deve permitir adicionar tarefas, ver tarefas, marcar como concluída, remover tarefas e sair.

tarefas= []
concluidas= []

def menu_de_tarefas():
    print("=== GERENCIADOR DE TAREFAS ===")

    print("=== 1. ADICIONAR TAREFA ===")

    print("=== 2. VER TAREFAS ===")

    print("=== 3. MARCAR TAREFAS COMO CONCLUÍDAS ===")

    print("=== 4. REMOVER TAREFAS ===")

    print("=== 5. SAIR ===")

def adicionar_tarefa():
    nome_tarefa= input("Digite a tarefa: ")
    prioridade_tarefa= input("Digite a prioridade da tarefa: ")
    tarefa= {
        'nome': nome_tarefa,
        'prioridade': prioridade_tarefa
    }
    tarefas.append(tarefa)
    print("Tarefa registrada com sucesso!")

def ver_tarefas():
    if not tarefas:
        print("Nenhuma tarefa registrada.")
    else:
        print("=== LISTA DE TAREFAS REGISTRADAS == ")
        for i, t in enumerate(tarefas, start=1):
            print(f"{i}. Nome: {t['nome']}, Prioridade: {t['prioridade']} ")

def marcar_concluido():
    if not tarefas:
        print("Nenhuma tarefa concluída.")
        return
    
    print("=== TAREFAS PENDENTES ===")
    for i, t in enumerate(tarefas, start=1):
        print(f"{i}. Nome: {t['nome']}, Prioridade: {t['prioridade']}")

    try:
        indice= int(input("Digite o número da tarefa que deseja marcar como concluída: "))
        if 1 <= indice <= len(tarefas):
            tarefa_concluida = tarefas.pop(indice - 1)
            concluidas.append(tarefa_concluida)
            print("Tarefa concluída com sucesso!")
        else:
            print("Digite um número válido!" )
    except ValueError:
        print("Digite um número válido!" )

def remover_tarefa():
    if not tarefas:
        print("Nenhuma tarefa registrada para remover.")
        return
    
    print("=== TAREFAS DISPONÍVEIS PARA REMOVER ===")
    for i, t in enumerate(tarefas, start=1):
        print(f"{i}. Nome: {t['nome']}, Prioridade: {t['prioridade']}")

    try:
        indice= int(input("Digite o número da tarefa que deseja remover: "))
        if 1 <= indice <= len(tarefas):
            tarefa_removida = tarefas.pop(indice - 1)
            print(f" '{tarefa_removida['nome']}' removida com sucesso!")
        else:
            print("Digite um número válido!" )
    except ValueError:
        print("Digite um número válido!" )

while True:
    menu_de_tarefas()
    escolha= input("Digite um número: ")
    if escolha == "1":
        adicionar_tarefa()
    elif escolha == "2":
        ver_tarefas()
    elif escolha == "3":
        marcar_concluido()
    elif escolha == "4":
        remover_tarefa()
    elif escolha == "5":
        print("Saindo...")
        break   
