import text

def inputnumb() :
    numb = 0
    numb = int(input("Для перехода, введите номер задачи:"))
    choisetask(numb)


def choisetask(numb) :
    if numb == 1 :
        text.tasktext1()
        text.taskmenuprint()
        taskmenu(numb)
    elif numb == 2 :
        text.tasktext2()
        text.taskmenuprint()
        taskmenu(numb)
    elif numb == 3 :
        text.tasktext3()
        text.taskmenuprint()
        taskmenu(numb)
    elif numb == 4 :
        text.tasktext4()
        text.taskmenuprint()
        taskmenu(numb)
    elif numb == 5 :
        text.tasktext5()
        text.taskmenuprint()
        taskmenu(numb)
    else :
        text.taskexeption()
        inputnumb()

def taskmenu(numb) :
    x = str(input('Поле ввода:'))
    x = x.lower()
    if x == 'решить' or x == 'код' or x == 'ответ' :
        task(x, numb)
    else :
        text.repeat()
        taskmenu(numb)

def taskcode(numb) :
    if numb == 1 :
        j, answ = 0, 0
        for i in range(1, 7) :
            j = 9 - i
            if (2 * i) + (3 * j) == 23 :
                answ = j
        return answ
    elif numb == 2 :
        j = 0
        for i in range(1, 11) :
            j = 19 - i
            if i + 2 * j == 28 :
                return j
    elif numb == 3 :
        j = 0
        for i in range(1, int(68 / 6) + 1) :
            j = 10 - i
            if 6 * i + 8 * j == 68 :
                return j
    elif numb == 4 :
        b, c = 0, 0
        for a in range(1, 16) :
            b = 1
            c = a - b
            if a + b + c == 16 and a - b == c :
                return a
    elif numb == 5 :
        for kira in range(1, int(81 / 4)) :
            if kira + kira * 5 + kira * 5 * 5 + kira * 5 * 5 * 2 == 81 :
                return kira * 5

def code(numb) :
    if numb==1 :
        text.code1()
    elif numb==2 :
        text.code2()
    elif numb==3 :
        text.code3()
    elif numb==4 :
        text.code4()
    elif numb==5 :
        text.code5()
    text.endtaskprint()
    endtask(numb)

def task(x, numb) :
    if x == 'решить' :
        while taskcode(numb) != text.yourtry() :
            print('Не правильно')
        else :
            print('Правильно')
            text.endtaskprint()
            endtask(numb)

    elif x == 'код' :
        code(numb)

    elif x == 'ответ' :
        print('Ответ:', taskcode(numb))
        text.endtaskprint()
        endtask(numb)

    else :
        text.repeat()
        task(x, numb)

def endtask(numb) :
    y = str(input('Поле ввода:'))
    y = y.lower()
    if y=='назад' or y=='меню' or y=='выход' :
        if y == 'назад' :
            text.taskmenuprint()
            taskmenu(numb)
        elif y == 'меню' :
            text.taskslist()
            inputnumb()
        elif y == 'выход' :
            exit()
    else:
        text.repeat()
        endtask(numb)
