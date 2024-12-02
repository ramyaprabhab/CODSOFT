def task():
    tasks=[]
    print("Your TO_DO list :)")

    total_tasks=int(input("Enter the number of tasks you wan to add: "))

    for i in range (1, total_tasks+1):
        task_name=input(f"enter task number {i}: ")
        tasks.append(task_name)
    
    print(f"your todays tasks are\n{tasks}")

    while True:
        operation=int(input("What do you want to do\n1-Add\n2-Update\n3-Delete\n4-View\n5-stop\n: "))

        if (operation==1):
            new=input("enter a new task ")
            tasks.append(new)
            print(f"{new} added")

        elif operation==2:
            updated_val= input("enter the task you want to update with ")
            if updated_val in tasks:
                up_new=input("enter the task: ")
                a= tasks.index(updated_val)
                tasks[a] =up_new
                print(f"{up_new}added")                
        elif operation==3:
            del_val= input("enter the task that you want to delete ")    
            if del_val in tasks:
                a=tasks.index(del_val)
                del tasks[a]
                print(f" {del_val} deleted")

        elif operation==4:
            print(tasks)

        elif operation==5:
            print("closing the program")
            break
        else:
            print("invalid input")

task()