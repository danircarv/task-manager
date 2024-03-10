tasks = []
def add_task(tasks, task_name):
    task = {"nome": task_name, "completada": False}
    tasks.append(task)
    print(f"Tarefa {task_name} foi adicionada com sucesso!")
    return

def show_tasks(tasks):
    print("\nLista de tarefas")
    print(tasks)

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
            task_name = input("Digite o nome da tarefa que deseja adicionar: ")
            add_task(tasks, task_name=task_name)
        case "2":
            show_tasks(tasks=tasks)
            
            
#         case "3":
#             # ...
#         case "4":
#             # ...
#         case "5":
#             # ...
#         case "6":
#             # ...

        
  
            
            
            

# print("Programa finalizado")


