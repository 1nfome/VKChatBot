from AddDelChatsParametrs import AddChatPar, DelChatParam
from Stats import GetMyFullStat, GetMyMiniStat, GetUserFullStat, GetUserMiniStat
from AddDelSwear import AddSwear, DelSwear
from SetName import SetBotName, SetUserName
from SendMessage import SendMsgToChat
from ShowUserMessages import Show
from GivePermissions import Give
from WarnBanKick import Warn, Unwarn, UnBan, Ban, Kick
from ChangeChatSet import PrintChatSet, ChangeMaxWarns, ChangeAuto_kick, ChangeSwearReact, ChangeMaxMessLen, ChangeHelloMessage, ChangeReturnHelloMessage
from SendAniMessage import Loading
from who import kto, kogo, na_skoko, doyouthink
from ShowOnline import WhoOnline
from ChatSettings import ChatSetToFile
from SettingsOfClasses import CreateGroup, DeleteGroup, AddGroupPermessions, DelGroupPermissions, ShowGroups, ShowGroupPrivileges, CleanGroup

def NumbersPermession(msg, UserStats, event, ChatSet, ChatParam, vk, IdBase, BotName, UserMessages,vk_session,session, UserNames, parametrs):
    if ('addchatpar' in msg) and UserStats[event.obj.from_id]['Privilege']==3:
        Temp=AddChatPar(msg, ChatSet, ChatParam, event, vk, IdBase)
        if Temp!=None:
            ChatSet=Temp[0]
            ChatParam=Temp[1]
    elif (('addchatpar' in msg) or ('delchatpar' in msg) or ('addswear' in msg) or ('delswear' in msg)) and UserStats[event.obj.from_id]['Privilege']!=3:
        message='Данная команда разрешена только создателю бота'
        SendMsgToChat(event, message, vk)
    elif ('delchatpar' in msg) and UserStats[event.obj.from_id]['Privilege']==3:
        variants={BotName+'delchatpar':1,BotName+' delchatpar':2,BotName+',delchatpar':1,BotName+', delchatpar':2}
        for elem in variants.keys():
            if msg.startswith(elem):
                Temp=DelChatParam(msg.split()[variants[elem]], ChatParam, ChatSet, event, vk, IdBase)
                if Temp!=None:
                    ChatSet=Temp[0]
                    ChatParam=Temp[1]
    elif ('addswear' in msg.lower()) and UserStats[event.obj.from_id]['Privilege']==3:
        AddSwear(msg, event, vk)
    elif ('delswear' in msg.lower()) and UserStats[event.obj.from_id]['Privilege']==3:
        DelSwear(msg, event, vk)
    elif ('sgp' in msg.lower()) and UserStats[event.obj.from_id]['Privilege']>1:
        ShowGroupPrivileges(msg, ChatSet, event, vk, UserStats)
    elif ('sgr' in msg.lower()) and UserStats[event.obj.from_id]['Privilege']>1:
        ShowGroups(ChatSet, event, vk, UserStats)
    elif ('dellgp' in msg.lower()) and UserStats[event.obj.from_id]['Privilege']>1:
        temp=DelGroupPermissions(msg, ChatSet, event, vk, UserStats)
        if temp!=None:
            ChatSet=temp
            ChatSetToFile(ChatSet, event.chat_id)
    elif ('addgp' in msg.lower()) and UserStats[event.obj.from_id]['Privilege']>1:
        temp=AddGroupPermessions(msg, ChatSet, event, vk, UserStats)
        if temp!=None:
            ChatSet=temp
            ChatSetToFile(ChatSet, event.chat_id)
    elif ('deletegroup' in msg.lower()) and UserStats[event.obj.from_id]['Privilege']>1:
        temp=DeleteGroup(msg, ChatSet, event, vk, UserStats)
        if temp!=None:
            ChatSet=temp
            ChatSetToFile(ChatSet, event.chat_id)
    elif ('creategroup' in msg.lower()) and UserStats[event.obj.from_id]['Privilege']>1:
        temp=CreateGroup(msg, ChatSet, UserStats, event, vk)
        if temp!=None:
            ChatSet=temp
            ChatSetToFile(ChatSet, event.chat_id)
    elif ('cleangroup' in msg.lower()) and UserStats[event.obj.from_id]['Privilege']>1:
        temp=CleanGroup(msg,ChatSet,event,vk,UserStats)
        if temp!=None:
            ChatSet=temp
            ChatSetToFile(ChatSet, event.chat_id)
    elif ('sum' in msg.lower()) and UserStats[event.obj.from_id]['Privilege']>0:
        Id=''
        Name=''
        num=''
        correct=True
