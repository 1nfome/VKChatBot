from SendMessage import SendMsgToChat
from Exceptor import Except
import traceback
from copy import copy

cmdslist={'sum':'Просмотр сообщений другого пользователя',\
              'give':'Выдача привилегий',\
              'unwarn':'Снятие предупреждения', \
              'warn':'Выдача предупреждения',\
              'unban':'Разбан человека',\
              'ban':'Бан человека',\
              'kick':'Исключение человека из чата',\
              'mfs':'Просмотр полной статистики своих действия и информации о себе',\
              'ms':'Просмотр краткой статистики действий и информации о себе',\
              'fs':'Просмотр полной статистики действия и информации о другом человеке',\
              'stat':'Просмотр краткой статистики действия и информации о другом человеке',\
              'sbn':'Смена имени бота',\
              'smn':'Смена своего имени для бота',\
              'scs':'Просмотр настроек чата',\
              'cmw':'Изменение максимального количества предупреждений',\
              'cak':'Вкл/Выкл Авто-кика',\
              'csr':'Вкл/Выкл реакции на маты',\
              'cmm':'Изменение максимальной длины сохраняемого в базу сообщения',\
              'chm':'Смена приветственного сообщения',\
              'crhm':'Смена приветственного сообщения при возвращении в чат',\
              'anima':'Анимация в ЛС',\
              'kto':'Кто "это" сделал?',\
              'kogo':'Кого "это" коснулось?',\
              'prc':'Истина в процентах',\
              'hdyt':'Мнение Бота',\
              'help':'Помощь по Боту',\
              'online':'Кто онлайн?',\
              'spam':'спам'}




def CreateGroup(msg, ChatSet, UserStats, event, vk):
    i=0
    print('SettingsOfClasses CreateGroup msg: '+msg)
    while i<30:
        if msg.lower()[i:i+12]=='creategroup ':
            break
        i+=1
    i+=12
    if i<30:
        Gname=msg[i:]
        if ChatSet['classes']==0:
            ChatSet['classes']={}
            ChatSet['classes'][Gname]={}
            ChatSet['classes'][Gname]['smile']=''
            ChatSet['classes'][Gname]['cmds']=['start']
            ChatSet['classes'][Gname]['Can_spam']='False'
            message=UserStats[event.obj.from_id]['UserName']+', класс "'+Gname+'" успешно создан!'
            SendMsgToChat(event, message, vk)
        else:
            doublecheck=False
            for clas in ChatSet['classes'].keys():
                if Gname==clas:
                    message=UserStats[event.obj.from_id]['UserName']+', класс с данным именем уже есть. Чтобы обнулить его привилегии напишите:\n\n'+str(UserStats[event.obj.from_id]['BotName'])+' cleangroup '+str(Gname)
                    SendMsgToChat(event, message, vk)
                    doublecheck=True
                    break
            if doublecheck==False:
                ChatSet['classes'][Gname]={}
                ChatSet['classes'][Gname]['smile']=''
                ChatSet['classes'][Gname]['cmds']=['start']
                ChatSet['classes'][Gname]['Can_spam']='False'
                message=UserStats[event.obj.from_id]['UserName']+', класс "'+Gname+'" успешно создан!'
                SendMsgToChat(event, message, vk)
        return ChatSet
    else:
        message=UserStats[event.obj.from_id]['UserName']+', произошла ошибка при создании класса, скорее всего у бота слишком длинное имя'
        SendMsgToChat(event, message, vk)
        Except(traceback.format_exc(), event, vk)


def CleanGroup(msg,ChatSet,event,vk,UserStats):
    i=0
    while i<30:
        if msg.lower()[i:i+11]=='cleangroup ':
            break
        i+=1
    i+=11
    if i<30:
        Gname=msg[i:]
        if ChatSet['classes']==0:
            message='В этой беседе не создано ни одного класса. Сначала создайте класс, чтобы его обнулить'
            SendMsgToChat(event, message, vk)
        else:
            if Gname in list(ChatSet['classes'].keys()):
                ChatSet['classes'][Gname]={}
                ChatSet['classes'][Gname]['smile']=''
                ChatSet['classes'][Gname]['cmds']=['start']
                ChatSet['classes'][Gname]['Can_spam']='False'
                message=UserStats[event.obj.from_id]['UserName']+', класс "'+Gname+'" успешно обнулён!'
                SendMsgToChat(event, message, vk)
            else:
                message=UserStats[event.obj.from_id]['UserName']+', класс "'+Gname+'" не обнаружен среди классов группы!'
                SendMsgToChat(event, message, vk)
                message='Вот полный список классов данной беседы:\n\n'
                for clas in ChatSet['classes'].keys():
                    message+=clas+ChatSet['classes'][clas]['smile']+'\n'
                SendMsgToChat(event, message, vk)
        return ChatSet
    else:
        message=UserStats[event.obj.from_id]['UserName']+', произошла ошибка при создании класса, скорее всего у бота слишком длинное имя'
        SendMsgToChat(event, message, vk)
        Except(traceback.format_exc(), event, vk)



