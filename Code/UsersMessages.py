import os.path
from time import time
from OpenFiles import OpenUserMessage, CloseUserMessage, OpenSwearList, CloseSwearList
from SendMessage import SendMsgToChat
from random import choice

def ReadAndAddMessageToFile(event, UserMessages, msg, ChatSet, session, vk_session):
    global PreviousTime, NowTime
    SpamUnDetected=True
    FilePath='/app/Data/UserMessages/User_'+str(event.obj.from_id)+'_in chat_'+str(event.chat_id)+'.txt'
    if os.path.isfile(FilePath) and (os.stat(FilePath).st_size!=0):
        UserMessageFile=OpenUserMessage(event.obj.from_id, event.chat_id, 'для чтения сообщений пользователя из уже существующего файла', 'r')
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

#        print('UsersMessages numbers: {}\n'.format(UserMessages))

        TempMessage={}
        if len(UserMessages.keys())>149:
            UserMessages.pop(149)
        TextToFile='messages= '+str(len(UserMessages.keys())+1)+'\n'
#        UserMessageFile.write(TextToFile)
        TextToFile=TextToFile+'******************************\n'
#        UserMessageFile.write('******************************\n')
        TempMessage['time']=str(time())
        TextToFile=TextToFile+'time: '+str(time())+'\n'
#        TextToFile='time: '+str(time())+'\n'
#        UserMessageFile.write(TextToFile)
        if msg!='':
            if len(msg)>ChatSet['parametrs']['max_message_len']:
                TempMessage['text']='"Слишком большое, похожее на спам сообщение"'
                TextToFile=TextToFile+'text: "Слишком большое, похожее на спам сообщение"\n'
#                TextToFile='text: "Слишком большое, похожее на спам сообщение"\n'
#                UserMessageFile.write(TextToFile)
            else:
                msg=msg.replace('\n','/n')
                TempMessage['text']=msg
                TextToFile=TextToFile+'text: '+msg+'\n'
#                TextToFile='text: '+msg+'\n'
#                UserMessageFile.write(TextToFile)
        else:
            TempMessage['text']='/NONE/'
            TextToFile=TextToFile+'text: /NONE/\n'
#            TextToFile='text: /NONE/\n'
#            UserMessageFile.write(TextToFile)
#        print('\nTextToFile0: \n', TextToFile,'\n')
        if str(event.object.attachments)!='[]':
            TempMessage['attachments']={}
            TextToFile=TextToFile+'attachments: '+str(len(event.object.attachments))+'\n'
#            TextToFile='attachments: '+str(len(event.object.attachments))+'\n'
#            UserMessageFile.write(TextToFile)
            for elem in event.object.attachments:
                if elem['type']=='photo':
                    maxwidth=0
                    maxheight=0
                    for slice in elem['photo']['sizes']:
                        if slice['width']>=maxwidth and slice['height']>=maxheight:
                            maxwidth=slice['width']
                            maxheight=slice['height']
                            url=slice['url']
                    TempMessage['attachments'][str(elem['type'])]=str(url)
                    TextToFile=TextToFile+str(elem['type'])+' '+str(url)+'\n'
#                    TextToFile=str(elem['type'])+' '+str(url)+'\n'
#                    UserMessageFile.write(TextToFile)
                elif elem['type']=='video':
#                    TextToFile=str(elem['type'])+' '+str(elem['type'])+str(elem[elem['type']]['owner_id'])+'_'+str(elem[elem['type']]['id'])+'\n'
#                    UserMessageFile.write(TextToFile)
                    TempMessage['attachments'][str(elem['type'])]=str(elem['type'])+str(elem[elem['type']]['owner_id'])+'_'+str(elem[elem['type']]['id'])
                    TextToFile=TextToFile+str(elem['type'])+' '+str(elem['type'])+str(elem[elem['type']]['owner_id'])+'_'+str(elem[elem['type']]['id'])+'\n'
                elif elem['type']=='audio':
#                    TextToFile=str(elem['type'])+' '+str(elem['type'])+str(elem[elem['type']]['owner_id'])+'_'+str(elem[elem['type']]['id'])+'\n'
#                    UserMessageFile.write(TextToFile)
                    TempMessage['attachments'][str(elem['type'])]=str(elem['type'])+str(elem[elem['type']]['owner_id'])+'_'+str(elem[elem['type']]['id'])
                    TextToFile=TextToFile+str(elem['type'])+' '+str(elem['type'])+str(elem[elem['type']]['owner_id'])+'_'+str(elem[elem['type']]['id'])+'\n'
                elif elem['type']=='doc':