#        for man in vk.messages.getConversationMembers(peer_id = 2000000000 + event.chat_id)['profiles']:
#            print("msg[msg.find('[id')+3:msg.find('|')]= {}\nman['id']= {}\n".format(msg[msg.find('[id')+3:msg.find('|')], man['id']))
#            if str(man['id'])==str(msg[msg.find('[id')+3:msg.find('|')]):
        Id=int(msg[msg.find('[id')+3:msg.find('|')])
        Name=UserStats[Id]['Name']
        try:
            num=int(msg[msg.find(']')+1:])
            print('vkbot num: {}\n'.format(num))
        except:
            MessageToChat='Некорректно введена команда\nПользуйтесь следующим шаблоном: ИБ_SUM @User «номер сообщения»'
            correct=False
            SendMsgToChat(event, MessageToChat, vk)
#        print('VkBot, ShowMessage\nName:{}\nnum:{}\n'.format(Name, num))
#        break
        if Id!='' and Name!=''and correct==True and 0<num<=150:
            Show(UserMessages, num, Id, Name, event, vk, vk_session, session)
        elif correct==True and 0<num<=150 and (Id=='' or Name==''):
            TextToMsg='В этом чате нет такого человека'
            SendMsgToChat(event, TextToMsg, vk)
        elif correct==True and num>150:
            TextToMsg='Я храню только последние 150 сообщений'
            SendMsgToChat(event, TextToMsg, vk)
        elif correct==True and num==0:
            TextToMsg='Где я тебе возьму нулевое сообщение? Его же ещё не написали'
            SendMsgToChat(event, TextToMsg, vk)
    elif ('give' in msg.lower()) and UserStats[event.obj.from_id]['Privilege']>1:
        Temp=Give(vk, event, msg, UserStats, UserMessages, vk_session, session, ChatSet, UserNames)
        if Temp!=None:
            UserStats=Temp
    elif ('unwarn' in msg.lower()) and UserStats[event.obj.from_id]['Privilege']>0:
        Temp=Unwarn(UserStats, event, UserNames, vk, msg)
        if Temp!=None:
            UserStats=Temp
    elif ('warn' in msg.lower()) and UserStats[event.obj.from_id]['Privilege']>0:
        Temp=Warn(UserStats, event, ChatSet, UserNames, vk, msg)
        if Temp!=None:
            UserStats=Temp
    elif ('unban' in msg.lower()) and UserStats[event.obj.from_id]['Privilege']>0:
        Temp=UnBan(UserStats, event, UserNames, vk, msg)
        if Temp!=None:
            UserStats=Temp
    elif ('ban' in msg.lower()) and UserStats[event.obj.from_id]['Privilege']>0:
        Temp=Ban(UserStats, event, UserNames, vk, msg)
        if Temp!=None:
            UserStats=Temp
    elif ('kick' in msg.lower()) and UserStats[event.obj.from_id]['Privilege']>0:
        Kick(UserStats, event, vk, msg)
###########################################################################################   ОБЩЕПОЛЬЗОВАТЕЛЬСКОЕ #######################################################################
    elif 'mfs' in msg.lower():
        print('твой MFS\n')
        GetMyFullStat(UserStats, event, ChatSet, vk, vk_session, session)
    elif 'ms' in msg.lower():
        print('твой MS\n')
        GetMyMiniStat(UserStats, event, ChatSet, vk)
    elif ('id' in msg.lower()) and ('fs' in msg.lower()):
        if UserStats[event.obj.from_id]['Privilege']>0:
            Id=''
            Name=''
