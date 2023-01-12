# -*- coding: utf-8 -*-
from random import choice
import os
import os.path
import requests
import copy
import vk_api
import traceback
from vk_api import VkUpload
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from IdBase import StartIdBase, IsChatOnBase, ChatToIdBase, IdBaseToFile
from AddReadWriteUsersStats import AddChatToStat, WriteAllStats, ReadAllStats, NewUser
from ChatSettings import ReadChatSet, ChatSetToFile
from UsersMessages import ReadAndAddMessageToFile, counter
from AddDelUsersParametrs import AddUsersParametr, DelUsersParametr
from OpenFiles import OpenParam, CloseParam, OpenChatParam, CloseChatParam
from vk_api.utils import get_random_id
from SendMessage import SendMsgToChat, SendMsgToHuman
from Exceptor import Except
from ChooseCommand import ClassPermession, NumbersPermession
import sqlite3

#        self.help = 'комманды:\n/hw - Сказать "Привет мир"\n' \
#                    '/helloWorld - Привет мир на разных ЯП\n' \
#                    '/сбор - призвать всех в беседу (или хотя-бы попытаться)\n' \
#                    '/онлайн - проверить, кто онлайн в беседе\n' \
#                    '/кто <фраза, имя, прозвище, и т.д.> - рандомно выбирает\n' \
#                    'человека'

def sendMsgToChat(event, message, image = False, url = 'https://pbs.twimg.com/media/D4aTJ8yWAAE4GJu.jpg'):
    try:
        attachments = []
        if image:
            upload = VkUpload(vk_session)
            image_url = url
            image = session.get(image_url, stream=True)
            photo = upload.photo_messages(photos=image.raw)[0]
            attachments.append(
            'photo{}_{}'.format(photo['owner_id'], photo['id']))
            print('\nadress: {}\n', attachments)
        vk.messages.send(
                    attachment=','.join(attachments),
                    chat_id=event.chat_id,
                    message=message,
                    random_id=1
                )
    except Exception as e:
        print(e)

def MessageFromChat(msg, event, Debug, View, ViewMessage, vk):
    IdBase={}
    UserStats= {}
    ChatSet={}
    ChatParam={}
    UserMessages={}
    UserNames={}
    gens=['nom','gen','dat','acc','ins', 'abl']
    for man in vk.messages.getConversationMembers(peer_id = 2000000000 + event.chat_id,fields='sex, photo_id, first_name_nom, first_name_gen, first_name_dat, first_name_acc, first_name_ins, first_name_abl,, last_name_nom, last_name_gen, last_name_dat, last_name_acc, last_name_ins, last_name_abl')['profiles']:
#        print('VKbot names: {}\n'.format(man))
        UserNames[man['id']]={}
        for gen in gens:
            UserNames[man['id']][gen]=man['first_name_'+gen]+' '+man['last_name_'+gen]
        UserNames[man['id']]['sex']=man['sex']
#    print('VKbot UserNames: {}\n'.format(UserNames))
    if len(UserNames.keys())<2:
        SendMsgToChat(event, 'Извините, но я работаю только в чатах.\nБеседа на одного человека не считается за чат', vk)
        vk.messages.removeChatUser(chat_id=event.chat_id, member_id='-185153508')
    if Debug:
        print('Чат успешно считывается')

#------------------------------------------------------------------------------------------------------------------------------------------------
    parametrs={}
    if str(parametrs)=='{}':
        ParametrsFile=OpenParam('Что бы изначально считать параметры пользователей')
        for i in range(5):
            parametrs[ParametrsFile.readline()[:-1]]='0'
        for line in ParametrsFile:
            TextToFile=line.split()
            temp=str(TextToFile[0])
            try:
                temp2=int(TextToFile[1])
            except:
                temp2=str(' '.join(TextToFile[1:]))                                                     #!&!&&!&!&!&!&!&!&!&!&&!&!&!&!&!&!&&!&!&!&
            temp3=ParametrsFile.readline()[:-1]
            if Debug:
                print('параметр: ', temp, 'характеристика: ', temp2,' прим: ',temp3,'\n')
            parametrs[temp]=[temp2, temp3]
        CloseParam('После изначального считывания параметров', ParametrsFile)
