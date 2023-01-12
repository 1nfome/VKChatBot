from SendMessage import SendMsgToChat
from random import choice
from ShowUserMessages import Show

def Give(vk, event, msg, UserStats, UserMessages, vk_session, session, ChatSet, UserNames):
    GroupNameCheck=False
    Default=False
    correct=False
    Id=''
    Name=''
    num=''
    Gname=''
    admin=[]
    Permissions={'nom':{0:'Юзверь', 1:'Модератор', 2:'Одмэн', 3:'Создатель'},'тв':{0:'Юзверем', 1:'Модератором', 2:'Одмэном', 3:'Создателем'}}
    for man in vk.messages.getConversationMembers(peer_id = 2000000000 + event.chat_id)['profiles']:
#        print("msg[msg.find('[id')+3:msg.find('|')]= {}\nman['id']= {}\n".format(msg[msg.find('[id')+3:msg.find('|')], man['id']))
        if str(man['id'])==str(msg[msg.find('[id')+3:msg.find('|')]):
            Id=man['id']
            Name=man['first_name']+' '+man['last_name']
            try:
                num=int(msg[msg.find('] ')+2:msg.find('] ')+3])
                if 3>num>-1:
                    Default=True
                else:
                    Default=False
                    MessageToChat='Некорректно введена команда\nДля выдачи Default-привилегий пишите:\n'+UserStats[event.obj.from_id]['BotName']+' give '+msg[msg.find('[',0):msg.find(']',0)+1]+' <цифра от 0 до 2 включительно, "Юзверь"-"Одмэн" соответственно>'
                    SendMsgToChat(event, MessageToChat, vk)
#                print('VkBot num: {}\n'.format(int(num)))
            except:
                Gname=msg[msg.find('] ')+2:]
                for gn in ChatSet['classes'].keys():
                    if gn==Gname:
                        GroupNameCheck=True
                    break
                if GroupNameCheck==False:
                    MessageToChat='Некорректно введена команда\nДля выдачи привилегий группы пишите:\n'+UserStats[event.obj.from_id]['BotName']+' give '+msg[msg.find('[',0):msg.find(']',0)+1]+' <имя существующей группы>\n\nЧтобы посмотреть список группы введите:\n'+UserStats[event.obj.from_id]['BotName']+' sgr'
                    SendMsgToChat(event, MessageToChat, vk)
#            print('VkBot, ShowMessage\nName:{}\n'.format(Name))
            correct=True
            break
    if correct==False:
        MessageToChat='Ошибка!!! Данного человека нет в беседе!'
        SendMsgToChat(event, MessageToChat, vk)
    if (GroupNameCheck==True or Default==True):
        for man in vk.messages.getConversationMembers(peer_id = 2000000000 + event.chat_id)['items']:
            try:
                if man['is_admin']==True and (not str(man['member_id']).startswith('-')):
#                    print('VkBot список админовDDDD: {}\n'.format(man))
                    admin.append(man['member_id'])
