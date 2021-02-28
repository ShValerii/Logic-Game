
def taskslist ():
    print ( '\n', 'Решение задач из LogicLike с использованием Python:', '\n', "Задача №1", '\n', 'Задача №2', '\n',
            'Задача №3', '\n', 'Задача №4', '\n', 'Задача №5' )


def taskmenu (numb) :
    print ( 'Если хотите попробовать решить самостоятельно, введите "Решить"' , '\n' ,
            'Чтобы увидеть ответ введите "Ответ"' , '\n' , 'Для просмотра кода решения введите "Код"' , '\n' )
    x = str ( input ( 'Поле ввода:' ) )
    x = x.lower ()
    task ( x, numb )

def inputnumb() :
    numb=0
    numb = int(input("Для перехода, введите номер задачи:"))
    choisetask ( numb )

def choisetask(numb) :
    if numb==1 : task1(numb)
    elif numb==2 : task2(numb)
    elif numb==3 : task3(numb)
    elif numb==4 : task4(numb)
    elif numb==5 : task5(numb)
    else:
        print("Вы ввели не кректное значение,\nповторите ввод используя числа от 1 до 5")
        inputnumb()

def taskcode(numb) :
    if numb==1 :
        j,answ = 0,0
        for i in range(1, 7):
            j = 9 - i
            if (2 * i) + (3 * j) == 23:
                answ=j
        return answ
    elif numb==2 :
        j = 0
        for i in range ( 1 , 11 ):
            j = 19 - i
            if i + 2 * j == 28:
                return j
    elif numb==3 :
        j = 0
        for i in range ( 1 , int ( 68 / 6 ) + 1 ):
            j = 10 - i
            if 6 * i + 8 * j == 68:
                return j
    elif numb==4 :
        b , c = 0 , 0
        for a in range ( 1 , 16 ):
            b = 1
            c = a - b
            if a + b + c == 16 and a - b == c:
                return a
    elif numb==5 :
        for kira in range ( 1 , int ( 81 / 4 ) ):
            if kira + kira * 5 + kira * 5 * 5 + kira * 5 * 5 * 2 == 81:
                return kira * 5

def task(x,numb) :
    if x == 'решить':
        while taskcode(numb) != yourtry():
            print('Не правильно')
        else:
            print('Правильно')
            endtask(numb)
    elif x == 'код':
        code(numb)
        endtask(numb)
    elif x == 'ответ':
        print('Ответ:',taskcode(numb))
        endtask(numb)

def code(numb) :
    if numb==1 :
        code = """j=0
for i in range(1, 7):
    j=9-i
    if (2 * i) + (3 * j) == 23:
        print('Ответ:',j) 
                    """
    elif numb==2 :
        code = """j=0
for i in range(1, 11):
    j=19-i
    if i + 2 * j == 28:
        print('Ответ:',j)
                  """
    elif numb==3 :
        code = """j=0
for i in range(1, int(68 / 6) + 1):
    j=10-i
    if 6 * i + 8 * j == 68:
        print('Ответ:',j) 
                """
    elif numb==4 :
        code = """b,c=0,0
for a in range(1, 16):
    b=1
    c=a-b
    if a + b + c == 16 and a - b == c:
        print('Ответ:',a)
                """
    elif numb==5 :
        code = """for kira in range(1,int(81/4)) :
    if  kira+kira*5+kira*5*5+kira*5*5*2==81:
        print('Ответ:',kira*5)"""
    print(code)

def task1(numb) :
    print('\n', 'У девяти трехколесных и двухколесных велосипедов вместе 23 колеса', '\n',
          'Сколько среди них трехколесных велосипедов?', '\n')
    taskmenu(numb)

def task2(numb) :
    print ( '\n' , '28 человек ехали на велосипедах и скутерах.' , '\n' ,
            'По одному на велосипеде и по двое на скутере.''\n' ,
            'Сколько было скутеров если велосипедов и скутеров вместе было 19?' , '\n' )
    taskmenu ( numb )

def task3(numb) :
    print ( '\n' , 'У десяти пауков и мух вместе 68 ног.' , '\n' , 'Сколько среди них пауков?' , '\n' )
    taskmenu ( numb )

def task4(numb):
    print ( '\n' , 'А+В+С=16' , '\n' , 'А-В=С' , '\n' , 'Чему равно А?' , '\n' )
    taskmenu ( numb )

def task5(numb) :
    print ( '\n' , 'Рома в 5 раз тарше Киры, Влад в 5 раз страрше Ромы,' , '\n' ,
            'Олег вдвое старше Влада, а всем четверым вместе 81 год.' , '\n' ,
            'Сколько лет Роме?' , '\n' )
    taskmenu ( numb )

def endtask(numb):
    print()
    print('Для возврата в пред. меню введите "Назад"')
    print('Для возврата в меню выбора задач введите "Меню"')
    print('Для выхода введите "Выход"')
    y=str(input('Поле ввода:'))
    y=y.lower()
    if y=='назад' :
        taskmenu(numb)
    elif y=='меню':
        taskslist()
        inputnumb()
    elif y=='выход' :
        exit()

def yourtry() :
    return  int(input('Введите Ваш вариант ответа:'))

taskslist()
inputnumb()