def DeleteGroup(msg, ChatSet, event, vk, UserStats):
    i=0
    while i<30:
        if list(msg)[i:i+12]==list('deletegroup '):
            break
        i+=1
    i+=12
    if i<30:
        IsClass=False
        for clas in ChatSet['classes'].keys():
            if msg[i:i+len(clas)]==clas:
                IsClass=True
                break
        if IsClass==True:
            message=UserStats[event.obj.from_id]['UserName']+', класс "'+clas+'" удалён из списка классов этой беседы'
            ChatSet['classes'].pop(clas)
            if str(ChatSet['classes'])=='{}':
                ChatSet['classes']=0
            SendMsgToChat(event, message, vk)
            return ChatSet
        else:
            message=UserStats[event.obj.from_id]['UserName']+', в данном чате не обнаружен класс под названием "'+msg[i:msg.find(' ',i+1)]+'"\nИмя класса необходимо вводить без префикса класса'
            SendMsgToChat(event, message, vk)
            if len(ChatSet['classes'].keys())>0:
                message=UserStats[event.obj.from_id]['UserName']+', вот полный список классов данной беседы:\n'
                for clas in ChatSet['classes'].keys():
                    message+=clas+ChatSet['classes'][clas]['smile']+'\n'
                SendMsgToChat(event, message, vk)
            else:
                message=UserStats[event.obj.from_id]['UserName']+', в этой беседе не создано ни одного класса'
                SendMsgToChat(event, message, vk)
    else:
        message=UserStats[event.obj.from_id]['UserName']+', произошла ошибка при удалении класса, скорее всего у бота слишком длинное имя'
        SendMsgToChat(event, message, vk)