#            for man in vk.messages.getConversationMembers(peer_id = 2000000000 + event.chat_id,fields='first_name_gen, last_name_gen')['profiles']:
#                print("msg[msg.find('[id')+3:msg.find('|')]= {}\nman['id']= {}\n".format(msg[msg.find('[id')+3:msg.find('|')], man['id']))
#                if str(man['id'])==str(msg[msg.find('[id')+3:msg.find('|')]):
            Id=int(msg[msg.find('[id')+3:msg.find('|')])
            Name=UserNames[Id]['gen']
#                    break
#                    print('id: {} Name: {} SecondName: {}\n'.format(Id,Name,SecondName))
            print('чужой FS\n')
            GetUserFullStat(UserStats, event, ChatSet, vk, Id, Name, vk_session, session)
        else:
            message='Данная команда разрешена только модераторам и админам'
            SendMsgToChat(event, message, vk)
    elif ('id' in msg.lower()) and ('stat' in msg.lower()):
        if UserStats[event.obj.from_id]['Privilege']>0:
            Id=''
            Name=''
#            for man in vk.messages.getConversationMembers(peer_id = 2000000000 + event.chat_id,fields='first_name_gen, last_name_gen')['profiles']:
#                print("msg[msg.find('[id')+3:msg.find('|')]= {}\nman['id']= {}\n".format(msg[msg.find('[id')+3:msg.find('|')], man['id']))
#                if str(man['id'])==str():
            Id=int(msg[msg.find('[id')+3:msg.find('|')])
            Name=UserNames[Id]['gen']
#                    Name=man['first_name_gen']
#                    SecondName=man['last_name_gen']
#                    break
#                    print('id: {} Name: {} SecondName: {}\n'.format(Id,Name,SecondName))
#            print('чужой stat\n')
            GetUserMiniStat(UserStats, event, ChatSet, vk, Id, Name)
        else:
            message='Данная команда разрешена только модераторам и админам'
            SendMsgToChat(event, message, vk)
    elif ('sbn' in msg.lower()):
        if ('all' in msg.lower()):
            tempUS=SetBotName(msg, event, vk, UserStats, IdBase, parametrs, UserNames, True)
        else:
            tempUS=SetBotName(msg, event, vk, UserStats, IdBase, parametrs, UserNames)
        if tempUS!=None:
            UserStats=tempUS
    elif ('smn' in msg.lower()):
        if ('all' in msg.lower()):
            tempUS=SetUserName(msg, event, vk, UserStats, UserNames, IdBase, parametrs, True)
        else:
            tempUS=SetUserName(msg, event, vk, UserStats, UserNames, IdBase, parametrs)
        if tempUS!=None:
            UserStats=tempUS
    elif ('scs' in msg.lower()) and UserStats[event.obj.from_id]['Privilege']>0:
        PrintChatSet(ChatSet, event, vk)
    elif 'cmw' in msg.lower() and UserStats[event.obj.from_id]['Privilege']>0:
        tempCS=ChangeMaxWarns(event, msg, ChatSet, vk)
        if tempCS!=None:
            ChatSet=tempCS
            ChatSetToFile(ChatSet, event.chat_id)
    elif 'cak' in msg.lower() and UserStats[event.obj.from_id]['Privilege']>0:
        tempCS=ChangeAuto_kick(event, msg, ChatSet, vk)
        if tempCS!=None:
            ChatSet=tempCS
            ChatSetToFile(ChatSet, event.chat_id)
    elif 'csr' in msg.lower() and UserStats[event.obj.from_id]['Privilege']>0:
        tempCS=ChangeSwearReact(event, msg, ChatSet, vk)
        if tempCS!=None:
            ChatSet=tempCS
            ChatSetToFile(ChatSet, event.chat_id)
    elif 'cmm' in msg.lower() and UserStats[event.obj.from_id]['Privilege']>0:
        tempCS=ChangeMaxMessLen(event, msg, ChatSet, vk)
        if tempCS!=None:
            ChatSet=tempCS
            ChatSetToFile(ChatSet, event.chat_id)
    elif 'chm' in msg.lower() and UserStats[event.obj.from_id]['Privilege']>0:
        tempCS=ChangeHelloMessage(event, msg, ChatSet, vk)
        if tempCS!=None:
            ChatSet=tempCS
            ChatSetToFile(ChatSet, event.chat_id)
    elif 'crhm' in msg.lower() and UserStats[event.obj.from_id]['Privilege']>0:
        tempCS=ChangeReturnHelloMessage(event, msg, ChatSet, vk)
        if tempCS!=None:
            ChatSet=tempCS
            ChatSetToFile(ChatSet, event.chat_id)
    elif UserStats[event.obj.from_id]['Privilege']==0:
        CommList=['mfs','ms','ban','warn','give','sum','scs','cmw','cak','csr','cmm','kick','chm','crhm']
        for com in CommList:
            if com in msg.lower():
                message='Данная команда разрешена только администраторам и модераторам чата'
                SendMsgToChat(event, message, vk)
    elif ('anima' in msg):
        Loading(event, vk)
    elif ('kto' in msg.lower()):
        kto(msg, UserNames, event, vk)
    elif ('kogo' in msg.lower()):
        kogo(msg, UserNames, event, vk)
    elif ('prc' in msg.lower()):
        na_skoko(event, vk)
    elif ('hdyt' in msg.lower()):
        doyouthink(event, vk)
    elif ('help' in msg.lower()):
        SendMsgToChat(event, 'Помощь:\nvk.com/@emptypixel-komandy-bota', vk)
    elif ('online' in msg.lower()):
        WhoOnline(vk,event,vk_session,session)


