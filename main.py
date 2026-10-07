import json
Todo_File = "TododList.json"
#Check for previous data
try:
    with open(Todo_File, "r") as f:
        Tasks = json.load(f)
except FileNotFoundError:
        Tasks = []
        print("No File Found")

#Will Print the list it is given
def print_list(Tasks):
    for index, task in enumerate(Tasks, start=1):
        print(f'Task {index}: {task}')

def save_list():
    with open(Todo_File, "w") as f:
        json.dump(Tasks, f)


print("Hello welcome to Todo, What can I do for you?")
print("Options:\nWrite\nList")
user_input = input()


if user_input == "Write":
    while True:
        task = input("Add Task (Type done to finish): ")
        #Speciffically before bc if list then no need to add.
        if task == "Done":
            save_list()
            break
        Tasks.append(task)

if user_input == "List":
    print_list(Tasks)

