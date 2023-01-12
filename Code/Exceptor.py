from time import time
import traceback
from Times import SecToDate
from vk_api.utils import get_random_id
from SendMessage import SendMsgToChat

def Except(trouble, event, vk):
#    print('\n\nTROUBLE:\n\n'+trouble)
    if "[917] You don't have access to this chat" in str(trouble):
#        print("проверка Exceptor Except You don't have access to this chat")
        try:
            if event.obj.action['type']=='chat_invite_user' and event.obj.action['member_id']==-185153508:
                SendMsgToChat(event, 'Сорри, но без прав админа я совершенно беспомощен(((', vk)
        except:
            pass
    try:
        eventTime=event.obj.date
    except:
        eventTime=None
    if eventTime!=None and (time()-event.obj.date)<5 and (not ("[917] You don't have access to this chat" in str(trouble))):
        Message=str(event)+'\n\n\n@id'+str(event.obj.from_id)+'\n'+SecToDate(event.obj.date, 60*60*6)+'\nНаписал:'+event.obj.text+'\nВ чате № '+str(event.chat_id)+'\n\n\n'+traceback.format_exc()
        ChatId=449891250
        try:
            vk.messages.send(
                    peer_id=ChatId,
                    message=Message,
                    random_id=get_random_id()
                )
        except:
            if 'vk_api.exceptions.ApiError: [914] Message is too long' in traceback.format_exc():
                message='-------------------------------------------------------------------------------------------------------------------'+'\nСлишком длинное сообщение разбито на несколько сообщений:'
                vk.messages.send(
                    peer_id=ChatId,
                    message=message,
                    random_id=get_random_id()
                )
                for i in range(int(len(Message)/4000)):
                    message=str(i)+' из '+str(int(len(Message)/4000))+'\n\n'+Message[i*4000:(i+1)*4000]
                    vk.messages.send(
                        peer_id=ChatId,
                        message=message,
                        random_id=get_random_id()
                    )
            vk.messages.send(
                    peer_id=ChatId,
                    message='-------------------------------------------------------------------------------------------------------------------',
                    random_id=get_random_id()
                )
    elif eventTime==None or (time()-event.obj.date)>5 and (not ("[917] You don't have access to this chat" in str(trouble))):
        Message=SecToDate(event.obj.date, 60*60*6)+'\n\n\n'+traceback.format_exc()
        ChatId=449891250
        try:
            vk.messages.send(
                    peer_id=ChatId,
                    message=message,
                    random_id=get_random_id()
                )
        except:
            if 'vk_api.exceptions.ApiError: [914] Message is too long' in traceback.format_exc():
                message='-------------------------------------------------------------------------------------------------------------------\n'+'Слишком длинное сообщение разбито на несколько сообщений:'
                vk.messages.send(
                    peer_id=ChatId,
                    message=message,
                    random_id=get_random_id()
                )
                for i in range(int(len(Message)/4000)):
                    message=str(i)+' из '+str(int(len(Message)/4000))+'\n\n'+Message[i*4000:(i+1)*4000]
                    vk.messages.send(
                        peer_id=ChatId,
                        message=message,
                        random_id=get_random_id()
                    )
                vk.messages.send(
                        peer_id=ChatId,
                        message='-------------------------------------------------------------------------------------------------------------------',
                        random_id=get_random_id()
                    )