def AddGroupPermessions(msg, ChatSet, event, vk, UserStats):
    i=0
    while i<30:
        if msg.lower()[i:i+6]=='addgp ':
            break
        i+=1
    i+=6
    if i<30:
        IsClass=False
        for clas in ChatSet['classes'].keys():
            if msg[i:i+len(clas)]==clas:
                IsClass=True
                break
        if IsClass==True:
            i+=len(clas)+1
            cmds=msg.lower()[i:].split()
            yes=[]
            already=[]
            notYet=[]
            no=[]
            for cmd in cmds:
                AtLeastOne=False
                for command in cmdslist.keys():
                    if cmd==command:
                        AtLeastOne=True
                        break
                if AtLeastOne==True:
                    if (not cmd in yes):
                        yes.append(cmd)
                else:
                    no.append(cmd)
            if 'spam' in yes:
                yes.remove('spam')
                if ChatSet['classes'][clas]['Can_spam']=='False':
                    message=UserStats[event.obj.from_id]['UserName']+', теперь бот БУДЕТ воспринимать повторяющиеся комманды людей, входящих в класс "'+clas+'"'
                    SendMsgToChat(event, message, vk)
                    ChatSet['classes'][clas]['Can_spam']='True'
                else:
                    message=UserStats[event.obj.from_id]['UserName']+', характеристика "Spam" класса "'+clas+'" УЖЕ имеет значение "True"'
                    SendMsgToChat(event, message, vk)
            for com in yes:
                if com in ChatSet['classes'][clas]['cmds']:
                    already.append(com)
                else:
                    notYet.append(com)
            if str(notYet)!='[]':
                tempcmdslist=copy(cmdslist)
                tempcmdslist.pop('spam')
                if notYet==list(tempcmdslist.keys()):
                    message=UserStats[event.obj.from_id]['UserName']+', теперь людям, входящим в класс "'+clas+'" будут доступны ВСЕ команды бота.\n\n\nТолько вот зачем нужно было создавать такой класс, если уже есть класс "Одмэн", который можно получить через:\n'+str(UserStats[event.obj.from_id]['BotName'])+' give 2'
                    if 'start' in ChatSet['classes'][clas]['cmds']:
                        ChatSet['classes'][clas]['cmds'].remove('start')
                    for com in notYet:
                        ChatSet['classes'][clas]['cmds'].append(com)
                    SendMsgToChat(event, message, vk)
                else:
                    message=UserStats[event.obj.from_id]['UserName']+', теперь людям, входящим в класс "'+clas+'" будет доступно:\n\n'
                    if 'start' in ChatSet['classes'][clas]['cmds']:
                        ChatSet['classes'][clas]['cmds'].remove('start')
                    for com in notYet:
                        message+='✅ '+cmdslist[com]+'\n'
                        ChatSet['classes'][clas]['cmds'].append(com)
                    SendMsgToChat(event, message, vk)
            if str(already)!='[]':
                message=UserStats[event.obj.from_id]['UserName']+', следующие команды УЖЕ доступны людям, входящим в класс "'+clas+'":\n\n'
                for com in already:
                    message+='▸ '+cmdslist[com]+'\n'
                SendMsgToChat(event, message, vk)
            if str(no)!='[]':
                if len(no)>1:
                    message=UserStats[event.obj.from_id]['UserName']+', команды '
                    for com in no:
                        message+='✖ '+com+'\n'
                    message+=' НЕ опознанны, а потому НЕ добавлены в список привилегий класса "'+clas+'"'
                    SendMsgToChat(event, message, vk)
                else:
                    message=UserStats[event.obj.from_id]['UserName']+', команда "'+no[0]+'" НЕ опознанна, а потому НЕ добавлена в список привилегий класса "'+clas+'"'
                    SendMsgToChat(event, message, vk)
            return ChatSet
        else:
            if ChatSet['classes']==0:
                message=UserStats[event.obj.from_id]['UserName']+', в данном чате не создано ни одного класса/группы. Сначала создайте хотябы одну, чтобы изменять её характеристики'
                SendMsgToChat(event, message, vk)
            else:
                message=UserStats[event.obj.from_id]['UserName']+', в данном чате не обнаружен класс под названием "'+msg[i:msg.find(' ',i+1)]+'"\nИмя класса необходимо вводить без префикса класса'
                SendMsgToChat(event, message, vk)
                message='Вот полный список классов данной беседы:\n\n'
                for clas in ChatSet['classes'].keys():
                    message+=clas+ChatSet['classes'][clas]['smile']+'\n'
                SendMsgToChat(event, message, vk)
    else:
        message=UserStats[event.obj.from_id]['UserName']+', произошла ошибка при увеличении прав класса, скорее всего у бота слишком длинное имя'
        SendMsgToChat(event, message, vk)

