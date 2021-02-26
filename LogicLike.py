#ver1.6
def head():
    print('\n','Решение задач из LogicLike с использованием Python:','\n',
          'Задача №1','\n','Задача №2','\n','Задача №3','\n','Задача №4','\n','Задача №5')

def endtask():
    print()
    print('Для возврата в пред. меню введите "Назад"')
    print('Для возврата в меню выбора задач введите "Меню"')
    print('Для выхода введите "Выход"')
    y=str(input('Поле ввода:')).lower()
    if y=='назад' :
        choiseprint()
        task()
    elif y=='меню':
        head()
        numb = int(input("Для перехода, введите номер задачи:"))
    elif y=='выход' :
        exit()

def yourtry() :
    return  int(input('Введите Ваш вариант ответа:'))

def choiseprint():
    print('Если хотите попробовать решить самостоятельно, введите "Решить"','\n',
          'Чтобы увидеть ответ введите "Ответ"','\n','Для просмотра кода решения введите "Код"','\n')

def task() :
    x = str(input('Поле ввода:')).lower()
    if x == 'решить':
        while taskcode() != yourtry():
            print('Не правильно')
        else:
            print('Правильно')
            endtask()
    elif x == 'код':
        print(code)
        endtask()
    elif x == 'ответ':
        print('Ответ:',taskcode())
        endtask()
head()
numb = int(input("Для перехода, введите номер задачи:"))
if 1<=numb<=5 :
    if numb==1 :
        print('\n','У девяти трехколесных и двухколесных велосипедов вместе 23 колеса','\n',
              'Сколько среди них трехколесных велосипедов?','\n')
        choiseprint()
        def taskcode():
            j=0
            for i in range(1, 7):
                j=9-i
                if (2 * i) + (3 * j) == 23:
                    return j
        code="""j=0
for i in range(1, 7):
    j=9-i
    if (2 * i) + (3 * j) == 23:
        print(j ,"трехколесных велосипедов") 
        """
        task()
    elif numb==2 :
        print('\n','28 человек ехали на велосипедах и скутерах.','\n',
              'По одному на велосипеде и по двое на скутере.''\n',
              'Сколько было скутеров если велосипедов и скутеров вместе было 19?','\n')
        choiseprint()
        def taskcode():
            j=0
            for i in range(1, 11):
                j=19-i
                if i + 2 * j == 28:
                    return j
        code="""j=0
for i in range(1, 11):
    j=19-i
    if i + 2 * j == 28:
         print('Было:',j,'скутеров')
          """
        task()
    elif numb==3 :
        print('\n','У десяти пауков и мух вместе 68 ног.','\n','Сколько среди них пауков?','\n')
        choiseprint()
        def taskcode():
            j=0
            for i in range(1, int(68 / 6) + 1):
                j=10-i
                if 6 * i + 8 * j == 68:
                    return j
        code="""j=0
for i in range(1, int(68 / 6) + 1):
    j=10-i
    if 6 * i + 8 * j == 68:
        print(j,'шт. пауков') 
        """
        task()
    elif numb==4 :
        print('\n','А+В+С=16','\n','А-В=С','\n','Чему равно А?','\n')
        choiseprint()
        def taskcode():
            b,c=0,0
            for a in range(1, 16):
                b=1
                c=a-b
                if a + b + c == 16 and a - b == c:
                    return a
        code="""b,c=0,0
for a in range(1, 16):
    b=1
    c=a-b
    if a + b + c == 16 and a - b == c:
       print('А равно:',a)
        """
        task()
    elif numb==5 :
        print('\n','Рома в 5 раз тарше Киры, Влад в 5 раз страрше Ромы,', '\n',
              'Олег вдвое старше Влада, а всем четверым вместе 81 год.','\n',
              'Сколько лет Роме?','\n')
        choiseprint()
        def taskcode():
            for kira in range(1, int(81/4)):
                if kira + kira * 5 + kira * 5 * 5 + kira * 5 * 5 * 2 == 81:
                    return kira * 5
        code="""for kira in range(1,int(81/4)) :
    if  kira+kira*5+kira*5*5+kira*5*5*2==81:
        print('Роме:',kira*5,'лет')"""
        task()


