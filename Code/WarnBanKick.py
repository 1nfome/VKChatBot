from SendMessage import SendMsgToChat
from random import choice

def Unwarn(UserStats, event, UserNames, vk, msg):
    print('че анварним, да?')
    try:
        if UserStats[event.obj.reply_message['from_id']]['Privilege']==0 or (UserStats[event.obj.from_id]['Privilege']>1 and UserStats[event.obj.reply_message['from_id']]['Privilege']==1):
            if UserStats[event.obj.reply_message['from_id']]['Warn']!=0:
                UserStats[event.obj.reply_message['from_id']]['Warn']-=1
                message='Теперь у '+UserNames[event.obj.reply_message['from_id']]['gen']+' '+str(UserStats[event.obj.reply_message['from_id']]['Warn'])+' Warn'
                SendMsgToChat(event, message, vk)
            else:
                message='У него(неё) и так 0 Warn! Куда еще отнимать то?'
                SendMsgToChat(event, message, vk)
        elif UserStats[event.obj.reply_message['from_id']]['Privilege']==1 and (UserStats[event.obj.from_id]['Privilege']==1 or UserStats[event.obj.from_id]['Privilege']==0):
            message='Снимать Warn с модератора может только админ'
            SendMsgToChat(event, message, vk)
        elif event.obj.reply_message['from_id']==event.obj.from_id:
            message='Снять Warn с себя нельзя!'
            SendMsgToChat(event, message, vk)
        elif UserStats[event.obj.reply_message['from_id']]['Privilege']==2:
            message='Зачем пытаться снять Warn с админа, если ему нельзя его выдать?'
            SendMsgToChat(event, message, vk)
    except:
        if '[id' in msg:
            try:
                Id=int(msg[msg.find('[id')+3:msg.find('|')])
                if UserStats[Id]['Privilege']==0 or (UserStats[event.obj.from_id]['Privilege']>1 and UserStats[Id]['Privilege']==1):
                    if UserStats[Id]['Warn']!=0:
                        UserStats[Id]['Warn']-=1
                        message='Теперь у '+UserNames[Id]['gen']+' '+str(UserStats[Id]['Warn'])+' Warn'
                        SendMsgToChat(event, message, vk)
                    else:
                        message='У него(неё) и так 0 Warn! Куда еще отнимать то?'
                        SendMsgToChat(event, message, vk)
                elif UserStats[Id]['Privilege']==1 and (UserStats[event.obj.from_id]['Privilege']==1 or UserStats[event.obj.from_id]['Privilege']==0):
                    message='Снимать Warn с модератора может только админ'
                    SendMsgToChat(event, message, vk)
                elif Id==event.obj.from_id:
                    message='Снять Warn с себя нельзя!'
                    SendMsgToChat(event, message, vk)
                elif UserStats[Id]['Privilege']==2:
                    message='Зачем пытаться снять Warn с админа, если ему нельзя его выдать?'
                    SendMsgToChat(event, message, vk)
            except KeyError:
                message='Такого человека нет в чате'
                SendMsgToChat(event, message, vk)
        else:
            message='Некорректно написано команда!\n Пишите команду в формате:\n<Имя_ботя> unwarn <уведомление человеку>\nИли же перешлите сообщение человека, у которого хотите забрать Warn и напишите:\n<Имя_бота> unwarn'
            SendMsgToChat(event, message, vk)