#                    print('VkBot prava. spisok adminov: {}\n'.format(admin))
            except:
                pass
    if GroupNameCheck==True or Default==True:
        if Id==449891250:
            if (not Id in admin):
                MessageToChat=choice(['Возможно ты не вкурсе... Но этого делать не стоило)','Ты видимо не вкурсе... Не надо было так делать))','Ага, щас...Только разбег возьму'])
                SendMsgToChat(event, MessageToChat, vk)
                MessageToChat='Теперь '+UserStats[event.obj.from_id]['UserName']+' '+Permissions['nom'][0]
                UserStats[event.obj.from_id]['Privilege']=0
                SendMsgToChat(event, MessageToChat, vk)
            else:
                MessageToChat=choice(['Ну и зачем?)','Ай-яй-яй!','Ты видимо не вкурсе... Не надо так делать))','Ага, щас...Только разбег возьму'])
                SendMsgToChat(event, MessageToChat, vk)
        elif Id==event.obj.from_id:
            MessageToChat=choice(['Эм... Самому себе?)','А лайки ты тоже сам себе ставишь?','Тебе не кажется странным самому себе выдавать привелегии?'])
            SendMsgToChat(event, MessageToChat, vk)
        elif (Id in admin):
            if Default==True and num<2:
                MessageToChat='Это ты зря)'
                SendMsgToChat(event, MessageToChat, vk)
                MessageToChat='[id'+str(Id)+'|'+UserStats[Id]['Name']+'], [id'+str(event.obj.from_id)+'|'+UserStats[event.obj.from_id]['Name']+'] хотел отобрать у тебя админку'
                SendMsgToChat(event, MessageToChat, vk)
                Show(UserMessages, 1, event.obj.from_id, UserStats[event.obj.from_id]['Name'], event, vk, vk_session, session)
            if Default==True and num==2:
                if UserNames[Id]['sex']==1:
                    MessageToChat=choice(['А разве она не админ?','Так она вроде и так админ, разве нет?','А она не админ чтоли?'])
                    SendMsgToChat(event, MessageToChat, vk)
                if UserNames[Id]['sex']==2:
                    MessageToChat=choice(['А разве он не админ?','Так он вроде и так админ, разве нет?','А он не админ чтоли?'])
                    SendMsgToChat(event, MessageToChat, vk)
                if UserNames[Id]['sex']==0:
                    MessageToChat=choice(['А разве оно не админ?','Так оно вроде и так админ, разве нет?','А оно не админ чтоли?'])
                    SendMsgToChat(event, MessageToChat, vk)
                if str(UserStats[Id]['Privilege'])=='2':
                    if UserNames[Id]['sex']==1:
                        MessageToChat=choice(['Только что проверил, правана месте!','Есть у неё админка! Только что проверил!','Ничего не знаю! Сейчас вот посмотрел, права админа на месте!'])
                        SendMsgToChat(event, MessageToChat, vk)
                    if UserNames[Id]['sex']==2:
                        MessageToChat=choice(['Есть у него админка! Только что проверил!','Проверил: права админа на месте!','Всё у него есть! Только что проверил!'])
                        SendMsgToChat(event, MessageToChat, vk)
                    if UserNames[Id]['sex']==0:
                        MessageToChat=choice(['Хм... Проверка показал, что права админа на месте!','Оно и так админ! Только что проверил!','Ещё какой админ! Проверено!'])
                        SendMsgToChat(event, MessageToChat, vk)
                else:
                    MessageToChat=choice(['Оу... Сорри.. Сейчас всё будет!','Упс... Секундочку!','Ой.. А ведь и вправду.. Подождите немного!'])
                    SendMsgToChat(event, MessageToChat, vk)
                    MessageToChat=Name+' теперь - '+Permissions['nom'][2]
                    UserStats[Id]['Privilege']=2
                    SendMsgToChat(event, MessageToChat, vk)
        else:
            if Default==True:
                MessageToChat=choice([Name+' теперь - '+Permissions['nom'][num],'Отныне и до разжалования '+Name+' нарекается '+Permissions['тв'][num]])
                UserStats[Id]['Privilege']=num
                SendMsgToChat(event, MessageToChat, vk)
                return UserStats
            elif GroupNameCheck==True:
                MessageToChat=choice(['Отныне и до разжалования '+Name+' будет обладать правами группы "'+Gname+'"','Теперь '+Name+' будет обладать правами группы "'+Gname+'"','Отныне и до разжалования '+Name+' будет принадлежать группе группы "'+Gname+'"'])
                UserStats[Id]['Privilege']=Gname
                SendMsgToChat(event, MessageToChat, vk)
                return UserStats
    elif num==3 and (GroupNameCheck==True or Default==True):
        MessageToChat='Менять права человека можно только в радиусе от "Юзверя" до "Одмэна", что соответствует значениям от 0 до 2 включительно'
        SendMsgToChat(event, MessageToChat, vk)