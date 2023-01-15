import uuid
import datetime

task_list = []


class Task:

    def __init__(self, task_name) -> None:
        self.id = uuid.uuid1()
        self.task_name = task_name
        self.created_time = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        self.updated_time = 'NA'
        self.completed_time = 'NA'
        self.task_done = False

    def update_task(self, update_task_name):
        self.task_name = update_task_name
        self.updated_time = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")

    def complete_task(self):
        self.task_done = True
        self.completed_time = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")


if __name__ == "__main__":
    while True:
        print("1. ADD NEW TASK")
        print("2. SHOW ALL TASK")
        print("3. SHOW INCOMPLETE TASK")
        print("4. SHOW COMPLETED TASK")
        print("5. UPDATE TASK")
        print("6. MARK A TASK COMPLETED")
        print("7. EXIT")
        option = input("ENTER OPTION: ")
        if option == '1':
            task_name = input("ENTER NEW TASK: ")
            task_list.append(Task(task_name))
            print()
            print('-'*55)
            print("\nTASK CREATED SUCCESSFULLY!\n")
            print('-'*55)
            print()
        elif option == '2':
            if task_list:
                print()
                print('-'*55)
                for task in task_list:
                    print()
                    print(f"ID - {task.id}")
                    print(f"TASK - {task.task_name}")
                    print(f"CREATED TIME - {task.created_time}")
                    print(f"UPDATE TIME - {task.updated_time}")
                    print(f"COMPLETED - {task.task_done}")
                    print(f"COMPLETED TIME - {task.completed_time}")
                print()
                print('-'*55)
                print()
            else:
                print()
                print('-'*55)
                print("\nTHERE IS NO TASK!\n")
                print('-'*55)
                print()
        elif option == '3':
            flag = True
            print()
            print('-'*55)
            for task in task_list:
                if (task.task_done == False):
                    flag = False
                    print()
                    print(f"ID - {task.id}")
                    print(f"TASK - {task.task_name}")
                    print(f"CREATED TIME - {task.created_time}")
                    print(f"UPDATE TIME - {task.updated_time}")
                    print(f"COMPLETED - {task.task_done}")
                    print(f"COMPLETED TIME - {task.completed_time}")
            if flag:
                print("\nTHERE IS NO INCOMPLETE TASK!")

            print()
            print('-'*55)
            print()
        elif option == '4':
            flag = True
            print()
            print('-'*55)
            for task in task_list:
                if (task.task_done == True):
                    flag = False
                    print()
                    print(f"ID - {task.id}")
                    print(f"TASK - {task.task_name}")
                    print(f"CREATED TIME - {task.created_time}")
                    print(f"UPDATE TIME - {task.updated_time}")
                    print(f"COMPLETED - {task.task_done}")
                    print(f"COMPLETED TIME - {task.completed_time}")
            if flag:
                print("\nTHERE IS NO COMPLETED TASK!")
            print()
            print('-'*55)
            print()
        elif option == '5':
            if task_list:
                print()
                print('-'*55)
                print("\nSELECT WHICH TASK TO UPDATE")
                for i, task in enumerate(task_list):
                    print()
                    print(f"TASK NO - {i+1}")
                    print(f"ID - {task.id}")
                    print(f"TASK - {task.task_name}")
                    print(f"CREATED TIME - {task.created_time}")
                    print(f"UPDATE TIME - {task.updated_time}")
                    print(f"COMPLETED - {task.task_done}")
                    print(f"COMPLETED TIME - {task.completed_time}")

                update_task_no = int(input("\nENTER TASK NO: "))
                update_task_name = input("ENTER NEW TASK: ")

                task_list[update_task_no-1].update_task(update_task_name)

                print("\nTASK UPDATED SUCCESSFULLY!\n")
                print('-'*55)
                print()
            else:
                print()
                print('-'*55)
                print()
                print("THERE IS NO TASK!")
                print()
                print('-'*55)
                print()
        elif option == '6':
            if task_list:
                flag = True
                print()
                print('-'*55)
                incompleteTask = []
                i = 0
                for task in task_list:
                    if (task.task_done == False):
                        flag = False
                        incompleteTask.append(task.id)
                        if i == 0:
                            print("\nSELECT WHICH TASK TO UPDATE")
                        i += 1
                        print()
                        print(f"TASK NO - {i}")
                        print(f"ID - {task.id}")
                        print(f"TASK - {task.task_name}")
                        print(f"CREATED TIME - {task.created_time}")
                        print(f"UPDATE TIME - {task.updated_time}")
                        print(f"COMPLETED - {task.task_done}")
                        print(f"COMPLETED TIME - {task.completed_time}")
                if incompleteTask:
                    complete_task_no = int(input("\nENTER TASK NO: "))
                    for task in task_list:
                        if (task.id == incompleteTask[complete_task_no-1]):
                            task.complete_task()

                    print("\nTASK COMPLETED SUCCESSFULLY!")
                if flag:
                    print()
                    print("THERE IS NO INCOMPLETE TASK!")

                print()
                print('-'*55)
                print()
            else:
                print()
                print('-'*55)
                print()
                print("THERE IS NO TASK!")
                print()
                print('-'*55)
                print()
        else:
            print("\nTHANKS FOR HAVING. IF YOU THINK EXIT IS UNEXPECTED, THEN PLEASE RUN THE PROJECT AGAIN ENTER THE RIGHT OPTION.\n")
            break