def ClassPermession(msg, UserStats, event, ChatSet, ChatParam, vk, IdBase, BotName, UserMessages,vk_session,session, UserNames, parametrs):
    if ('sgp' in msg.lower()) and 'sgp' in ChatSet['classes'][UserStats[event.obj.from_id]['Privilege']]['cmds']:
        ShowGroupPrivileges(msg, ChatSet, event, vk, UserStats)
    elif ('sgr' in msg.lower()) and 'sgr' in ChatSet['classes'][UserStats[event.obj.from_id]['Privilege']]['cmds']:
        ShowGroups(ChatSet, event, vk, UserStats)
    elif ('dellgp' in msg.lower()) and 'dellgp' in ChatSet['classes'][UserStats[event.obj.from_id]['Privilege']]['cmds']:
        temp=DelGroupPermissions(msg, ChatSet, event, vk, UserStats)
        if temp!=None:
            ChatSet=temp
            ChatSetToFile(ChatSet, event.chat_id)
    elif ('addgp' in msg.lower()) and 'addgp' in ChatSet['classes'][UserStats[event.obj.from_id]['Privilege']]['cmds']:
        temp=AddGroupPermessions(msg, ChatSet, event, vk, UserStats)
        if temp!=None:
            ChatSet=temp
            ChatSetToFile(ChatSet, event.chat_id)
    elif ('deletegroup' in msg.lower()) and 'deletegroup' in ChatSet['classes'][UserStats[event.obj.from_id]['Privilege']]['cmds']:
        temp=DeleteGroup(msg, ChatSet, event, vk, UserStats)
        if temp!=None:
            ChatSet=temp
            ChatSetToFile(ChatSet, event.chat_id)
    elif ('creategroup' in msg.lower()) and 'creategroup' in ChatSet['classes'][UserStats[event.obj.from_id]['Privilege']]['cmds']:
        temp=CreateGroup(msg, ChatSet, UserStats, event, vk)
        if temp!=None:
            ChatSet=temp
            ChatSetToFile(ChatSet, event.chat_id)
    elif ('cleangroup' in msg.lower()) and 'cleangroup' in ChatSet['classes'][UserStats[event.obj.from_id]['Privilege']]['cmds']:
        temp=CleanGroup(msg,ChatSet,event,vk,UserStats)
        if temp!=None:
            ChatSet=temp
            ChatSetToFile(ChatSet, event.chat_id)
    elif ('sum' in msg.lower()) and 'sum' in ChatSet['classes'][UserStats[event.obj.from_id]['Privilege']]['cmds']:
        Id=''
        Name=''
        num=''
        correct=True
