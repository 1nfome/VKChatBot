from SendMessage import SendMsgToChat
SetMode={'+':'True','-':'False'}
Mode={'True':'ВКЛючен ✅','False':'ВЫКЛючен ⛔'}
SMode={'True':'ВКЛючена ✅','False':'ВЫКЛючена ⛔'}

def PrintChatSet(ChatSet, event, vk):
    Space='ᅠ'
#    print("str(ChatSet[event.chat_id]['warn_numbers']): "+str(ChatSet[event.chat_id]['warn_numbers']))
#    print("str(ChatSet[event.chat_id]['kick_if_max_warn']): "+str(ChatSet[event.chat_id]['kick_if_max_warn']))
#    print("str(bool(ChatSet[event.chat_id]['kick_if_max_warn'])): "+str(bool(ChatSet[event.chat_id]['kick_if_max_warn'])))
#    print("Mode[bool(ChatSet[event.chat_id]['kick_if_max_warn'])]: "+Mode[bool(ChatSet[event.chat_id]['kick_if_max_warn'])])
#    print("SMode[bool(ChatSet[event.chat_id]['swear_answer'])]: "+SMode[bool(ChatSet[event.chat_id]['swear_answer'])])
#    print("str(ChatSet[event.chat_id]['max_message_len']): "+str(ChatSet[event.chat_id]['max_message_len']))
    TextToMessage=Space*3+'⚙Настройки беседы:🔧'\
                  '\n\nМаксимальное количество Warn-ов: '+str(ChatSet[event.chat_id]['warn_numbers'])+'⚠\n'\
                  'Авто-кик при достижении максимального кол-ва Warn-ов: '+Mode[ChatSet[event.chat_id]['kick_if_max_warn']]+'\n'\
                  'Реакция на маты: '+SMode[ChatSet[event.chat_id]['swear_answer']]+'\n'\
                  'Максимальное количество символов на сообщение, при превышении которого сообщение не сохраняется в базу: '+str(ChatSet[event.chat_id]['max_message_len'])+'📝\n'
    SendMsgToChat(event, TextToMessage, vk)

def ChangeMaxWarns(event, msg, ChatSet, vk):
    try:
        msg=msg.lower()
        Max=int(msg[msg.find('cmw')+3:])
        if 1<Max<31 :
            print('ChangeChatSet ChangeMaxWarns Max=',Max)
            ChatSet[event.chat_id]['warn_numbers']=Max
            TextToMessage='Новый максимум Warn-ов успешно установлен и равен: '+str(ChatSet[event.chat_id]['warn_numbers'])+'⚠\n'
            SendMsgToChat(event, TextToMessage, vk)
            return ChatSet
        elif Max>=31:
            TextToMessage='Максимальное количество предупреждений может быть не больше 30!'
            SendMsgToChat(event, TextToMessage, vk)
        elif Max<=1:
            TextToMessage='Минимальное количество предупреждений может быть не меньше 1!'
            SendMsgToChat(event, TextToMessage, vk)
    except ValueError:
        TextToMessage='Некорректно введена команда!\n Вводите команду в формате <Имя_бота> cmx <Число_Warn-ов>'
        SendMsgToChat(event, TextToMessage, vk)

def ChangeAuto_kick(event, msg, ChatSet, vk):
    msg=msg.lower()
    Set=str(msg[msg.find('cak')+4:])
    print('ChangeChatSet ChangeAuto_kick set: '+Set)
    if Set=='+' or Set=='-':
        print('ChangeChatSet ChangeAuto_kick Max= ',SetMode[Set])
        ChatSet[event.chat_id]['kick_if_max_warn']=str(SetMode[Set])
        TextToMessage='Авто-кик при достижении максимального кол-ва Warn-ов теперь: '+Mode[ChatSet[event.chat_id]['kick_if_max_warn']]
        SendMsgToChat(event, TextToMessage, vk)
        return ChatSet
    else:
        TextToMessage='Некорректно введена команда!\n Вводите команду в формате <Имя_бота> cak +//-'
        SendMsgToChat(event, TextToMessage, vk)

