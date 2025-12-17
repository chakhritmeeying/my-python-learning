
try:
    with open("demo.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    with open("demo.txt", "w") as file:
        file.write("This is a demo file.")
        print("demo.txt file created.")

while True:
    user_input = input(
        "Enter text to append to demo.txt (type 'exit' to quit): ")
    if user_input.lower().strip() == 'exit':
        with open("demo.txt", "w")as file:
            file.write("This is a demo file.")
        break
    with open("demo.txt", "a") as file:
        file.write(user_input + "\n")
        print("Text appended to demo.txt.")