#                    TextToFile=str(elem[elem['type']]['ext'])+' '+str(elem[elem['type']]['url'])+'\n'
#                    UserMessageFile.write(TextToFile)
                    TempMessage['attachments'][str(elem[elem['type']]['ext'])]=str(elem[elem['type']]['url'])
                    TextToFile=TextToFile+str(elem[elem['type']]['ext'])+' '+str(elem[elem['type']]['url'])+'\n'
                elif elem['type']=='wall':
#                    TextToFile=str(elem['type'])+' '+str(elem['type'])+str(elem[elem['type']]['from_id'])+'_'+str(elem[elem['type']]['id'])+'\n'
#                    UserMessageFile.write(TextToFile)
                    TempMessage['attachments'][str(elem['type'])]=str(elem['type'])+str(elem[elem['type']]['from_id'])+'_'+str(elem[elem['type']]['id'])
                    TextToFile=TextToFile+str(elem['type'])+' '+str(elem['type'])+str(elem[elem['type']]['from_id'])+'_'+str(elem[elem['type']]['id'])+'\n'
                elif elem['type']=='sticker':
#                    TextToFile=str(elem['type'])+' '+str(elem[elem['type']]['sticker_id'])+'\n'
#                    UserMessageFile.write(TextToFile)
                    TempMessage['attachments'][str(elem['type'])]=str(elem[elem['type']]['sticker_id'])
                    TextToFile=TextToFile+str(elem['type'])+' '+str(elem[elem['type']]['sticker_id'])+'\n'
                elif elem['type']=='graffiti':
#                    TextToFile=str(elem['type'])+' '+str(elem[elem['type']]['url'])+'\n'
#                    UserMessageFile.write(TextToFile)
                    TempMessage['attachments'][str(elem['type'])]=str(elem[elem['type']]['owner_id'])+'_'+str(elem[elem['type']]['id'])+'_'+str(elem[elem['type']]['access_key'])
                    TextToFile=TextToFile+str(elem['type'])+' '+str(elem[elem['type']]['owner_id'])+'_'+str(elem[elem['type']]['id'])+'_'+str(elem[elem['type']]['access_key'])+'\n'
                elif elem['type']=='audio_message':
#                    TextToFile=str(elem['type'])+' '+str(elem[elem['type']]['link_mp3'])+'\n'
#                    UserMessageFile.write(TextToFile)
                    TempMessage['attachments'][str(elem['type'])]=str(elem[elem['type']]['link_mp3'])
                    TextToFile=TextToFile+str(elem['type'])+' '+str(elem[elem['type']]['link_mp3'])+'\n'
                elif elem['type']=='poll':
#                    TextToFile=str(elem['type'])+' '+str(elem['type'])+str(elem[elem['type']]['owner_id'])+'_'+str(elem[elem['type']]['id'])+'\n'
#                    UserMessageFile.write(TextToFile)
                    TempMessage['attachments'][str(elem['type'])]=str(elem['type'])+str(elem[elem['type']]['owner_id'])+'_'+str(elem[elem['type']]['id'])
                    TextToFile=TextToFile+str(elem['type'])+' '+str(elem['type'])+str(elem[elem['type']]['owner_id'])+'_'+str(elem[elem['type']]['id'])+'\n'
                elif elem['type']=='link':
                    TempMessage['attachments'][str(elem['type'])]=str(elem[elem['type']]['url'])
                    TextToFile=TextToFile+str(elem['type'])+' '+str(elem[elem['type']]['url'])+'\n'
        else:
#            TextToFile='attachments: 0\n'
#            UserMessageFile.write(TextToFile)
            TempMessage['attachments']=0
            TextToFile=TextToFile+'attachments: 0\n'
        UserMessageFile=OpenUserMessage(event.obj.from_id, event.chat_id, 'для записи нового сообщения пользователя в уже существующий файл', 'w')
