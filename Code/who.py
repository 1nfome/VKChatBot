from random import choice, randint
from OpenFiles import OpenSwearList, CloseSwearList
from SendMessage import SendMsgToChat
randanswer=['жопа',\
            'гладиолус',
            'тетрагидропиранилциклопентилтетрагидропиридопиридин',\
            'сушка',\
            'баран',\
            'угол',\
            'свечка',\
            'квадрокоптер',\
            'фиалка','дриада',\
            'пеницилин',\
            'трахея',\
            'блок redstone',\
            'Wubba-Lubba-Dab-Dab!']

def kto(msg, UserNames, event, vk):
    SwearList=OpenSwearList('для проверки наличия мата в сообщении')
    Swear=SwearList.read().split()
    CloseSwearList('после считывания списка матов',SwearList)
    SC=False
    for word in msg.lower():
        if word in Swear:
            SC=True
            break
    if SC==True:
        message=choice(['Я думаю, что это именно ты)', 'Только ты тут такая(ой)','Мне кажется, что это ты','По-моему, это именно ты','Что-то мне подсказывает, что это именно ты','В зеркало глянь. Там есть кое-кто такой'])
        SendMsgToChat(event, message, vk)
    else:
        spisok=['Обэма', 'Паша Дуров', 'πдорас какой-то']
        Imena=[]
        for Id in UserNames:
            Imena.append(UserNames[Id]['nom'])
        x=randint(0,2)
        if x==0:
            print('who kto x0=',x)
            if randint(0,1)==0:
                sp=[]
                osobie=['конь в пальто', 'батя твой', 'дед Пихто']
                spisok.extend(osobie)
                for word in spisok:
                    sp.append(word[0].upper()+word[1:])
                sp.extend(Imena)
                message=choice(sp)
            else:
                message=choice(['Я не уверен, но по-моему это ', 'Скорее всего это ','Думаю, это ','Я не уверен, но возможно это ','Это однозначно ', ''])
                spisok.extend(Imena)
                message+=choice(spisok)
            SendMsgToChat(event, message, vk)
        elif x==1:
            print('who kto x1=',x)
            nums=randint(1,10)
            fingUp='👆🏻'
            fingDown='👇🏻'
            if nums==1:
                message=choice(['Мне кажется, это тот'+fingUp+' человек, на 1 сообщение выше моего','Мне кажется этот тот'+fingDown+' человек, который напишет следующее сообщение после моего'])
            elif 4>=nums>1:
                message=choice(['По-моим рачётам этот тот'+fingUp+' человек, что на '+str(nums)+' сообщения выше моего','Ошибки быть не может!\nЭтот тот'+fingDown+' человек, что будет '+str(nums)+' после моего сообщения!'])
            elif nums>=5:
                message=choice(['Это невероятно...\nНо исходя из моих расчётов, это тот'+fingUp+' человек, что был на '+str(nums)+' сообщений выше моего','Если я не ошибаюсь'+choice(['(а это бывает крайне редко)',''])+', то это тот'+fingDown+' человек, что будет '+str(nums)+' после моего сообщения'])
            SendMsgToChat(event, message, vk)
        elif x==2:
            print('who kto x2=',x)
            dontknow=['Вот, скажи, откуда я могу это знать?','Ты это сейчас серьёзно?!?!\nТы серьёзно, да?!!\nЯ грёбаный набор нулей и единиц! Херня построенная на чистом рандоме! Откуда, скажи, откуда я могу это знать?!?!?\n Или погоди... Ты наверное хочешь получить какой-то случайный ответ,да? Хорошо:\n'+choice(randanswer),'Понятия не имею','Откуда мне знать?','Это секретная информация','Не скажу','А тебе зачем?','Не знаю']
            message=choice(dontknow)
            SendMsgToChat(event, message, vk)


