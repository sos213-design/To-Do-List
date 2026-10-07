def print_list(Tasks):
    for task in Tasks:
        print(task)

Tasks = []
task = ""
print("Hello welcome to Todo, What can I do for you?")
print("Options: \n"
      "Write\n"
      "List")
user_input = input()


if user_input == "Write":
    while task != "List":
        task = input("Add Task: ")
        Tasks.append(task)
print_list(Tasks)

