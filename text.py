
def taskslist() :
    print('\n', 'Список задач: ', '\n', "Задача №1", '\n', 'Задача №2', '\n',
          'Задача №3', '\n', 'Задача №4', '\n', 'Задача №5')

def tasktext1() :
    print ('\n', 'У девяти трехколесных и двухколесных велосипедов вместе 23 колеса', '\n',
              'Сколько среди них трехколесных велосипедов?', '\n')
def tasktext2() :
    print ('\n', '28 человек ехали на велосипедах и скутерах.', '\n',
     'По одному на велосипеде и по двое на скутере.''\n',
     'Сколько было скутеров если велосипедов и скутеров вместе было 19?', '\n')

def tasktext3() :
    print ('\n', 'У десяти пауков и мух вместе 68 ног.', '\n', 'Сколько среди них пауков?', '\n')

def tasktext4() :
    print ('\n', 'А+В+С=16', '\n', 'А-В=С', '\n', 'Чему равно А?', '\n')

def tasktext5() :
    print ('\n', 'Рома в 5 раз тарше Киры, Влад в 5 раз страрше Ромы,', '\n',
              'Олег вдвое старше Влада, а всем четверым вместе 81 год.', '\n',
              'Сколько лет Роме?', '\n')
def taskexeption() :
    print ("Вы ввели не кректное значение,\nповторите ввод используя числа от 1 до 5")

def taskmenuprint() :
    print('Если хотите попробовать решить самостоятельно, введите "Решить"', '\n',
          'Чтобы увидеть ответ введите "Ответ"', '\n', 'Для просмотра кода решения введите "Код"', '\n')

def yourtry() :
    return int(input('Введите Ваш вариант ответа:'))

def code1():
    print ("j=0\n"
            "for i in range(1, 7):\n"
            "    j=9-i\n"
            "    if (2 * i) + (3 * j) == 23:\n"
            "        print('Ответ:',j) \n"
            "                    ")

def code2() :
    print ("j=0\n"
            "for i in range(1, 11):\n"
            "    j=19-i\n"
            "    if i + 2 * j == 28:\n"
            "        print('Ответ:',j)\n"
            "                  ")

def code3() :
    print ("j=0\n"
            "for i in range(1, int(68 / 6) + 1):\n"
            "    j=10-i\n"
            "    if 6 * i + 8 * j == 68:\n"
            "        print('Ответ:',j) \n"
            "                ")

def code4() :
    print ("b,c=0,0\n"
            "for a in range(1, 16):\n"
            "    b=1\n"
            "    c=a-b\n"
            "    if a + b + c == 16 and a - b == c:\n"
            "        print('Ответ:',a)\n"
            "                ")

def code5() :
    print ("for kira in range(1,int(81/4)) :\n"
            "    if  kira+kira*5+kira*5*5+kira*5*5*2==81:\n"
            "        print('Ответ:',kira*5)")

def endtaskprint() :
    print()
    print('Для возврата в пред. меню введите "Назад"')
    print('Для возврата в меню выбора задач введите "Меню"')
    print('Для выхода введите "Выход"')

def repeat() :
    print ("Неправильный ввод. Повторите ввод используя одно из предложеных значений.")
