course = " Python programming"
print(course)
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.find("P"))
print(course.replace("P", "A"))

user_input = "  Hello World  "
user_input_cleaned = user_input.lower()
user_input_cleaned = user_input_cleaned.strip()
print(user_input)
print(user_input_cleaned)
print(user_input.strip().lower())


print(course + " " + user_input_cleaned)
