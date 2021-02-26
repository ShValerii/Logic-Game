def head():
    print('\n','Решение задач из LogicLike с использованием Python:','\n',
      'Задача №1','\n',
      'Задача №2','\n',
      'Задача №3','\n',
      'Задача №4','\n',
      'Задача №5')

def endtask():
    print('\n','Для возврата в пред. меню введите "Назад"')
    print('Для возврата в меню выбора задач введите "Меню"')
    print('Для выхода введите "Выход"')

    y=str(input('Поле ввода:'))
    y=y.lower()
    if y=='назад' :
        head()
    elif y=='меню':
        head()
        numb = int(input("Для перехода, введите номер задачи:"))
        
    elif y=='выход' :
        exit()


def choisemenu():
    print(' Для решения введите "Решить"', '\n', 'Для просмотра кода решения введите "Код"', '\n',
          'Для выхода введите "Выход"')

def choise():
    x = str(input('Поле ввода:'))
    output(x)

def output(x) :
    x=x.lower()
    if x=='выход' :
        exit()
    elif x=='код' :
        if numb == 1:
            print(code1)
            endtask()
        elif numb == 2:
            print(code2)
            endtask()
        elif numb == 3:
            print(code3)
            endtask()
        elif numb == 4:
            print(code4)
            endtask()
        elif numb == 5:
            print(code5)
            endtask()

    elif x=='решить' :
        if numb==1:
            task1()
            endtask()
        elif numb==2 :
            task2()
            endtask()
        elif numb==3 :
            task3()
            endtask()
        elif numb==4 :
            task4()
            endtask()
        elif numb==5 :
            task5()
            endtask()
def task1() :
    for i in range(1, 7):
        for j in range(1, 7):
            if (2 * i) + (3 * j) == 23:
                print(j, 'трехколесных велосипедов')

def task2():
    for i in range(1, 15):
        for j in range(1, 15):
            if i + j == 19 and i + 2 * j == 28:
                print('Было:', j, 'скутеров')

def task3():
    for i in range(1, int(68 / 6) + 1):
        for j in range(1, int(68 / 8) + 1):
            if i + j == 10 and 6 * i + 8 * j == 68:
                print(j, 'шт. пауков')

def task4():
    for a in range(1, 16):
        for b in range(1, 16):
            for c in range(1, 16):
                if a + b + c == 16 and a - b == c:
                    print('А равно:',a)

def task5():
            for kira in range(1, 81):
                if kira + kira * 5 + kira * 5 * 5 + kira * 5 * 5 * 2 == 81:
                    print('Роме:', kira * 5, 'лет')

head()
numb = int(input("Для перехода, введите номер задачи:"))
while 1<=numb<=5 :
    if numb==1 :
        print('\n','\n','У девяти трехколесных и двухколесных велосипедов вместе 23 колеса','\n',
              'Сколько среди них трехколесных велосипедов?','\n','\n')
        code1="""
for i in range(1,7) :
    for j in range(1,7):
        if (2*i)+(3*j)==23 :
            print(j ,"трехколесных велосипедов")
            """
        choisemenu()
        choise()

    elif numb==2 :
        print('\n','\n','28 человек ехали на велосипедах и скутерах.','\n',
              'По одному на велосипеде и по двое на скутере.''\n',
              'Сколько было скутеров если велосипедов и скутеров вместе было 19?','\n','\n')
        choisemenu()
        code2="""
for i in range(1,15) :
    for j in range(1,15):
        if  i+j==19 and i+2*j==28 :
            print('Было:',j,'скутеров')
             """
        choise()

    elif numb==3 :
        print('\n','\n','У десяти пауков и мух вместе 68 ног.','\n',
              'Сколько среди них пауков?','\n','\n')
        choisemenu()
        code3="""
for i in range(1,int(68/6)+1):
    for j in range(1,int(68/8)+1):
        if i+j==10 and 6*i+8*j==68:
            print(j,'шт. пауков')
            """
        choise()

    elif numb==4 :
        print('\n','\n','А+В+С=16','\n','А-В=С','\n'
              'Чему равно А?','\n','\n')
        choisemenu()
        code4="""
for a in range(1,16):
    for b in range(1,16):
        for c in range(1,16):
            if a+b+c==16 and a-b==c :
                print('А равно:',a)
                """
        choise()

    elif numb==5 :
        print('\n', '\n','Рома в 5 раз тарше Киры, Влад в 5 раз страрше Ромы,', '\n',
              'Олег вдвое старше Влада, а всем четверым вместе 81 год.','\n',
              'Сколько лет Роме?', '\n', '\n')
        choisemenu()
        code5="""
for kira in range(1,81) :
    if  kira+kira*5+kira*5*5+kira*5*5*2==81:
        print('Роме:',kira*5,'лет')
    """
        choise()