def Warn(UserStats, event, ChatSet, UserNames, vk, msg):
    print('че варним, да?')
    print('warn chatparam: {}\n'.format(ChatSet))
    try:
        print('че варним, да?')
        if UserStats[event.obj['reply_message']['from_id']]['Privilege']==0 or (UserStats[event.obj.from_id]['Privilege']>1 and UserStats[event.obj['reply_message']['from_id']]['Privilege']==1):
            print('Все вроде норм')
            if ChatSet[event.chat_id]['warn_numbers']>UserStats[event.obj.reply_message['from_id']]['Warn']:
                print('Ваще всё заебись')
                UserStats[event.obj.reply_message['from_id']]['Warn']+=1
                message='Теперь у '+UserNames[event.obj.reply_message['from_id']]['gen']+' '+str(UserStats[event.obj.reply_message['from_id']]['Warn'])+' Warn из '+str(ChatSet[event.chat_id]['warn_numbers'])
                SendMsgToChat(event, message, vk)
            else:
                if ChatSet[event.chat_id]['kick_if_max_warn']=='True':
                        message=choice(['Неприятно было познакомиться. Уходите!','*Смачный пендаль*','Дверь вон там!👆🏻'])
                        SendMsgToChat(event, message, vk)
                        UserStats[event.obj.reply_message['from_id']]['Warn']=0
                        check=vk.messages.removeChatUser(chat_id = event.chat_id, user_id=event.obj.reply_message['from_id'])
                        if check!=1:
                            error={935:'Такого пользователя в чате нет',936:'Contact not found'}
                            message='Ошибка: '+error[check]
                            SendMsgToChat(event, message, vk)
                else:
                    message='Куда ему(ей) ещё? У него(неё) и так максимум!'
                    SendMsgToChat(event, message, vk)
        elif UserStats[event.obj.reply_message['from_id']]['Privilege']==1 and (UserStats[event.obj.from_id]['Privilege']==1 or UserStats[event.obj.from_id]['Privilege']==0):
            print('кеке')
            message='Выдавать Warn модератору может только админ'
            SendMsgToChat(event, message, vk)
        elif event.obj.reply_message['from_id']==event.obj.from_id:
            message='Зачем ты пытаешься выдать Warn самому себе?'
            SendMsgToChat(event, message, vk)
        elif UserStats[event.obj.reply_message['from_id']]['Privilege']==2:
            message='Админа нельзя Warn-ить'
            SendMsgToChat(event, message, vk)
    except:

        if '[id' in msg:
            Id=int(msg[msg.find('[id')+3:msg.find('|')])
            if UserStats[Id]['Privilege']==0 or (UserStats[event.obj.from_id]['Privilege']>1 and UserStats[Id]['Privilege']==1):
                if ChatSet[event.chat_id]['warn_numbers']>UserStats[Id]['Warn']:
                    UserStats[Id]['Warn']+=1
                    message='Теперь у '+UserNames[Id]['gen']+' '+str(UserStats[Id]['Warn'])+' Warn из '+str(ChatSet[event.chat_id]['warn_numbers'])
                    SendMsgToChat(event, message, vk)
                else:
                    if ChatSet[event.chat_id]['kick_if_max_warn']=='True':
                        message=choice(['Неприятно было познакомиться. Уходите!','*Смачный пендаль*','Дверь вон там!👆🏻'])
                        UserStats[Id]['Warn']=0
                        SendMsgToChat(event, message, vk)
                        check=vk.messages.removeChatUser(chat_id = event.chat_id, user_id=Id)
                        if check!=1:
                            error={935:'Такого пользователя в чате нет',936:'Contact not found'}
                            message='Ошибка: '+error[check]
                            SendMsgToChat(event, message, vk)
                    else:
                        message='Куда ему(ей) ещё? У него(неё) и так максимум!'
                        SendMsgToChat(event, message, vk)
            elif UserStats[Id]['Privilege']==1 and (UserStats[event.obj.from_id]['Privilege']==1 or UserStats[event.obj.from_id]['Privilege']==0):
                message='Выдавать Warn модератору может только админ'
                SendMsgToChat(event, message, vk)
            elif Id==event.obj.from_id:
                message='Зачем ты пытаешься выдать Warn самому себе?'
                SendMsgToChat(event, message, vk)
            elif UserStats[Id]['Privilege']==2:
                message='Админа нельзя Warn-ить'
                SendMsgToChat(event, message, vk)
        else:
            message='Некорректно написано команда!\n Пишите команду в формате:\n<Имя_ботя> warn <уведомление человеку>\nИли же перешлите сообщение человека, которому хотите выдать Warn и напишите:\n<Имя_бота> warn'
            SendMsgToChat(event, message, vk)