#        for man in vk.messages.getConversationMembers(peer_id = 2000000000 + event.chat_id)['profiles']:
#            print("msg[msg.find('[id')+3:msg.find('|')]= {}\nman['id']= {}\n".format(msg[msg.find('[id')+3:msg.find('|')], man['id']))
#            if str(man['id'])==str(msg[msg.find('[id')+3:msg.find('|')]):
        Id=int(msg[msg.find('[id')+3:msg.find('|')])
        Name=UserStats[Id]['Name']
        try:
            num=int(msg[msg.find(']')+1:])
            print('vkbot num: {}\n'.format(num))
        except:
            MessageToChat='Некорректно введена команда\nПользуйтесь следующим шаблоном: ИБ_SUM @User «номер сообщения»'
            correct=False
            SendMsgToChat(event, MessageToChat, vk)
#        print('VkBot, ShowMessage\nName:{}\nnum:{}\n'.format(Name, num))
#        break
        if Id!='' and Name!=''and correct==True and 0<num<=150:
            Show(UserMessages, num, Id, Name, event, vk, vk_session, session)
        elif correct==True and 0<num<=150 and (Id=='' or Name==''):
            TextToMsg='В этом чате нет такого человека'
            SendMsgToChat(event, TextToMsg, vk)
        elif correct==True and num>150:
            TextToMsg='Я храню только последние 150 сообщений'
            SendMsgToChat(event, TextToMsg, vk)
        elif correct==True and num==0:
            TextToMsg='Где я тебе возьму нулевое сообщение? Его же ещё не написали'
            SendMsgToChat(event, TextToMsg, vk)
    elif ('give' in msg.lower()) and 'give' in ChatSet['classes'][UserStats[event.obj.from_id]['Privilege']]['cmds']:
        Temp=Give(vk, event, msg, UserStats, UserMessages, vk_session, session, ChatSet, UserNames)
        if Temp!=None:
            UserStats=Temp
    elif ('unwarn' in msg.lower()) and 'unwarn' in ChatSet['classes'][UserStats[event.obj.from_id]['Privilege']]['cmds']:
        Temp=Unwarn(UserStats, event, UserNames, vk, msg)
        if Temp!=None:
            UserStats=Temp
    elif ('warn' in msg.lower()) and 'warn' in ChatSet['classes'][UserStats[event.obj.from_id]['Privilege']]['cmds']:
        Temp=Warn(UserStats, event, ChatSet, UserNames, vk, msg)
        if Temp!=None:
            UserStats=Temp
    elif ('unban' in msg.lower()) and 'unban' in ChatSet['classes'][UserStats[event.obj.from_id]['Privilege']]['cmds']:
        Temp=UnBan(UserStats, event, UserNames, vk, msg)
        if Temp!=None:
            UserStats=Temp
    elif ('ban' in msg.lower()) and 'ban' in ChatSet['classes'][UserStats[event.obj.from_id]['Privilege']]['cmds']:
        Temp=Ban(UserStats, event, UserNames, vk, msg)
        if Temp!=None:
            UserStats=Temp
    elif ('kick' in msg.lower()) and 'kick' in ChatSet['classes'][UserStats[event.obj.from_id]['Privilege']]['cmds']:
        Kick(UserStats, event, vk, msg)
