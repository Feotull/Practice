def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        # Основной вариант
        if root_word.lower().count(i.lower()) or i.upper().count(root_word.upper()):
            same_words.append(i)
    return same_words
    # Вариант 2
    #     if root_word.lower() in i.lower() or i.upper() in root_word.upper():
    #         same_words.append(word)
    # return same_words


print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
# ['richiest', 'richies']


print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))
# ['Disable']