#        print('\nparametrs= ', parametrs, '\n')
#------------------------------------------------------------------------------------------------------------------------------------------------
    if str(ChatParam)=='{}':
            ChatParamFile=OpenChatParam('Что бы изначально считать параметры чатов')
            for line in ChatParamFile:
                TextToFile=line.split()
                temP=str(TextToFile[0])
                try:
                    temP2=int(TextToFile[1])
                except:
                    temP2=str(' '.join(TextToFile[1:]))
                if Debug:
                    print('параметр чата: ', temP, 'default: ', temP2,'\n')
                ChatParam[temP]=temP2
            CloseChatParam('После изначального считывания параметров чатов', ChatParamFile)
#            print('\nchatparam= ', ChatParam, '\n')
#------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------
    if Debug:
        print('\nНачинается этап проверки UserStatsFile и UserStats на наличие данных \n')
#------------------------------------------------------------------------------------------------------------------------------------------------
    if (not os.path.isfile('/app/Data/UserStats/US_for_'+str(event.chat_id)+'_chat.txt')) and (str(UserStats)=='{}'):
#        print('кек\n\n')
        UserStats=AddChatToStat(copy.copy(parametrs), vk, UserStats, event, Debug)
        if Debug:
            print('\n\nparametrs после AddChatToStat:\n\n',parametrs,'\n\n')
    elif (os.path.isfile('/app/Data/UserStats/US_for_'+str(event.chat_id)+'_chat.txt')) and (str(UserStats)=='{}'):
#        print('лол\n\n')
        UserStats=ReadAllStats(parametrs, UserStats, event.chat_id)                                                           # Считываем все чаты
#        print('UserStats после чтения из файла','\n',UserStats,'\n\n')
#        print('UserStats ПОСЛЕ ReadAllStats','\n',UserStats,'\n\n')
#-------------------------------------------------------------------------------------------------------------------------------------------------------
    if Debug:
        print('\nЗакончился этап проверки UserStatsFile и UserStats на начилие данных\n')
        print('\nНачинается этап проверки наличия чата в статистике\n')
#--------------------------------------------------------------------------------------------------------------------------------------------------------
#    CheckChatId=False                                                           # проверяем наличие чата в статистике
#    for elem in UserStats.keys():
#        if int(elem)==int(event.chat_id):
#            CheckChatId=True
#            break
#--------------------------------------------------------------------------------------------------------------------------------------------------------
    if Debug:
        print('\nЗакончился этап проверки наличия чата в статистике\n')
        print('\nНачинается этап занесения чата в статистику в случае отсутствия его там\n')
#--------------------------------------------------------------------------------------------------------------------------------------------------------
#    if CheckChatId==False:                                                      # Если чата нет в статистике
#        UserStats=AddChatToStat(copy.copy(parametrs), vk, UserStats, event, Debug)
#        if Debug:
#            print('\n\nparametrs после AddChatToStat:\n\n',parametrs,'\n\n')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if Debug:
        print('\nЗакончился этап занесения чата в статистику в случае отсутствия его там\n')
        print('\nНачинается этап заполнения базы Id\n')