###########################################################################################   ОБЩЕПОЛЬЗОВАТЕЛЬСКОЕ #######################################################################
    elif 'mfs' in msg.lower() and 'mfs' in ChatSet['classes'][UserStats[event.obj.from_id]['Privilege']]['cmds']:
        print('твой MFS\n')
        GetMyFullStat(UserStats, event, ChatSet, vk, vk_session, session)
    elif 'ms' in msg.lower() and 'ms' in ChatSet['classes'][UserStats[event.obj.from_id]['Privilege']]['cmds']:
        print('твой MS\n')
        GetMyMiniStat(UserStats, event, ChatSet, vk)
    elif ('id' in msg.lower()) and ('fs' in msg.lower()) and 'fs' in ChatSet['classes'][UserStats[event.obj.from_id]['Privilege']]['cmds']:
        if UserStats[event.obj.from_id]['Privilege']>0:
            Id=''
            Name=''
#            for man in vk.messages.getConversationMembers(peer_id = 2000000000 + event.chat_id,fields='first_name_gen, last_name_gen')['profiles']:
#                print("msg[msg.find('[id')+3:msg.find('|')]= {}\nman['id']= {}\n".format(msg[msg.find('[id')+3:msg.find('|')], man['id']))
#                if str(man['id'])==str(msg[msg.find('[id')+3:msg.find('|')]):
            Id=int(msg[msg.find('[id')+3:msg.find('|')])
            Name=UserNames[Id]['gen']
#                    break
#                    print('id: {} Name: {} SecondName: {}\n'.format(Id,Name,SecondName))
            print('чужой FS\n')
            GetUserFullStat(UserStats, event, ChatSet, vk, Id, Name, vk_session, session)
        else:
            message='Данная команда разрешена только модераторам и админам'
            SendMsgToChat(event, message, vk)
    elif ('id' in msg.lower()) and ('stat' in msg.lower()) and 'stat' in ChatSet['classes'][UserStats[event.obj.from_id]['Privilege']]['cmds']:
        if UserStats[event.obj.from_id]['Privilege']>0:
            Id=''
            Name=''
#            for man in vk.messages.getConversationMembers(peer_id = 2000000000 + event.chat_id,fields='first_name_gen, last_name_gen')['profiles']:
#                print("msg[msg.find('[id')+3:msg.find('|')]= {}\nman['id']= {}\n".format(msg[msg.find('[id')+3:msg.find('|')], man['id']))
#                if str(man['id'])==str():
            Id=int(msg[msg.find('[id')+3:msg.find('|')])
            Name=UserNames[Id]['gen']
