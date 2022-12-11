from functions import get_to_do,write_to_do
import time
now=time.strftime("%b-%d,%Y,%H:%M:%S")
print("date and time",now)

user_prompt = "Type add , Show , Edit , complete or Exit:"

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    if user_action.startswith("add") or user_action.startswith("new"):
        item = user_action[4:] + "\n"
        x = get_to_do("Data.txt")
        x.append(item)
        write_to_do("Data.txt", x)

    elif user_action.startswith("show"):

        x = get_to_do("Data.txt")

        for index, i in enumerate(x):
            i = i.strip('\n')
            i = i.title()
            row = f"{index + 1}-{i}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(input("No. of task you wanted to edit? "))
            number = number - 1
            x = get_to_do("Data.txt")
            new_to_do = input("Enter the new task")
            x[number] = new_to_do + '\n'
            write_to_do("Data.txt", x)
        except ValueError:
            print("Please enter the No. of task you want to edit ")
            continue

    elif user_action.startswith("exit"):
        break

    elif user_action.startswith("complete"):
        try:
            number = int(input("Number of task you completed :"))
            x = get_to_do("Data.txt")
            index = number-1
            completed = x[index].strip('\n')
            x.pop(index)
            write_to_do("Data.txt", x)
            message = f"task {completed} completed"
            print(message)
        except IndexError:
            print("There is no task with this number")
            continue
    else:
        print("please enter a correct command")

print("Have a nice day!!")
