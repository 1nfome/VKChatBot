from Times import SecToDate
from SendMessage import SendMsgToChat, SendStickerToChat, SendGraffityToChat
import os.path
from OpenFiles import OpenUserMessage, CloseUserMessage

def Show(UserMessages, num, Id, Name, event, vk, vk_session, session):
    num-=1
    FilePath='/app/Data/UserMessages/User_'+str(Id)+'_in chat_'+str(event.chat_id)+'.txt'
    if os.path.isfile(FilePath) and (os.stat(FilePath).st_size!=0):
        UserMessageFile=OpenUserMessage(Id, event.chat_id, 'для чтения сообщений пользователя из уже существующего файла', 'r')
        messages=int(UserMessageFile.readline().split()[1])             # messages=
        UserMessages={}
        for mess in range(messages):
            UserMessageFile.readline()                                  # **********
            UserMessages[mess]={}
            UserMessages[mess]['time']=str(UserMessageFile.readline().split()[1])
#            print('из UsersMessages.py:\nUserMessages[{}]["time"]={}\n'.format(mess, UserMessages[mess]['time']))

            UserMessages[mess]['text']=str(' '.join(UserMessageFile.readline().split()[1:]))
#            print('из UsersMessages.py:\nUserMessages[{}]["text"]={}\n'.format(mess, UserMessages[mess]['text']))

            UserMessages[mess]['attachment']=int(UserMessageFile.readline().split()[1])
#            print('из UsersMessages.py:\nUserMessages[{}]["attachment"]={}\n'.format(mess, UserMessages[mess]['attachment']))

            if UserMessages[mess]['attachment']>0:
                tempatt=UserMessages[mess]['attachment']
                UserMessages[mess]['attachment']={}
                for att in range(tempatt):
                    tempadress=UserMessageFile.readline().split()
#                    print('из UsersMessages.py:\ntempadress={}\n'.format(tempadress))
                    UserMessages[mess]['attachment'][tempadress[0]]=tempadress[1]
#                    print('из UsersMessages.py:\nUserMessages[{}]["attachment"][{}]={}\n'.format(mess,tempadress[0],tempadress[1]))
        CloseUserMessage('после чтения сообщений пользователя из уже существующего файла', UserMessageFile)


        if len(UserMessages.keys())-num>0:
            if UserMessages[num]['text']!='/NONE/':
                TextToMsg=SecToDate(float(UserMessages[num]['time']))+' по МСК '+Name+' сказал:\n'+'"'+UserMessages[num]['text']+'"'
            elif UserMessages[num]['text']=='/NONE/' and UserMessages[num]['attachment']!=0:
                TextToMsg=SecToDate(float(UserMessages[num]['time']))+' по МСК '+Name+' отправил:'
            elif UserMessages[num]['text']=='/NONE/' and UserMessages[num]['attachment']==0:
                TextToMsg=SecToDate(float(UserMessages[num]['time']))+' по МСК '+Name+' отправил пустое сообщение'
            check='x'
            if UserMessages[num]['attachment']!=0:
                for elem in UserMessages[num]['attachment'].keys():
                    if elem=='graffiti' or elem=='sticker':
                        check=elem
                        break
                if check=='x':
                    attach={}
                    for elem in UserMessages[num]['attachment'].keys():
                        attach[elem]=UserMessages[num]['attachment'][elem]
                    SendMsgToChat(event, TextToMsg, vk, attach, vk_session, session, Name)
                else:
                    SendMsgToChat(event, TextToMsg, vk)
                    if check=='graffiti':
                        SendGraffityToChat(event, UserMessages[num]['attachment']['graffiti'], session, vk_session, vk)
                    elif check=='sticker':
                        SendStickerToChat(event, UserMessages[num]['attachment']['sticker'], vk)
            else:
                SendMsgToChat(event, TextToMsg, vk)
        else:
            TextToMsg='К сожалению в моей базе только '+str(len(UserMessages.keys()))+' сбщ. этого человека'
            SendMsgToChat(event, TextToMsg, vk)
    else:
        TextToMsg='Этот человек еще ничего не писал в чат'
        SendMsgToChat(event, TextToMsg, vk)