#        print('UsersMessages.py\ntext:\n{}\n\nTempMess:\n{}\n'.format(TextToFile, TempMessage))

        PreviousTime=0
        NowTime=0
        for elem in range(len(list(UserMessages[0]['time']))):
            if list(UserMessages[0]['time'])[elem]=='.':
                PreviousTime=int(''.join(list(UserMessages[0]['time'])[0:elem]))
                micro=int(''.join(list(UserMessages[0]['time'])[(elem+1):]))
                PreviousTime=PreviousTime+(micro/10**len(str(micro)))
                break
        for elem in range(len(list(TempMessage['time']))):
            if list(TempMessage['time'])[elem]=='.':
                NowTime=int(''.join(list(TempMessage['time'])[0:elem]))
                micro=int(''.join(list(TempMessage['time'])[(elem+1):]))
                NowTime=NowTime+(micro/10**len(str(micro)))
                break


#        print('\nUsersMessages prev: \n', UserMessages,'\n')
#        print('\nTempMessage итог: \n', TempMessage,'\n')
#        print('\nNowTime-PreviousTime итог: \n', NowTime-PreviousTime,'\n')
        if TempMessage['attachments']!=0 and UserMessages[0]['attachment']!=0 and (TempMessage['attachments']==UserMessages[0]['attachment']):
            SpamUnDetected=False
            TextToFile='messages= '+str(len(UserMessages.keys()))+'\n'
#            print('\nTextToFile итог1: \n', TextToFile,'\n')
            UserMessageFile.write(TextToFile)
        elif (UserMessages[0]['text']==TempMessage['text'] and (UserMessages[0]['text']!='/NONE/' and TempMessage['text']!='/NONE/')) or (NowTime-PreviousTime)<1.0:
            TextToFile='messages= '+str(len(UserMessages.keys()))+'\n'
 #           print('\nTextToFile итог2: \n', TextToFile,'\n')
            UserMessageFile.write(TextToFile)
            SpamUnDetected=False
        else:
