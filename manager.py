tasks = []
def add_task(tasks, task_name):
    task = {"name": task_name, "completada": False}
    tasks.append(task)
    print(f"Tarefa {task_name} foi adicionada com sucesso!")
    return

def show_tasks(tasks):
    print("\nLista de tarefas")
    for index, task in enumerate(tasks, start=1):
       status = "✓" if task["completada"] else " "
       task_name = task["name"]
       print(f"{index}. [{status}] {task_name} ")
    return
    
def update_task_name(tasks, task_index, task_new_name):
    corrected_task_index = int(task_index) - 1
    if corrected_task_index >= 0 and corrected_task_index < len(tasks):
        tasks[corrected_task_index]["name"] = task_new_name
        print(f"Tarefa {task_index} atualizada para {task_new_name}")
    else:
        print("índice de tarefa inválido")
    return

while True:
    print("\n Menu do Gerenciador de Lista de Tarefas:")
    print("1. Adicionar tarefa")
    print("2. Ver tarefa")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair ")

    choice = input("Digite sua escolha: ")

    match choice:
        case "1":
            task_name = (input("Digite o nome da tarefa que deseja adicionar: "))
            add_task(tasks, task_name=task_name)
        case "2":
            show_tasks(tasks=tasks)    
        case "3":
            show_tasks(tasks=tasks)
            task_index = input("Digite o numero da tarefa que deseja atualizar:")
            task_new_name = input("Digite o novo nome da tarefa: ")
            update_task_name(tasks, task_index, task_new_name)
            
#         case "4":
#             # ...
#         case "5":
#             # ...
        case "6":
            break

        
  
            
            
            

# print("Programa finalizado")