def UnBan(UserStats, event, UserNames, vk, msg):
    print('че анбаним, да?')
    try:
        if event.obj.reply_message['from_id']==event.obj.from_id:
            message='В чём логика попыток разбанить самого себя, если я не реагирую на сообщения забаненных?'
            SendMsgToChat(event, message, vk)
        elif UserStats[event.obj.reply_message['from_id']]['Privilege']==0 or (UserStats[event.obj.from_id]['Privilege']>1 and UserStats[event.obj.reply_message['from_id']]['Privilege']==1):
            if UserStats[event.obj.reply_message['from_id']]['BlackList']==1:
                UserStats[event.obj.reply_message['from_id']]['BlackList']=0
                message=UserNames[event.obj.reply_message['from_id']]['nom']+' успешно разбанен(а)'
                SendMsgToChat(event, message, vk)
            else:
                message='Но ведь '+UserNames[event.obj.reply_message['from_id']]['nom']+' не забанен(а)'
                SendMsgToChat(event, message, vk)
        elif UserStats[event.obj.reply_message['from_id']]['Privilege']==1 and (UserStats[event.obj.from_id]['Privilege']==1 or UserStats[event.obj.from_id]['Privilege']==0):
            message='Разбанить модератора может только админ'
            SendMsgToChat(event, message, vk)
        elif UserStats[event.obj.reply_message['from_id']]['Privilege']==2:
            message='Зачем пытаться разбанить админа, если его нельзя забанить?'
            SendMsgToChat(event, message, vk)
    except:
        if '[id' in msg:
            Id=int(msg[msg.find('[id')+3:msg.find('|')])
            if Id==event.obj.from_id:
                message='В чём логика попыток разбанить самого себя, если я не реагирую на сообщения забаненных?'
                SendMsgToChat(event, message, vk)
            elif UserStats[Id]['Privilege']==0 or (UserStats[event.obj.from_id]['Privilege']>1 and UserStats[Id]['Privilege']==1):
                if UserStats[Id]['BlackList']==1:
                    UserStats[Id]['Warn']=0
                    message=UserNames[Id]['nom']+' успешно разбанен(а)'
                    SendMsgToChat(event, message, vk)
                else:
                    message='Но ведь '+UserNames[Id]['nom']+' не забанен(а)'
                    SendMsgToChat(event, message, vk)
            elif UserStats[Id]['Privilege']==1 and (UserStats[event.obj.from_id]['Privilege']==1 or UserStats[event.obj.from_id]['Privilege']==0):
                message='Разбанить модератора может только админ'
                SendMsgToChat(event, message, vk)
            elif UserStats[Id]['Privilege']==2:
                message='Зачем пытаться разбанить админа, если его нельзя забанить?'
                SendMsgToChat(event, message, vk)
        else:
            message='Некорректно написано команда!\n Пишите команду в формате:\n<Имя_ботя> unban <уведомление человеку>\nИли же перешлите сообщение человека, которого хотите разбанить и напишите:\n<Имя_бота> unban'
            SendMsgToChat(event, message, vk)

def Ban(UserStats, event, UserNames, vk, msg):
    print('че баним, да?')
    try:
        print('UserStats ПОСЛЕ ban','\n',UserStats,'\n\n')
        if UserStats[event.obj['reply_message']['from_id']]['Privilege']==0 or (UserStats[event.obj.from_id]['Privilege']>1 and UserStats[event.obj['reply_message']['from_id']]['Privilege']==1):
            if UserStats[event.obj.reply_message['from_id']]['BlackList']==0:
                UserStats[event.obj.reply_message['from_id']]['BlackList']=1
                message=UserNames[event.obj.reply_message['from_id']]['nom']+' успешно забанен(а)'
                SendMsgToChat(event, message, vk)
            else:
                message='Но ведь '+UserNames[event.obj.reply_message['from_id']]['nom']+' уже забанена'
                SendMsgToChat(event, message, vk)
        elif UserStats[event.obj.reply_message['from_id']]['Privilege']==1 and (UserStats[event.obj.from_id]['Privilege']==1 or UserStats[event.obj.from_id]['Privilege']==0):
            message='Банить модератора может только админ'
            SendMsgToChat(event, message, vk)
        elif event.obj.reply_message['from_id']==event.obj.from_id:
            message='Зачем ты пытаешься забанить самого себя?'
            SendMsgToChat(event, message, vk)
        elif UserStats[event.obj.reply_message['from_id']]['Privilege']==2:
            message='Админа нельзя забанить'
            SendMsgToChat(event, message, vk)
    except:
        if '[id' in msg:
            Id=int(msg[msg.find('[id')+3:msg.find('|')])
            if UserStats[Id]['Privilege']==0 or (UserStats[event.obj.from_id]['Privilege']>1 and UserStats[Id]['Privilege']==1):
                if UserStats[Id]['BlackList']==0:
                    UserStats[Id]['BlackList']=1
                    message=UserNames[Id]['nom']+' успешно забанен(а) '
                    SendMsgToChat(event, message, vk)
                else:
                    message='Но ведь '+UserNames[Id]['nom']+' уже забанен(а)'
                    SendMsgToChat(event, message, vk)
            elif UserStats[Id]['Privilege']==1 and (UserStats[event.obj.from_id]['Privilege']==1 or UserStats[event.obj.from_id]['Privilege']==0):
                message='Банить модератора может только админ'
                SendMsgToChat(event, message, vk)
            elif Id==event.obj.from_id:
                message='Зачем ты пытаешься забанить самого себя?'
                SendMsgToChat(event, message, vk)
            elif UserStats[Id]['Privilege']==2:
                message='Админа нельзя забанить'
                SendMsgToChat(event, message, vk)
        else:
            message='Некорректно написано команда!\n Пишите команду в формате:\n<Имя_ботя> ban <уведомление человеку>\nИли же перешлите сообщение человека, которого хотите забанить и напишите:\n<Имя_бота> ban'
            SendMsgToChat(event, message, vk)


