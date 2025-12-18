
def view_tasks(tasks):  # function to view all tasks
    for idx, t in enumerate(tasks, start=1):
        print(f"Task {idx}: {t}")


def search_tasks(tasks, search_keyword):  # Function to search tasks
    matching_tasks = []
    for i in tasks:
        if search_keyword.lower() in i.lower():
            matching_tasks.append(i)
    return matching_tasks


tasks = ["Play game", "Read book", "Buy something",
         "Write code", "study python", "study mathematics"]
# main program
view_tasks(tasks)
user_search = input("Enter the keyword you want to search for: ")
# variable to hold the returned matching tasks
matching_tasks = search_tasks(tasks, user_search)
# check if any matching tasks found
if not matching_tasks:
    print("No matching tasks found.")
else:
    print("Matching tasks: ")
    for idx, t in enumerate(matching_tasks, start=1):
        print(f"{idx}: {t}")


# search_task = []
# for idx, t in enumerate(tasks, start=1):
#     if user_search.lower() in t.lower():
#         search_task.append(t)
#     else:
#         continue
# if not search_task:
#     print("No matching tasks found.")
# else:
#     print("Matching tasks: ")
#     for idx, t in enumerate(search_task, start=1):
#         print(f"{idx}: {t}")
