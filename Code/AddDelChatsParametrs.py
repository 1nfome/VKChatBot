from ChatSettings import ReadChatSet, ChatSetToFile
from OpenFiles import OpenChatParam, CloseChatParam
from SendMessage import SendMsgToChat
from copy import copy

def AddChatPar(msg, ChatSet, ChatParam, event, vk, IdBase):
    i=0
    while i<30:
        if list(msg)[i:i+11]==list('addchatpar '):
            break
        i+=1
    i+=11
    FirstPoint=i
    if i<30:
        while FirstPoint<70:
            if list(msg)[FirstPoint]=='.':
                break
            FirstPoint+=1
        FirstPoint+=1
        if FirstPoint<70:
            Temp1=str(''.join(list(msg)[i:FirstPoint-1]))
            Temp2=''.join(list(msg)[FirstPoint:])
            try:
                Temp2=int(Temp2)
            except:
                Temp2=str(Temp2)
            print('AddChatPar ChatSet до цикла: '+str(ChatSet))
            for chat in IdBase.keys():
                print('Номер чата в цикле {} из {}'.format(chat,str(IdBase.keys())))
                ChatSet=ReadChatSet(chat, ChatParam)
                print('AddChatPar ChatSet считали: '+str(ChatSet))
                ChatSet['parametrs'][Temp1]=Temp2
                print('AddChatPar ChatSet добавили: '+str(ChatSet))
                ChatSetToFile(ChatSet, chat)
            ChatParam[Temp1]=Temp2
            ChatSet=ReadChatSet(event.chat_id, ChatParam)
            ChatParamFile=OpenChatParam('Для добавления нового параметра', 'a')
            TextToFile=Temp1+' '+str(Temp2)+'\n'
            ChatParamFile.write(TextToFile)
            CloseChatParam('После добавления нового параметра', ChatParamFile)
            ToReturn=[]
            ToReturn.append(ChatSet)
            ToReturn.append(ChatParam)
            message='Параметр '+str(Temp1)+', имеющий Default: '+str(Temp2)+' успешно добавлен в список параметров чата и список настроек чатов'
            SendMsgToChat(event, message, vk)
            return ToReturn
        else:
            message='Название характеристики должно быть не длиннее ~40 символов'
            SendMsgToChat(event, message, vk)
    else:
        message='Сори, но походу у бота слишком длинное имя'
        SendMsgToChat(event, message, vk)


def DelChatParam(param, ChatParam, ChatSet, event, vk, IdBase):
    message='Параметр '+str(param)+', имеющий Default: '+str(ChatParam[str(param)])+' успешно удалён из списка параметров чата и списка настроек чатов'
    NewChatPar=copy(ChatParam)
    NewChatPar.pop(param)
    print('AddDelChatsParametrs DelChatParam NewChatPar '+str(NewChatPar))
    print('DelChatParam ChatSet до цикла: '+str(ChatSet))
    for chat in IdBase.keys():
        ChatSet=ReadChatSet(chat, ChatParam)
        print('DelChatParam ChatSet до удаления: '+str(ChatSet))
        ChatSet['parametrs'].pop(param)
        print('DelChatParam ChatSet после удаления: '+str(ChatSet))
        ChatSetToFile(ChatSet, chat)
    ChatSet=ReadChatSet(event.chat_id, NewChatPar)
#    print('\nChatSet после удаления {} : \n {} \n'.format(param,ChatParam))
    ChatParamFile=OpenChatParam('Для удаления параметра', 'w')
    for one in NewChatPar.keys():
        TextToFile=one+' '+str(NewChatPar[one])+'\n'
        ChatParamFile.write(TextToFile)
    CloseChatParam('После удаления параметра', ChatParamFile)
    ToReturn=[]
    ToReturn.append(ChatSet)
    ToReturn.append(NewChatPar)
    SendMsgToChat(event, message, vk)
    return ToReturn