def Kick(UserStats, event, vk, msg):
    print('че кикаем, да?')
    try:
        print('че кикаем, да?')
        if UserStats[event.obj['reply_message']['from_id']]['Privilege']==0 or (UserStats[event.obj.from_id]['Privilege']>1 and UserStats[event.obj['reply_message']['from_id']]['Privilege']==1):
            print('Ваще всё заебись')
            message=choice(['Неприятно было познакомиться. Уходите!','*Смачный пендаль*','Дверь вон там!👆🏻'])
            SendMsgToChat(event, message, vk)
            UserStats[event.obj.reply_message['from_id']]['Warn']=0
            check=vk.messages.removeChatUser(chat_id = event.chat_id, user_id=event.obj.reply_message['from_id'])
            if check!=1:
                error={935:'Такого пользователя в чате нет',936:'Contact not found'}
                message='Ошибка: '+error[check]
                SendMsgToChat(event, message, vk)
        elif UserStats[event.obj.reply_message['from_id']]['Privilege']==1 and (UserStats[event.obj.from_id]['Privilege']==1 or UserStats[event.obj.from_id]['Privilege']==0):
            print('кеке')
            message='Кикнуть модератора может только админ'
            SendMsgToChat(event, message, vk)
        elif event.obj.reply_message['from_id']==event.obj.from_id:
            message='Зачем ты пытаешься кикнуть самого себя?'
            SendMsgToChat(event, message, vk)
        elif UserStats[event.obj.reply_message['from_id']]['Privilege']==2:
            message='Админа нельзя кикнуть'
            SendMsgToChat(event, message, vk)
    except KeyError:

        if '[id' in msg:
            Id=int(msg[msg.find('[id')+3:msg.find('|')])
            if UserStats[Id]['Privilege']==0 or (UserStats[event.obj.from_id]['Privilege']>1 and UserStats[Id]['Privilege']==1):
                message=choice(['Неприятно было познакомиться. Уходите!','*Смачный пендаль*','Дверь вон там!👆🏻'])
                UserStats[Id]['Warn']=0
                SendMsgToChat(event, message, vk)
                check=vk.messages.removeChatUser(chat_id = event.chat_id, user_id=Id)
                if check!=1:
                    error={935:'Такого пользователя в чате нет',936:'Contact not found'}
                    message='Ошибка: '+error[check]
                    SendMsgToChat(event, message, vk)
            elif UserStats[Id]['Privilege']==1 and (UserStats[event.obj.from_id]['Privilege']==1 or UserStats[event.obj.from_id]['Privilege']==0):
                message='Кикнуть модератора модератора может только админ'
                SendMsgToChat(event, message, vk)
            elif Id==event.obj.from_id:
                message='Зачем ты пытаешься кикнуть самого себя?'
                SendMsgToChat(event, message, vk)
            elif UserStats[Id]['Privilege']==2:
                message='Админа нельзя кикнуть'
                SendMsgToChat(event, message, vk)
        else:
            message='Некорректно написано команда!\n Пишите команду в формате:\n<Имя_ботя> kick <уведомление человеку>\nИли же перешлите сообщение человека, которого хотите кикнуть и напишите:\n<Имя_бота> kick'
            SendMsgToChat(event, message, vk)
    except:
        message='Этого человека нет в чате'
        SendMsgToChat(event, message, vk)