def kogo(msg, UserNames, event, vk):
    SwearList=OpenSwearList('для проверки наличия мата в сообщении')
    Swear=SwearList.read().split()
    CloseSwearList('после считывания списка матов',SwearList)
    SC=False
    for word in msg.lower():
        if word in Swear:
            SC=True
            break
    if SC==True:
        message=choice(['Я думаю, что именно тебя)', 'Из всех здесь присутствующих только тебя','Мне кажется, что тебя','По-моему, именно тебя','Что-то мне подсказывает, что именно тебя','В зеркало глянь. Там есть кое-кто такой'])
        SendMsgToChat(event, message, vk)
    else:
        spisok=['Обэму', 'Пашу Дурова', 'πдораса какого-то']
        Imena=[]
        for Id in UserNames:
            Imena.append(UserNames[Id]['gen'])
        x=randint(0,2)
        if x==0:
            print('whog kogo x0=',x)
            if randint(0,1)==0:
                sp=[]
                osobie=['коня в пальто', 'батю твоего', 'деда Пихто']
                spisok.extend(osobie)
                for word in spisok:
                    sp.append(word[0].upper()+word[1:])
                sp.extend(Imena)
                message=choice(sp)
            else:
                message=choice(['Я не уверен, но по-моему ', 'Скорее всего ','Думаю, ','Я не уверен, но возможно ','Однозначно ', ''])
                spisok.extend(Imena)
                message+=choice(spisok)
            SendMsgToChat(event, message, vk)
        elif x==1:
            print('who kogo x1=',x)
            nums=randint(1,10)
            fingUp='👆🏻'
            fingDown='👇🏻'
            if nums==1:
                message=choice(['Мне кажется, вот этого'+fingUp+' человека, на 1 сообщение выше моего','Мне кажется вот этого'+fingDown+' человека, который напишет следующее сообщение после моего'])
            elif 4>=nums>1:
                message=choice(['По-моим рачётам вон того'+fingUp+' человека, что на '+str(nums)+' сообщения выше моего','Это очень странно, но ошибки быть не может!\nЭто произойдёт с тем'+fingDown+' человеком, что будет '+str(nums)+' после моего сообщения!'])
            elif nums>=5:
                message=choice(['Это невероятно...\nНо исходя из моих расчётов, это произойдёт с тем'+fingUp+' человеком, что был на '+str(nums)+' сообщений выше моего','Если я не ошибаюсь'+choice(['(а это бывает крайне редко)',''])+', то того'+fingDown+' человека, что будет '+str(nums)+' после моего сообщения'])
            SendMsgToChat(event, message, vk)
        elif x==2:
            print('who kogo x2=',x)
            dontknow=['Вот, скажи, откуда я могу это знать?','Ты это сейчас серьёзно?!?!\nТы серьёзно, да?!!\nЯ грёбаный набор нулей и единиц! Херня построенная на чистом рандоме! Откуда, скажи, откуда я могу это знать?!?!?\n Или погоди... Ты наверное хочешь получить какой-то случайный ответ,да? Хорошо:\n'+choice(randanswer),'Понятия не имею','Откуда мне знать?','Это секретная информация','Не скажу','А тебе зачем?','Не знаю']
            message=choice(dontknow)
            SendMsgToChat(event, message, vk)


def na_skoko(event, vk):
    x=randint(0,1)
    if x==0:
        dontknow=['Вот, скажи, откуда я могу это знать?','Ты это сейчас серьёзно?!?!\nТы серьёзно, да?!!\nЯ грёбаный набор нулей и единиц! Херня построенная на чистом рандоме! Откуда, скажи, откуда я могу это знать?!?!?\n Или погоди... Ты наверное хочешь получить какой-то случайный ответ,да? Хорошо:\n'+choice(randanswer),'Понятия не имею','Откуда мне знать?','Это секретная информация','Не скажу','А тебе зачем?','Не знаю']
        message=choice(dontknow)
        SendMsgToChat(event, message, vk)
    elif x==1:
        message='Примерно на '+str(randint(0,100))+'%, '
        message+=choice(['не больше','не меньше'])
        SendMsgToChat(event, message, vk)

def doyouthink(event, vk):
    x=randint(0,2)
    if x==0:
        dontknow=['Вот, скажи, откуда я могу это знать?','Ты это сейчас серьёзно?!?!\nТы серьёзно, да?!!\nЯ грёбаный набор нулей и единиц! Херня построенная на чистом рандоме! Откуда, скажи, откуда я могу это знать?!?!?\n Или погоди... Ты наверное хочешь получить какой-то случайный ответ,да? Хорошо:\n'+choice(randanswer),'Понятия не имею','Откуда мне знать?','Это секретная информация','Не скажу','А тебе зачем?','Не знаю']
        message=choice(dontknow)
        SendMsgToChat(event, message, vk)
    elif x==1:
        message=choice(['Что правда, то правда','Воистину!','Это правда','Именно так','Само собой','Конечно!','Еще как!','Еще бы)'])
        SendMsgToChat(event, message, vk)
    elif x==2:
        message=choice(['Неа','Ложь, πздёшь и провокация','Это неправда','Никак нет','Само собой нет!','Конечно нет!','Гнусная ложь','Вранье'])
        SendMsgToChat(event, message, vk)