def ChangeSwearReact(event, msg, ChatSet, vk):
    msg=msg.lower()
    Set=str(msg[msg.find('csr')+4:])
    if Set=='+' or Set=='-':
        print('ChangeChatSet ChangeSwearReact Max= ',SetMode[Set])
        ChatSet[event.chat_id]['swear_answer']=SetMode[Set]
        TextToMessage='Реакция на маты теперь: '+SMode[ChatSet[event.chat_id]['swear_answer']]
        SendMsgToChat(event, TextToMessage, vk)
        return ChatSet
    else:
        TextToMessage='Некорректно введена команда!\n Вводите команду в формате <Имя_бота> csr +//-'
        SendMsgToChat(event, TextToMessage, vk)

def ChangeMaxMessLen(event, msg, ChatSet, vk):
    try:
        msg=msg.lower()
        Set=int(msg[msg.find('cmm')+3:])
        if Set<=4096:
            print('ChangeChatSet ChangeMaxMessLen Max= ',Set)
            ChatSet[event.chat_id]['max_message_len']=Set
            TextToMessage='Максимальное количество символов на сообщение теперь: '+str(ChatSet[event.chat_id]['max_message_len'])+'📝'
            SendMsgToChat(event, TextToMessage, vk)
            return ChatSet
        else:
            TextToMessage='Максимальная длина сообщения может быть не больше 4096 символов!'
        SendMsgToChat(event, TextToMessage, vk)
    except ValueError:
        TextToMessage='Некорректно введена команда!\n Вводите команду в формате <Имя_бота> cmm <Число_символов>'
        SendMsgToChat(event, TextToMessage, vk)


def ChangeHelloMessage(event, msg, ChatSet, vk):
    try:
        x=msg.lower().find('chm')
#        print('ChangeChatSet ChangeHelloMessage msg[msg[x]:msg[x]+1].lower()=',msg[msg[x]:msg[x]+1].lower())

        tmsg=msg[x:x+1].lower()+msg[x+2:]
        Set=str(tmsg[tmsg.find('chm')+3:])
        if len(Set)<=4096:
            print('ChangeChatSet ChangeMaxMessLen Max= ',Set)
            ChatSet[event.chat_id]['HelloMessage']=Set
            TextToMessage='Приветственное сообщение теперь:\n'+str(ChatSet[event.chat_id]['HelloMessage'])
            SendMsgToChat(event, TextToMessage, vk)
            return ChatSet
        else:
            TextToMessage='Максимальная длина сообщения может быть не больше 4096 символов!'
        SendMsgToChat(event, TextToMessage, vk)
    except ValueError:
        TextToMessage='Некорректно введена команда!\n Вводите команду в формате <Имя_бота> chm <Текст приветствия>'
        SendMsgToChat(event, TextToMessage, vk)

def ChangeReturnHelloMessage(event, msg, ChatSet, vk):
    try:
        x=msg.lower().find('crhm')
        tmsg=msg[x:x+2].lower()+msg[x+3:]
        Set=str(tmsg[tmsg.find('chm')+4:])
        if len(Set)<=4096:
            print('ChangeChatSet ChangeMaxMessLen Max= ',Set)
            ChatSet[event.chat_id]['ReturnHello']=Set
            TextToMessage='Приветственное сообщение вернувшемуся в чат теперь:\n'+str(ChatSet[event.chat_id]['ReturnHello'])
            SendMsgToChat(event, TextToMessage, vk)
            return ChatSet
        else:
            TextToMessage='Максимальная длина сообщения может быть не больше 4096 символов!'
        SendMsgToChat(event, TextToMessage, vk)
    except ValueError:
        TextToMessage='Некорректно введена команда!\n Вводите команду в формате <Имя_бота> crhm <Текст приветствия вернувшегося человека>'
        SendMsgToChat(event, TextToMessage, vk)