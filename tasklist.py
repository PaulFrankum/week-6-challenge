11# import json module
import json

# Load json from file
# Ensuring 'data.json' exists in your directory or create it for testing
try:
    with open('task_list.json', 'r') as file:
        task_list = json.load(file)
except FileNotFoundError:
    print("Error: File not Found. Creating new file")
    task_list= [{"id":1, "task":"Sample", "status":"Open"}]
    with open('task_list.json', 'w') as file:
        json.dump(task_list, file, indent=4)
        print("Data Written to task_list.json")

except json.JSONDecodeerror:
    print("Error: Invalid JSON format. Creating new file")
    task_list=[{"id":1, "task":"Sample", "status":"Open"}]
    with open('task_list.json', 'w') as file:
        json.dump(task_list, file, indent=4)
        print("Data Written to task_list.json")

# define functions
# function to print task list
def view_task():
    # Print Json file
    print("")
    print("Task List")
    print("---------")
    print("")
    for item in task_list:
        print("ID:", item["id"], " Task:", item["task"], " Status:", item["status"])
    print("")
    print("")

# function create a task
def create_task():
    task=input("Enter task-")
    choicetest = True
    while choicetest:
        status=input("(O)pen/(C)losed?")
        # check O or C
        match status:
            case "o":
                status = "Open"
                choicetest = False
            case "O":
                status = "Open"
                choicetest = False
            case "c":
                status = "Closed"
                choicetest = False
            case "C":
                status = "Closed"
                choicetest = False
            case _:
                print("""
                     *************
                  
                     Invalid Entry
                  
                     *************
                  
                  """)
# Add task to JSON File
    new_id = len(task_list) +1
    new_task={"id":new_id, "task":task, "status":status}
    task_list.append(new_task)
    view_task()
# Writing JSON data to a file
    with open('task_list.json', 'w') as file:
        json.dump(task_list, file, indent=4)
        print("")
        print("Data Written to task_list.json")

# function to update a task
def update_task():
# print list 
    view_task()
# input task to update
    choicetest = True
    while choicetest:
        update_id = input("Enter ID of the the task you wish to update?")
# check valid
        number_of_id = len(task_list)+1
        if (update_id <= "0" or update_id >= str(number_of_id)):
            print("""
            *************
                  
            Invalid Entry
                  
            *************
                  
            """)
        else:
            choicetest = False
# get input of new value
    update_task=input("Enter task-")
    choicetest = True
    while choicetest:
        status=input("(O)pen/(C)losed?")
        # check O or C
        match status:
            case "o":
                update_status = "Open"
                choicetest = False
            case "O":
                update_status = "Open"
                choicetest = False
            case "c":
                update_status = "Closed"
                choicetest = False
            case "C":
                update_status = "Closed"
                choicetest = False
            case _:
                print("""
                     *************
                  
                     Invalid Entry
                  
                     *************
                  
                  """)
# Add task to JSON File
    new_task={"id":update_id, "task":update_task, "status":update_status}
    number_of_id = number_of_id-2
    del task_list[number_of_id]
#insert new_task
    task_list.insert(number_of_id, new_task)
# Writing JSON data to a file
    with open('task_list.json', 'w') as file:
        json.dump(task_list, file, indent=4)
        print("")
        print("Data Written to task_list.json")
    view_task()

# function to delete a task
def delete_task():
# print list 
    view_task()
# input task to delete
# check valid
    choicetest = True
    while choicetest:
        to_delete = input("which task do you wish to delete?")
        number_of_id = len(task_list)+1
        if (to_delete <= "0" or to_delete >= str(number_of_id)):
            print("""
            *************
                  
            Invalid Entry
                  
            *************
                  
            """)
        else:
            choicetest = False
# display task and ask are you sure(Y/N)?
    to_delete = int(to_delete)-1
    print(task_list[to_delete])
    choicetest = True
    while choicetest:
        y_n = input("Are you sure (Y/N)?")
        # check y or n
        match y_n:
            case "y":
                y_n ="Yes"
                # delete task
                del task_list[to_delete]                
                # redo ID number <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                to_end_of_json = len(task_list)+1
                for i in range(1,to_end_of_json):
                    task_list("id") = i
                # Writing JSON data to a file
                with open('task_list.json', 'w') as file:
                    json.dump(task_list, file, indent=4)
                    print("")
                    print("Data Written to task_list.json")
                choicetest = False
            case "Y":
                y_n ="Yes"
                # delete task
                del task_list[to_delete]
                # redo ID number <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                to_end_of_json = len(task_list)+1
                for i in range(1,to_end_of_json):
                    task_list("id") = i               
                # Writing JSON data to a file
                with open('task_list.json', 'w') as file:
                    json.dump(task_list, file, indent=4)
                    print("")
                    print("Data Written to task_list.json")
                choicetest = False
            case "n":
                y_n ="No"
                choicetest = False
            case "N":
                y_n ="No"
                choicetest = False
            case _:
                print("""
                        *************
                    
                        Invalid Entry
                    
                        *************
                    
                    """)
    view_task()

#Panic ---------------System overload -----------------
def calculator():
    print("""
        ******************************************************************
           
        Dear Receiver
          
                    You have just received the Ex-Mayors's virus.
          
                Since Ex-Mayor's are not so technoloyically advanced.
        
                              THIS IS A MANUAL VIRUS.
        
                 Please delete all the files on your hard disk 
                  yourself and send this to everyone you know.
        
                            
                            Thanks that would be great
                         Mayor The Hacker at mayor@hasbeen.com
    
        *****************************************************************

        """)

choice = 1
while choice != "6":
    print(" 1. Create Task")
    print(" 2. Update Task")
    print(" 3. Delete Task")
    print(" 4. View Tasks")
    print(" 5. Enter Jason Supreme Calculator")
    print(" 6. Exit")
    choice = input("choice:")
    match choice:
        case "1":
            create_task()
        case "2":
            update_task()
        case "3":
            delete_task()
        case "4":
            view_task()
        case "5":
            calculator()
        case "6":
            # Writing JSON data to a file
            with open('task_list.json', 'w') as file:
                json.dump(task_list, file, indent=4)
                print("")
                print("Data Written to task_list.json")
            print("")
            print("******************************")
            print("* GoodBye! Have a great day. *")
            print("******************************")
            break
        case _:
            print("""
                     *************
                  
                     Invalid Entry
                  
                     *************
                  
                  """)