#            print('\nTextToFile итог3: \n', TextToFile,'\n')
            UserMessageFile.write(TextToFile)

        for mess in UserMessages.keys():
            UserMessageFile.write('******************************\n')
            TextToFile='time: '+str(UserMessages[mess]['time'])+'\n'
            UserMessageFile.write(TextToFile)
            TextToFile='text: '+str(UserMessages[mess]['text'])+'\n'
            UserMessageFile.write(TextToFile)
            if UserMessages[mess]['attachment']==0:
                TextToFile='attachment: 0\n'
                UserMessageFile.write(TextToFile)
            else:
                TextToFile='attachment: '+str(len(UserMessages[mess]['attachment']))+'\n'
                UserMessageFile.write(TextToFile)
                for elem in UserMessages[mess]['attachment'].keys():
                    TextToFile=str(elem)+' '+str(UserMessages[mess]['attachment'][elem])+' \n'
                    UserMessageFile.write(TextToFile)
        CloseUserMessage('после записи всех сообщений пользователя в уже существующий файл', UserMessageFile)
        UserMessageFile=OpenUserMessage(event.obj.from_id, event.chat_id, 'для чтения сообщений пользователя из уже существующего файла', 'r')
        messages=int(UserMessageFile.readline().split()[1])             # messages=
        UserMessages={}
        for mess in range(messages):
            UserMessageFile.readline()                                  # **********
            UserMessages[mess]={}
            UserMessages[mess]['time']=str(UserMessageFile.readline().split()[1])
            UserMessages[mess]['text']=str(' '.join(UserMessageFile.readline().split()[1:]))
            UserMessages[mess]['attachment']=int(UserMessageFile.readline().split()[1])
            if UserMessages[mess]['attachment']>0:
                tempatt=UserMessages[mess]['attachment']
                UserMessages[mess]['attachment']={}
                for att in range(tempatt):
                    tempadress=UserMessageFile.readline().split()
                    UserMessages[mess]['attachment'][tempadress[0]]=tempadress[1]
        CloseUserMessage('после чтения сообщений пользователя из уже существующего файла', UserMessageFile)
    else:
        UserMessageFile=OpenUserMessage(event.obj.from_id, event.chat_id, 'для записи нового сообщения пользователя в новый файл', 'w')
        TextToFile='messages= 1\n'
        UserMessageFile.write(TextToFile)
        UserMessageFile.write('******************************\n')
        TextToFile='time: '+str(time())+'\n'
        UserMessageFile.write(TextToFile)
        if msg!='':
            if len(msg)>=ChatSet['parametrs']['max_message_len']:
                TextToFile='text: "Слишком большое, похожее на спам сообщение"\n'
                UserMessageFile.write(TextToFile)
            else:
                msg=msg.replace('\n','/n')
                TextToFile='text: '+msg+'\n'
                UserMessageFile.write(TextToFile)
        else:
            TextToFile='text: /NONE/\n'
            UserMessageFile.write(TextToFile)
        if str(event.object.attachments)!='[]':
            TextToFile='attachments: '+str(len(event.object.attachments))+'\n'
            UserMessageFile.write(TextToFile)
            for elem in event.object.attachments:
                if elem['type']=='photo':
                    maxwidth=0
                    maxheight=0
                    for slice in elem['photo']['sizes']:
                        if slice['width']>=maxwidth and slice['height']>=maxheight:
                            maxwidth=slice['width']
                            maxheight=slice['height']
                            url=slice['url']
                    TextToFile=str(elem['type'])+' '+str(url)+'\n'
                    UserMessageFile.write(TextToFile)
                elif elem['type']=='video':
                    TextToFile=str(elem['type'])+' '+str(elem['type'])+str(elem[elem['type']]['owner_id'])+'_'+str(elem[elem['type']]['id'])+'\n'
                    UserMessageFile.write(TextToFile)
                elif elem['type']=='audio':
                    TextToFile=str(elem['type'])+' '+str(elem['type'])+str(elem[elem['type']]['owner_id'])+'_'+str(elem[elem['type']]['id'])+'\n'
                    UserMessageFile.write(TextToFile)
                elif elem['type']=='doc':
                    TextToFile=str(elem[elem['type']]['ext'])+' '+str(elem[elem['type']]['url'])+'\n'
                    UserMessageFile.write(TextToFile)
                elif elem['type']=='wall':
                    TextToFile=str(elem['type'])+' '+str(elem['type'])+str(elem[elem['type']]['from_id'])+'_'+str(elem[elem['type']]['id'])+'\n'
                    UserMessageFile.write(TextToFile)
                elif elem['type']=='sticker':
                    TextToFile=str(elem['type'])+' '+str(elem[elem['type']]['sticker_id'])+'\n'
                    UserMessageFile.write(TextToFile)
                elif elem['type']=='graffiti':
                    TextToFile=str(elem['type'])+' '+str(elem[elem['type']]['owner_id'])+'_'+str(elem[elem['type']]['id'])+'_'+str(elem[elem['type']]['access_key'])+'\n'
                    UserMessageFile.write(TextToFile)
                elif elem['type']=='audio_message':
                    TextToFile=str(elem['type'])+' '+str(elem[elem['type']]['link_mp3'])+'\n'
                    UserMessageFile.write(TextToFile)
                elif elem['type']=='poll':
                    TextToFile=str(elem['type'])+' '+str(elem['type'])+str(elem[elem['type']]['owner_id'])+'_'+str(elem[elem['type']]['id'])+'\n'
                    UserMessageFile.write(TextToFile)
                elif elem['type']=='link':
                    TextToFile=str(elem['type'])+' '+str(elem[elem['type']]['url'])+'\n'
                    UserMessageFile.write(TextToFile)
        else:
            TextToFile='attachments: 0\n'
            UserMessageFile.write(TextToFile)
        CloseUserMessage('после записи первого пользователя в новый файл', UserMessageFile)
        UserMessageFile=OpenUserMessage(event.obj.from_id, event.chat_id, 'для чтения сообщений пользователя из уже существующего файла', 'r')
        messages=int(UserMessageFile.readline().split()[1])             # messages=
        UserMessages={}
        for mess in range(messages):
            UserMessageFile.readline()                                  # **********
            UserMessages[mess]={}
            UserMessages[mess]['time']=str(UserMessageFile.readline().split()[1])
            UserMessages[mess]['text']=str(' '.join(UserMessageFile.readline().split()[1:]))
            UserMessages[mess]['attachment']=int(UserMessageFile.readline().split()[1])
            if UserMessages[mess]['attachment']>0:
                tempatt=UserMessages[mess]['attachment']
                UserMessages[mess]['attachment']={}
                for att in range(tempatt):
                    tempadress=UserMessageFile.readline().split()
                    UserMessages[mess]['attachment'][tempadress[0]]=tempadress[1]
        CloseUserMessage('после чтения сообщений пользователя из уже существующего файла', UserMessageFile)
