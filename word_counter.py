def word_counter(text):
    word = text.split()
    return len(word)


def characters_counter(text):
    char_count = [char for char in text]
    return char_count


def main():
    text = input("Enter some text: ")
    print("Word count: ", word_counter(text))
    char_count = {char: text.count(char) for char in text}
    char = "\n".join(f"{idx} : {count}" for idx, count in char_count.items())
    print(f"Characters conut : {char}")
    print("Characters count : ", len(characters_counter(text)))


main()