def DelGroupPermissions(msg, ChatSet, event, vk, UserStats):
    i=0
    while i<30:
        if msg.lower()[i:i+7]=='dellgp ':
            break
        i+=1
    i+=7
    if i<30:
        IsClass=False
        for clas in ChatSet['classes'].keys():
            if msg[i:i+len(clas)]==clas:
                IsClass=True
                break
        if IsClass==True:
            i+=len(clas)+1
            cmds=msg.lower()[i:].split()
            yes=[]
            needToDel=[]
            no=[]
            for cmd in cmds:
                AtLeastOne=False
                for command in cmdslist.keys():
                    if cmd==command:
                        AtLeastOne=True
                        break
                if AtLeastOne==True:
                    yes.append(cmd)
                else:
                    no.append(cmd)
            if 'spam' in yes:
                yes.remove('spam')
                if ChatSet['classes'][clas]['Can_spam']=='True':
                    ChatSet['classes'][clas]['Can_spam']='False'
                    message=UserStats[event.obj.from_id]['UserName']+', теперь бот НЕ будет воспринимать повторяющиеся команды людей, входящих в класс "'+clas+'"'
                    SendMsgToChat(event, message, vk)
                else:
                    message=UserStats[event.obj.from_id]['UserName']+', характеристика "Spam" класса "'+clas+'" УЖЕ имеет значение "False"'
                    SendMsgToChat(event, message, vk)
            for com in yes:
                if com in ChatSet['classes'][clas]['cmds']:
                    needToDel.append(com)
                    yes.remove(com)
            if str(needToDel)!='[]':
                if needToDel==list(cmdslist.keys()):
                    message=UserStats[event.obj.from_id]['UserName']+', теперь людям, входящим в класс "'+clas+'" НЕ будет доступна НИ ОДНА команда бота'
                    ChatSet['classes'][clas]['cmds']='start'
                    SendMsgToChat(event, message, vk)
                else:
                    message=UserStats[event.obj.from_id]['UserName']+', теперь людям, входящим в класс "'+clas+'" НЕ будет доступно:\n\n'
                    for com in needToDel:
                        message+='❌ '+cmdslist[com]+'\n'
                        ChatSet['classes'][clas]['cmds'].remove(com)
                    if str(ChatSet['classes'][clas]['cmds'])=='[]':
                        ChatSet['classes'][clas]['cmds'].append('start')
                    SendMsgToChat(event, message, vk)
            if str(yes)!='[]':
                message=UserStats[event.obj.from_id]['UserName']+', следующие команды УЖЕ не доступны людям, входящим в класс "'+clas+'":\n\n'
                for com in yes:
                    message+='▸ '+cmdslist[com]+'\n'
                SendMsgToChat(event, message, vk)
            if str(no)!='[]':
                if len(no)>1:
                    message=UserStats[event.obj.from_id]['UserName']+', команды '
                    for com in no:
                        message+='✖ '+com+'\n'
                    message+=' НЕ опознанны, а потому НЕ добавлены в список привилегий класса "'+clas+'"'
                else:
                    message=UserStats[event.obj.from_id]['UserName']+', команда '
                    for com in no:
                        message+='✖ '+com+'\n'
                    message+=' НЕ опознанна, а потому НЕ добавлена в список привилегий класса "'+clas+'"'
            return ChatSet
        else:
            if ChatSet['classes']==0:
                message=UserStats[event.obj.from_id]['UserName']+', в данном чате не создано ни одного класса/группы. Сначала создайте хотябы одну, чтобы изменять её характеристики'
                SendMsgToChat(event, message, vk)
            else:
                message=UserStats[event.obj.from_id]['UserName']+', в данном чате не обнаружен класс под названием "'+msg[i:msg.find(' ',i+1)]+'"\nИмя класса необходимо вводить без префикса класса'
                SendMsgToChat(event, message, vk)
                message='Вот полный список классов данной беседы:\n\n'
                for clas in ChatSet['classes'].keys():
                    message+=clas+ChatSet['classes'][clas]['smile']+'\n'
                SendMsgToChat(event, message, vk)
    else:
        message=UserStats[event.obj.from_id]['UserName']+', произошла ошибка при уменьшении прав класса'
        SendMsgToChat(event, message, vk)

def ShowGroups(ChatSet, event, vk, UserStats):
    if ChatSet['classes']!=0:
        message=UserStats[event.obj.from_id]['UserName']+', в этом чате существуют следующие классы:\n\n\n'
        for clas in ChatSet['classes'].keys():
            message+=clas+' '+ChatSet['classes'][clas]['smile']+'\n'
        SendMsgToChat(event, message, vk)
    else:
        message=UserStats[event.obj.from_id]['UserName']+', в этом чате нет классов'
        SendMsgToChat(event, message, vk)

def ShowGroupPrivileges(msg, ChatSet, event, vk, UserStats):
    i=0
    while i<30:
        if msg.lower()[i:i+4]=='sgp ':
            break
        i+=1
    i+=4
    if i<30:
        IsClass=False
        for clas in ChatSet['classes'].keys():
            if msg[i:i+len(clas)]==clas:
                IsClass=True
                break
        if IsClass==True:
            if (not 'start' in ChatSet['classes'][clas]['cmds']):
                message=UserStats[event.obj.from_id]['UserName']+', людям этой группы доступны следующие комманды:\n\n\n'
                for com in ChatSet['classes'][clas]['cmds']:
                    message+='▸ '+cmdslist[com]+'\n'
                SendMsgToChat(event, message, vk)
            else:
                message=UserStats[event.obj.from_id]['UserName']+', людям этой группы не доступны никакие команды'
                SendMsgToChat(event, message, vk)
        else:
            message=UserStats[event.obj.from_id]['UserName']+', в данном чате не обнаружен класс под названием "'+msg[i:msg.find(' ',i+1)]+'"\nИмя класса необходимо вводить без префикса класса'
            SendMsgToChat(event, message, vk)
            if len(ChatSet['classes'].keys())>0:
                message=UserStats[event.obj.from_id]['UserName']+', вот полный список классов данной беседы:\n'
                for clas in ChatSet['classes'].keys():
                    message+=clas+ChatSet['classes'][clas]['smile']+'\n'
                SendMsgToChat(event, message, vk)
            else:
                message=UserStats[event.obj.from_id]['UserName']+', в этой беседе не создано ни одного класса'
                SendMsgToChat(event, message, vk)
    else:
        message='Произошла ошибка при показе доступа класса'
        SendMsgToChat(event, message, vk)