#    print('usermessages\nSpamUnDetected: {}\n'.format(SpamUnDetected))
    return UserMessages, SpamUnDetected







def counter(event, UserStats, UserMessages, vk, Check, msg, BotName, ChatSet):
    global PreviousTime, NowTime
#    print('counter\nPreviousTime: {}\nNowTime: {}\n'.format(PreviousTime,NowTime))
    SpamReact={3:'Ты же вкурсе, что спам - это плохо?',5:'Че спамишь то? Делать нефиг?',6:'Еще раз: хватит спамить!',7:'Я за спам, если что баню))',8:'Ты в бан хочешь?',9:'Ну я тебе предупреждал...'}
    if Check==True and UserStats[event.obj.from_id]['BlackList']==0 and (not msg.startswith(BotName)) and (not msg.startswith('Бот')):
        if UserStats[event.obj.from_id]['SpamTotal']!=0:
            UserStats[event.obj.from_id]['SpamTotal']-=1
        SwearList=OpenSwearList('для проверки наличия мата в сообщении')
        Swear=SwearList.read().split()
        CloseSwearList('после считывания списка матов',SwearList)
        SC=False
        for word in UserMessages[0]['text'].lower().split():
            if word in Swear:
                UserStats[event.obj.from_id]['SwearTotal']+=1
#                text='Я считаю, что "'+word+'" является матом!!!!'
#                SendMsgToChat(event, text, vk)
                if ChatSet['parametrs']['swear_answer']=='True':
                    SC=True
        if SC==True:
            text=choice(['Ты же вкурсе, что маты - это плохо?','Давайте общаться без мата!','Не матерись!','Фу, как не культурно!'])
            SendMsgToChat(event, text, vk)
        CloseSwearList('После проверки на наличие матов в сообщении', SwearList)
        UserStats[event.obj.from_id]['MessageTotal']+=1
        UserStats[event.obj.from_id]['WordsTotal']+=len(msg.split())
        UserStats[event.obj.from_id]['LetterTotal']+=len(list(msg))
        UserStats[event.obj.from_id]['LastActiveTime']=time()
        Top={}
        for man in UserStats.keys():
            UserStats[man]['Status']=''
        ############################################################ ТОП ПО МАТАМ
        i=0
        for human in UserStats.keys():
            Top[i]=[human,UserStats[human]['SwearTotal']]
            i+=1
        i=0
        while True:
            if int(Top[i][1])<int(Top[i+1][1]):
                temp=Top[i]
                Top[i]=Top[i+1]
                Top[i+1]=temp
                i=0
            else:
                i+=1
            if i==len(Top)-1:
                break
#        print('Top: ',Top,'\n')
        if Top[0][1]!=0:
            UserStats[Top[0][0]]['Status']+='🤬'
        if Top[len(Top)-1][1]==0 and Top[len(Top)-2][1]!=0:
            UserStats[Top[len(Top)-1][0]]['Status']+='🧐'
        ############################################################# ТОП ПО ГРАФФИТИ
        Top={}
        i=0
        for human in UserStats.keys():
            Top[i]=[human,UserStats[human]['Graffity']]
            i+=1
        i=0
        while True:
            if int(Top[i][1])<int(Top[i+1][1]):
                temp=Top[i]
                Top[i]=Top[i+1]
                Top[i+1]=temp
                i=0
            else:
                i+=1
            if i==len(Top)-1:
                break
#        print('Top: ',Top,'\n')
        if Top[0][1]!=0:
            UserStats[Top[0][0]]['Status']+='🎨'

        ############################################################# ТОП ПО ГОЛОСОВЫМ
        Top={}
        i=0
        for human in UserStats.keys():
            Top[i]=[human,UserStats[human]['Speech']]
            i+=1
        i=0
        while True:
            if int(Top[i][1])<int(Top[i+1][1]):
                temp=Top[i]
                Top[i]=Top[i+1]
                Top[i+1]=temp
                i=0
            else:
                i+=1
            if i==len(Top)-1:
                break
