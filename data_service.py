"""модуль для роботи з файлами первинних даних
- зчитування та вивід на екран
"""

"""модуль зчитує первинні файли для обробки
"""

def get_tovars():
    """повертає список клієнтів b з файла `tovars.txt`
    Returns:
        tovars_list: список клієнтів
    """

    with open("./data/tovars.txt") as tovars_file:
        from_file = tovars_file.readlines()

    tovars_list = []
    for line in from_file:
        line_list = line.split(';')
        tovars_list.append(line_list)

    return tovars_list


def get_dovidniks():
    """повертає список накладних
    Returns:
        from_file: список накладних
    """
    
    with open('./data/dovidniks.txt') as dovidniks_file:
        from_file = dovidniks_file.readlines()

    
    # розбити строку на реквізити та перетворити формати (при потребі)
    
    # список-накопичувач
    dovidniks_list = []    
    
    for line in from_file:
        line_list = line.split(';')
        line_list[0] = int(line_list[0]) 
        line_list[1] = float(line_list[1]) 
        line_list[2] = float(line_list[2])
        line_list[3] = float(line_list[3])
        line_list[4] = float(line_list[4])
        line_list[5] = int(line_list[5])
        dovidniks_list.append(line_list)

    return dovidniks_list


def show_tovars(tovars):
    """виводить список товару по заданому інтервалу кодів
    Args:
        tovars (list): список товару
    """

    # задати інтервал виводу
    tovar_code_from = input("З якого кода товару? ")
    tovar_code_to   = input("По який кода товару? ")

    lines_found = 0

    for tovar in tovars:
        if tovar_code_from <= tovar[0] <= tovar_code_to:
            print ("код: {:5} назва: {:12} кг: {:3} ціна: {:5}".format(*tovar))
            lines_found += 1

    if lines_found == 0:
        print("Товарів по Вашому запиту не знайдено") 


def show_dovidniks(dovidniks):
    """виводить список цін на екран
    Args:
        dovidniks (list): список цін
    """

    for dovidnik in dovidniks:
        print("код товару: {:4} дата1: {:4}  дата2: {:4} дата3: {:4} дата4: {:4} рік: {:4}"
            .format(dovidnik[0], dovidnik[1], dovidnik[2], dovidnik[3], dovidnik[4], dovidnik[5]))


 # tovars = get_tovars()
 # show_tovars(tovars)

dovidniks = get_dovidniks()
show_dovidniks(dovidniks)