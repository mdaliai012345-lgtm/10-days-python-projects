
task = []
while True:
    print('''
    ====== TO-DO LIST ======
    1. Add Task
    2. View Task
    3. Delete Task
    4. Exit
    ''')
    user = int(input("Enter Your Choice : "))
    if user == 1:
        add = input("enter new tast : ")
        task.append(add)
        print(task)
    elif user == 2:
        if len(task) == 0:
               print("No task available")
        else:
            print("\n your task ")
            for  i in range(len(task)):
                print(f"{i + 1}. {task[i]}")
    elif user == 3:
        if len(task) == 0:
            print("No task to delet")
        else: 
            print(f"\n your task ")
            for i in range((len(task))):
                print(f"{i + 1}, {task[i]}")
        delete = int(input("Enter the task which u want to delete :"))
        if 1 <= delete <= len(task):
            task.pop(delete - 1)
            print("task deleted")
        else:
            print("Invalid task")
        print(task)
    elif user == 4:
        print("Done")
        break

else:
    print("invalid")