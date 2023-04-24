def requsetArrayFromUser():
    isLoop = True
    array = []
    print('Вводите слова по одному для добавления в массив. Если хотите закончить добавление введите слово "конец".')
    while isLoop == True:
        el = str(input('Введите слово: '))
        if (el.lower() != "конец"):
            array.append(el)
        else:
            isLoop = False
    return array
