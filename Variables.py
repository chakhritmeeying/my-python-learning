"""
name = "Bella"
age = 27
height = 1.50
is_student = False

print("Name: " + name)
print("Age: " + str(age) + " years")
print("Height: " + str(height) + " meters")

print("Let's Introducte Yourself")
print("what is your name? ")
name = input("please enter your name ")
print("How old are you?")
age = input("please enter your age: ")
print("what is your height in meters?")
height = input("please enter  your height: ")
print("Are you a student? (yes/no)")
is_student = input("please enter yes or no: ")
print("Thank you for the information!")
print("this is your information:")
print("Your name is " + name + " , you are " + str(age) + " years old, your height is "
      + str(height) + " meters, and you are a student: " + is_student)
"""
information = dict(name="", age="", height="", is_student="")
for i in information:
    get_info = input("please enter your " + i + " ")
    information[i] = get_info

for i in information:
    print("Your " + i + " is " + information[i])