#                    Name=man['first_name_gen']
#                    SecondName=man['last_name_gen']
#                    break
#                    print('id: {} Name: {} SecondName: {}\n'.format(Id,Name,SecondName))
#            print('чужой stat\n')
            GetUserMiniStat(UserStats, event, ChatSet, vk, Id, Name)
        else:
            message='Данная команда разрешена только модераторам и админам'
            SendMsgToChat(event, message, vk)
    elif ('sbn' in msg.lower()) and 'sbn' in ChatSet['classes'][UserStats[event.obj.from_id]['Privilege']]['cmds']:
        if ('all' in msg.lower()):
            tempUS=SetBotName(msg, event, vk, UserStats, IdBase, parametrs, UserNames, True)
        else:
            tempUS=SetBotName(msg, event, vk, UserStats, IdBase, parametrs, UserNames)
        if tempUS!=None:
            UserStats=tempUS
    elif ('smn' in msg.lower()) and 'smn' in ChatSet['classes'][UserStats[event.obj.from_id]['Privilege']]['cmds']:
        if ('all' in msg.lower()):
            tempUS=SetUserName(msg, event, vk, UserStats, UserNames, IdBase, parametrs, True)
        else:
            tempUS=SetUserName(msg, event, vk, UserStats, UserNames, IdBase, parametrs)
        if tempUS!=None:
            UserStats=tempUS
    elif ('scs' in msg.lower()) and 'scs' in ChatSet['classes'][UserStats[event.obj.from_id]['Privilege']]['cmds']:
        PrintChatSet(ChatSet, event, vk)
    elif 'cmw' in msg.lower() and 'cmw' in ChatSet['classes'][UserStats[event.obj.from_id]['Privilege']]['cmds']:
        tempCS=ChangeMaxWarns(event, msg, ChatSet, vk)
        if tempCS!=None:
            ChatSet=tempCS
            ChatSetToFile(ChatSet, event.chat_id)
    elif 'cak' in msg.lower() and 'cak' in ChatSet['classes'][UserStats[event.obj.from_id]['Privilege']]['cmds']:
        tempCS=ChangeAuto_kick(event, msg, ChatSet, vk)
        if tempCS!=None:
            ChatSet=tempCS
            ChatSetToFile(ChatSet, event.chat_id)
    elif 'csr' in msg.lower() and 'csr' in ChatSet['classes'][UserStats[event.obj.from_id]['Privilege']]['cmds']:
        tempCS=ChangeSwearReact(event, msg, ChatSet, vk)
        if tempCS!=None:
            ChatSet=tempCS
            ChatSetToFile(ChatSet, event.chat_id)
    elif 'cmm' in msg.lower() and 'cmm' in ChatSet['classes'][UserStats[event.obj.from_id]['Privilege']]['cmds']:
        tempCS=ChangeMaxMessLen(event, msg, ChatSet, vk)
        if tempCS!=None:
            ChatSet=tempCS
            ChatSetToFile(ChatSet, event.chat_id)
    elif 'chm' in msg.lower() and 'chm' in ChatSet['classes'][UserStats[event.obj.from_id]['Privilege']]['cmds']:
        tempCS=ChangeHelloMessage(event, msg, ChatSet, vk)
        if tempCS!=None:
            ChatSet=tempCS
            ChatSetToFile(ChatSet, event.chat_id)
    elif 'crhm' in msg.lower() and 'crhm' in ChatSet['classes'][UserStats[event.obj.from_id]['Privilege']]['cmds']:
        tempCS=ChangeReturnHelloMessage(event, msg, ChatSet, vk)
        if tempCS!=None:
            ChatSet=tempCS
            ChatSetToFile(ChatSet, event.chat_id)
    elif ('anima' in msg) and 'anima' in ChatSet['classes'][UserStats[event.obj.from_id]['Privilege']]['cmds']:
        Loading(event, vk)
    elif ('kto' in msg.lower()) and 'kto' in ChatSet['classes'][UserStats[event.obj.from_id]['Privilege']]['cmds']:
        kto(msg, UserNames, event, vk)
    elif ('kogo' in msg.lower()) and 'kogo' in ChatSet['classes'][UserStats[event.obj.from_id]['Privilege']]['cmds']:
        kogo(msg, UserNames, event, vk)
    elif ('prc' in msg.lower()) and 'prc' in ChatSet['classes'][UserStats[event.obj.from_id]['Privilege']]['cmds']:
        na_skoko(event, vk)
    elif ('hdyt' in msg.lower()) and 'hdyt' in ChatSet['classes'][UserStats[event.obj.from_id]['Privilege']]['cmds']:
        doyouthink(event, vk)
    elif ('help' in msg.lower()) and 'help' in ChatSet['classes'][UserStats[event.obj.from_id]['Privilege']]['cmds']:
        SendMsgToChat(event, 'Помощь:\nvk.com/@emptypixel-komandy-bota', vk)
    elif ('online' in msg.lower()) and 'online' in ChatSet['classes'][UserStats[event.obj.from_id]['Privilege']]['cmds']:
        WhoOnline(vk,event,vk_session,session)
    else:
        CommList=['mfs','ms','ban','warn','give','sum','scs','cmw','cak','csr','cmm','kick','chm','crhm','sgp','sgr','dellgp','addgp','deletegroup','creategroup','cleangroup','stat','sbn','smn','anima','kto','kogo','prc','hdyt','help','online']
        for com in CommList:
            if com in msg.lower() and not com in ChatSet['classes'][UserStats[event.obj.from_id]['Privilege']]['cmds']:
                message='Данная команда разрешена только администраторам и модераторам чата'
                SendMsgToChat(event, message, vk)