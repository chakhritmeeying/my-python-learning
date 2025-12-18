def uppercase_string(user_input):
    return user_input.upper()


def lowercase_string(user_input):
    return user_input.lower()


def string_length(user_input):
    return len(user_input)


user_input = input("Enter something: ")
print("Uppercase: ", uppercase_string(user_input))
print("Lowecase: ", lowercase_string(user_input))
print("Length: ", string_length(user_input))
