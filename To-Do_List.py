def Main():
    tasks = []

    while True:
        #displays the options to choose from
        print('\nOptions')
        print('1: display tasks')
        print('2:add task')
        print('3:remove task')
        print('4:quit')
        #gets the choice of the user 
        choice = input('Enter your choice: ')
    
        #use function bassed on the choice choosen
        if choice == '1':
            for index, task in enumerate(tasks):
                    print(f"{index + 1}. {task['Task']}")

        elif choice == "2":
            n_task= int(input("How many tasks would you like to add : "))

            for i in range(n_task):
                task = input("Enter the task: ")
                tasks.append({"Task":task, "Done":False})
                print("Task Added")

        elif choice == "3":
            if not tasks:
                print("No tasks to remove")
            else:
                print("\nCurrent tasks")
                for index, task in enumerate(tasks):
                    print(f"{index + 1}. {task['Task']}")
                try:
                    task_num = int(input("Enter task number to remove: "))
                    if 1 <= task_num <= len(tasks):
                        removed_task = tasks.pop(task_num - 1)
                        print(f"Removed: {removed_task['Task']}")
                    else:
                        print("Invailed task number")
                except ValueError:
                    print("Please enter a valid number.")


        elif choice == "4":
            print("you have left the app")
            break

        else:
            print("invalid choice. please try again")

Main()