#    print('IdBase до начала: \n',IdBase,'\n')
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    IdBase=StartIdBase(IdBase, event, vk)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    CheckChatId=IsChatOnBase(IdBase, event)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if CheckChatId==False:
        IdBase=ChatToIdBase(IdBase, event, vk)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if (os.stat('/app/Data/IdBase.txt').st_size==0) or (CheckChatId==False):
        IdBaseToFile(IdBase)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if Debug:
        print('\nЗакончился этап заполнения базы Id\n')
        print('\nНачинается этап добавления нового участника в базу в случае его захода в чат\n')
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                   /-------------------------------------\
#-----------------------------------------------    | СЧИТЫВАЕМ ИЛИ СОЗДАЕМ НАСТРОЙКИ ЧАТА |    -------------------------------------------------------------------------------
#                                                   \-------------------------------------/
    if (not os.path.isfile('/app/Data/ChatsSettings/ChatSet_for_'+str(event.chat_id)+'_chat.txt')):
        ChatSet['parametrs']={}
        for elem in ChatParam.keys():
            ChatSet['parametrs'][elem]=ChatParam[elem]
        ChatSet['classes']=0
        ChatSetToFile(ChatSet, event.chat_id)                                                  #Записываем настройки чата в файл
    elif (os.path.isfile('/app/Data/ChatsSettings/ChatSet_for_'+str(event.chat_id)+'_chat.txt')):
        ChatSet=ReadChatSet(event.chat_id, ChatParam)                                              # Считываем все параметры и классы
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    TempUserStats=NewUser(event, UserStats, parametrs, vk, ChatSet)
    if TempUserStats!=None:
        UserStats=TempUserStats
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if Debug:
        print('\nЗакончился этап добавления нового участника в базу в случае его захода в чат\n')
        print('\nНачинается этап реакции в случае выхода из чата\n')
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    try:
        if str(event.object.action['type'])=='chat_kick_user':
            print('\nЧеловек вышел из чата\n')
    except Exception as e:
        if str(e)!="'NoneType' object is not subscriptable":
            print('\nПроблема при выходе человека из чата:\n',e,'\n\n')
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if Debug:
        print('\nЗакончился этап реакции в случае выхода из чата\n')
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if View:
        print('\nIdBase: \n',IdBase, '\n\n','UserStats','\n',UserStats,'\n\n')
#    print('проверка в VkBot # 5\n')
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    BotName=str(UserStats[event.obj.from_id]['BotName'])                  #Переносим имя бота для конкретного человека в переменную(укорачиваем путь до него)
#    print('проверка в VkBot # 6\n')
    UserStats[event.obj.from_id]['PersonCodeOld']=UserStats[event.obj.from_id]['PersonCode']
#    print('проверка в VkBot # 7\n')
    print('VkBot UserStats: '+str(UserStats)+'\n')
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                                                                                                #Записываем сообщения в файл
#    print('\nДО:\n\n\n\nChatSet:\n{}\n\nParametrs:\n{}\n\nUserStats:\n{}\n\nUserMessages:\n{}\n'.format(ChatSet,parametrs,UserStats,UserMessages))
#    print('UserStats до ReadAndAddMessageToFile','\n',UserStats,'\n\n')
    UserMessages, Spam=ReadAndAddMessageToFile(event, UserMessages, msg, ChatSet, session, vk_session)              #Записываем сообщение пользователя в файл
#    print('UserStats после ReadAndAddMessageToFile ДО counter','\n',UserStats,'\n\n')
    print('проверка в VkBot # 8\n')
    UserStats=counter(event, UserStats, UserMessages, vk, Spam, msg, BotName, ChatSet)                                    #Увеличиваем счётчик сообщений конкретного человека
#    print('Status после counter: {}\n'.format(UserStats[event.obj.from_id]['Status']))
#    print('UserStats ПОСЛЕ counter перед WriteAllStats','\n',UserStats,'\n\n')
#    print('\nПОСЛЕ:\n\n\n\nParametrs:\n{}\n\nUserStats:\n{}\n\nUserMessages:\n{}\n'.format(parametrs,UserStats,UserMessages))
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#    print('UserStats ПОСЛЕ WriteAllStats','\n',UserStats,'\n\n')
#    print('после writeallstats\n')
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    Temp=AddUsersParametr(BotName, msg, UserStats, event, parametrs, Debug, vk, IdBase)
#    print('проверка связи  ГЫГЫГГ\n\n')
    if Temp!=None:
        UserStats=Temp[0]
        parametrs=Temp[1]