#        print('Top: ',Top,'\n')
        if Top[0][1]!=0:
            UserStats[Top[0][0]]['Status']+='📣'
        ############################################################ Привилегии
        for man in UserStats.keys():
            if UserStats[man]['Privilege']==1:
                UserStats[man]['Status']+='👁'
            elif UserStats[man]['Privilege']==2:
                UserStats[man]['Status']+='💼'
            elif UserStats[man]['Privilege']==3:
                UserStats[man]['Status']+='👽'
        ####################################################################
#        print('counter status: {}\n'.format(UserStats[event.obj.from_id]['Status']))
        for man in UserStats.keys():
            if UserStats[man]['Status']=='':
                UserStats[man]['Status']='None'
        TotalMessage=0
        LettersTotal=0
#        print('counter проверка 1\n')
        for human in UserStats.keys():
#            print('UserStats[{}]["MessageTotal"]={}'.format(human,UserStats[human]['MessageTotal']))
            TotalMessage=TotalMessage+int(UserStats[human]['MessageTotal'])
            LettersTotal=LettersTotal+int(UserStats[human]['LetterTotal'])
        if TotalMessage>=100:
            Middle=LettersTotal/TotalMessage
            if len(list(msg))>=Middle and (NowTime-PreviousTime)<25.0:
                UserStats[event.obj.from_id]['TypingTime']=NowTime-PreviousTime
        if str(event.object.attachments)!='[]':
            for elem in event.object.attachments:
                if elem['type']=='photo':
                    UserStats[event.obj.from_id]['Photos']+=1
                elif elem['type']=='video':
                    UserStats[event.obj.from_id]['Videos']+=1
                elif elem['type']=='sticker':
                    UserStats[event.obj.from_id]['StickersTotal']+=1
                elif elem['type']=='audio':
                    UserStats[event.obj.from_id]['Audios']+=1
                elif elem['type']=='graffiti':
                    UserStats[event.obj.from_id]['Graffity']+=1
                elif elem['type']=='audio_message':
                    UserStats[event.obj.from_id]['Speech']+=1
                elif elem['type']=='poll':
                    UserStats[event.obj.from_id]['Poll']+=1
                elif elem['type']=='doc':
                    if elem[elem['type']]['ext']=='gif':
                        UserStats[event.obj.from_id]['Gifs']+=1
                    elif elem[elem['type']]['ext']=='png' or elem[elem['type']]['ext']=='jpg' or elem[elem['type']]['ext']=='bmp':
                        UserStats[event.obj.from_id]['Photos']+=1
    if str(type(UserStats[event.obj.from_id]['Privilege']))=="<class 'int'>" and 4>UserStats[event.obj.from_id]['Privilege']>-1 and UserStats[event.obj.from_id]['BlackList']==0 and Check==False and UserStats[event.obj.from_id]['Privilege']<1:
        if UserStats[event.obj.from_id]['SpamTotal']==3 or UserStats[event.obj.from_id]['SpamTotal']>=5:
            SendMsgToChat(event, SpamReact[UserStats[event.obj.from_id]['SpamTotal']], vk)
        UserStats[event.obj.from_id]['SpamTotal']+=1
#        print('Counter Spam: ', UserStats[event.obj.from_id]['SpamTotal'],'\n')
        if UserStats[event.obj.from_id]['SpamTotal']==10:
            UserStats[event.obj.from_id]['BlackList']=1
            UserStats[event.obj.from_id]['SpamTotal']=0
    elif str(type(UserStats[event.obj.from_id]['Privilege']))=="<class 'str'>" and ChatSet['classes'][UserStats[event.obj.from_id]['Privilege']]['Can_spam']==False and Check==False and UserStats[event.obj.from_id]['BlackList']==0:
        if UserStats[event.obj.from_id]['SpamTotal']==3 or UserStats[event.obj.from_id]['SpamTotal']>=5:
            SendMsgToChat(event, SpamReact[UserStats[event.obj.from_id]['SpamTotal']], vk)
        UserStats[event.obj.from_id]['SpamTotal']+=1
#        print('Counter Spam: ', UserStats[event.obj.from_id]['SpamTotal'],'\n')
        if UserStats[event.obj.from_id]['SpamTotal']==10:
            UserStats[event.obj.from_id]['BlackList']=1
            UserStats[event.obj.from_id]['SpamTotal']=0

#    print('counter проверка 2\n')
    return UserStats


















