def get_count_of_entry_symbol(current_str, ch):
    entry_count = 0
    for item in current_str:
        if item == ch:
            entry_count += 1

    return entry_count


def reverse_str_word(current_str):
    word_array = current_str.split(" ")
    return " ".join(word for word in word_array[::-1])


entryCount = get_count_of_entry_symbol("12311212111", '2')
print("Кол-во вхождений", "Вхожденний не найденно" if entryCount <= 0 else entryCount)
print(reverse_str_word("кашу ела Саша"))