#    print('UserStats ПОСЛЕ AddUsersParametr','\n',UserStats,'\n\n')
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#    print('проверка связи0000\n\n')
    Temp=DelUsersParametr(BotName, msg, UserStats, event, parametrs, Debug, vk, IdBase)
    if Temp!=None:
        UserStats=Temp[0]
        parametrs=Temp[1]
#    print('проверка связи\n\n')
#    print('UserStats ПОСЛЕ DelUsersParametr','\n',UserStats,'\n\n')
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if msg.startswith(BotName):
        if str(type(UserStats[event.obj.from_id]['Privilege']))=="<class 'int'>" and 4>UserStats[event.obj.from_id]['Privilege']>-1:
            if UserStats[event.obj.from_id]['Privilege']>0:
                NumbersPermession(msg, UserStats, event, ChatSet, ChatParam, vk, IdBase, BotName, UserMessages,vk_session,session, UserNames, parametrs)
            elif UserStats[event.obj.from_id]['BlackList']==0 and Spam==True:
                NumbersPermession(msg, UserStats, event, ChatSet, ChatParam, vk, IdBase, BotName, UserMessages,vk_session,session, UserNames, parametrs)
        else:
            if Spam==True:
                ClassPermession(msg, UserStats, event, ChatSet, ChatParam, vk, IdBase, BotName, UserMessages,vk_session,session, UserNames, parametrs)
            elif Spam==False and ChatSet['classes'][UserStats[event.obj.from_id]['Privilege']]['Can_spam']==True:
                ClassPermession(msg, UserStats, event, ChatSet, ChatParam, vk, IdBase, BotName, UserMessages,vk_session,session, UserNames, parametrs)


    if msg.startswith(BotName):
        if str(type(UserStats[event.obj.from_id]['Privilege']))=="<class 'int'>" and 4>UserStats[event.obj.from_id]['Privilege']>-1 :
            if UserStats[event.obj.from_id]['BlackList']==0 and Spam==False and UserStats[event.obj.from_id]['Privilege']==0:
                message=choice(['Я что, на попугая похож?','Читай мой ответ выше','Повторение ответа стоит 100 рублей.Виртуальная карта QIWI: 4890 4946 2224 3574','Я вроде бы уже отвечал на это','Я не люблю повторяться'])
                SendMsgToChat(event, message, vk)
        else:
            if Spam==False and ChatSet['classes'][UserStats[event.obj.from_id]['Privilege']]['Can_spam']==False:
                message=choice(['Я что, на попугая похож?','Читай мой ответ выше','Повторение ответа стоит 100 рублей.Виртуальная карта QIWI: 4890 4946 2224 3574','Я вроде бы уже отвечал на это','Я не люблю повторяться'])
                SendMsgToChat(event, message, vk)

    elif (not msg.startswith(BotName)) and UserStats[event.obj.from_id]['BlackList']==0:
        CommList=['mfs','ms','ban','warn','give','sum','scs','cmw','cak','csr','cmm','kick','chm','crhm','sgp','sgr','dellgp','addgp','deletegroup','creategroup','cleangroup','stat','sbn','smn','anima','kto','kogo','prc','hdyt','help','online']
        for com in CommList:
            if msg.lower()[(-1*(len(com))):]==com:
                if BotName=='Бот':
                    if UserNames[event.obj.from_id]['sex']==1:
                        message=choice(['Я "Бот", если что','Возможно ты забыла, но меня зовут Бот','"Бот", просто "Бот"!! Без ковычек и даже запятых','Вчера я вроде был "Бот". Сегодня скорее всего тоже🤔','Напоминаю, что меня зовут "Бот". И ни как иначе! По крайней мере, пока имя мне не сменишь'])
                        SendMsgToChat(event, message, vk)
                    elif UserNames[event.obj.from_id]['sex']==2:
                        message=choice(['Я "Бот", если что','Возможно ты забыл, но меня зовут Бот','"Бот", просто "Бот"!! Без ковычек и даже запятых','Вчера я вроде был "Бот". Сегодня скорее всего тоже🤔','Напоминаю, что меня зовут "Бот". И ни как иначе! По крайней мере, пока имя мне не сменишь'])
                        SendMsgToChat(event, message, vk)
                    elif UserNames[event.obj.from_id]['sex']==0:
                        message=choice(['Я "Бот", если что','Возможно ты забыло, но меня зовут Бот','"Бот", просто "Бот"!! Без ковычек и даже запятых','Вчера я вроде был "Бот". Сегодня скорее всего тоже🤔','Напоминаю, что меня зовут "Бот". И ни как иначе! По крайней мере, пока имя мне не сменишь'])
                        SendMsgToChat(event, message, vk)
                else:
                    if UserNames[event.obj.from_id]['sex']==1:
                        message=choice(['Я "{}" , если что','Возможно ты забыла, но ты же сама назвала меня "{}"','Гхм...Вообще-то я "{}" . Сама ведь меня так назвала!','Но ведь я "{}" !','Напоминаю, что меня зовут "{}" . И ни как иначе! По крайней мере, пока имя мне не сменишь']).format(BotName)
                        SendMsgToChat(event, message, vk)
                    elif UserNames[event.obj.from_id]['sex']==2:
                        message=choice(['Я "{}" , если что','Возможно ты забыл, но ты же сам назвал меня "{}"','Гхм...Вообще-то я "{}" . Сам ведь меня так назвал!','Но ведь я "{}" !','Напоминаю, что меня зовут "{}" . И ни как иначе! По крайней мере, пока имя мне не сменишь']).format(BotName)
                        SendMsgToChat(event, message, vk)
                    elif UserNames[event.obj.from_id]['sex']==0:
                        message=choice(['Я "{}" , если что','Возможно ты забыло, но ты же само назвало меня "{}" ','Гхм...Вообще-то я "{}" . Само ведь меня так назвало!','Но ведь я "{}" !','Напоминаю, что меня зовут "{}" . И ни как иначе! По крайней мере, пока имя мне не сменишь']).format(BotName)
                        SendMsgToChat(event, message, vk)
                break
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    WriteAllStats(parametrs, UserStats, event.chat_id)                                   # Записываем в файл все данные обо всех пользователях
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                     #Записываем настройки чата в файл
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if ViewMessage:
        if event.type == VkBotEventType.MESSAGE_NEW:
            check='ничего'
            try:
                if str(event.object.action['type'])=='chat_kick_user':
                    check='вышел'
                elif 'invite_user' in str(event.object.action['type']):
                    check='вошел'
            except:
                pass
            if check=='ничего':
                print('Новое сообщение:')
                print('От ', end='')
                print(UserNames[event.obj.from_id]['gen'])
                print('Из '+str(event.chat_id)+' чата')
                print('Текст:', event.obj.text)
            elif check=='вышел':
                print(event.obj.from_id,'Вышел(ла) из ',end='')
                print(str(event.chat_id)+' чата')
            elif check=='вошел':
                print(UserNames[event.obj.from_id]['gen'],'Вошел(ла) в ',end='')
                print(str(event.chat_id)+' чат')

#            vk.messages.send(
#                    peer_id=449891250,
#                    message=5000*'-',
#                    random_id=get_random_id()
#                )

#            print('\n', vk.messages.getConversationMembers(peer_id = 2000000000 + event.chat_id,fields='photo_id')['profiles'])
#            print('\n\n')
#            print('Список участников чата: \n')
#            for man in vk.messages.getConversationMembers(peer_id = 2000000000 + event.chat_id)['profiles']:
#                print(man,'\n')

        else:
            print(event.type)
            print('\n\n')
    if msg=='Живой' and UserStats[event.obj.from_id]['Privilege']==3:
        message='Ага'
        SendMsgToChat(event, message, vk)
#    print('UserMessages from VkBot: {}\n'.format(UserMessages))




#    for word in msg.lower().split():                  #перебираем все слова в переведенном в нижний регистр сообщении
#        if word.replace('ё', 'е') in SwearList:       #заменяя буквы "ё" на "е" ищем каждое слово в словаре матов
#            SwearListCheck = True

#    if not msg.startswith('/'):
#        return
#    args = msg.split()
#    if args[0] == '/hw':
#        sendMsgToChat(event, 'Привет мир!')
#    elif args[0] == '/сбор':
#        m = ''
#        if len(args) > 1:
#            for i in range(1, len(args)):
#                m += args[i] + ' '
#        else:
#            m = 'Общий сбор!\n'
#
#        members = vk.messages.getConversationMembers(peer_id = 2000000000 + event.chat_id)['profiles']
#
#        for member in members:
#            #print(member)
#            if not 'screen_name' in member.keys():
#                continue
#            m += '@' + member['screen_name'] + ', '
#        sendMsgToChat(event, m)
#    elif args[0] == '/кто':
#        if len(args) == 1:
#            args.append('Это ')
#        members = vk.messages.getConversationMembers(peer_id = 2000000000 + event.chat_id)['profiles']
#        i = random.randint(0, len(members) - 1)
#        member = members[i]
#        who = ''
#        for word in args[1:]:
#            who += word + ' '
#        sendMsgToChat(event, who + 'естественно ' + \
#                           member['first_name'] + ' ' + member['last_name'] + '!')
#    elif args[0] == '/онлайн':
#        online = []
#        members = vk.messages.getConversationMembers(peer_id = 2000000000 + event.chat_id)['profiles']
#        for member in members:
#            if member['online']:
#                online.append(member['first_name'] + ' ' + member['last_name'])
#        txt = 'Сейчас онлайн:' if len(online) > 1 else 'Никого нет онлайн, кроме вас.'
#        for user in online:
#            if len(online) < 2:
#                break
#            txt += user + ', '
#        txt += 'и бот.' if len(online) > 1 else ''
#        sendMsgToChat(event, txt)
#    else:
#        sendMsgToChat(event, help)


def MessageFromUser(event, msg, View):
    if View:
        if event.type == VkBotEventType.MESSAGE_NEW:
            print('Новое сообщение В ЛС:')
            print('Для меня от: ', end='')
            print(event.obj.from_id)
            print('Текст:', event.obj.text)
            print('\n\n')
        else:
            print(event.type)
            print('\n\n')
    message=choice(['Данный бот работает только в групповых чатах','Извините, но бот работает только в групповых чатах','Я работаю только в групповых чатах'])
    SendMsgToHuman(event, message, vk, {'main_photo':'-185153508_457239027'})


def main():
    print('начало')

    ViewEvent=1
    ViewMessage=1
    View=0
    Debug=0

    try:                                                                                                                            #пытаемся
        global vk_session, longpoll, session, vk                                                                                    #   настроить
        vk_session = vk_api.VkApi(token='64776a890f158851524c21ab5a66150ac0538560f6c21f540872ad189a60617fdfd30b900c406a046444d')    #       взаимодействие
        longpoll = VkBotLongPoll(vk_session, '185153508')                                                                           #           с vk_api
        session = requests.Session()
        vk = vk_session.get_api()
    except Exception as e:
            print('Ошибка при работе с vk_api: \n', e)

    print('перед циклом')
    while True:
        try:
            for event in longpoll.listen():
                if ViewEvent:
                    print('event= ', event, '\n\n')                                                                                     #просмотр типа события
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                if event.type == VkBotEventType.MESSAGE_NEW:
                    if (not str(event.obj.from_id).startswith('-')):
                        if event.from_chat:
                            MessageFromChat(event.obj.text, event, Debug, View, ViewMessage, vk)
                        if event.from_user:
                            MessageFromUser(event, event.obj.text, View)
        except:
            Except(traceback.format_exc(), event, vk)
    vk.messages.send(
                    peer_id=449891250,
                    message='Кароч я тут вылетел из While true и по идее должен отфутболиться обратно в main',
                    random_id=get_random_id()
                )
    main()



if __name__=='__main__':
    main()