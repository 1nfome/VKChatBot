from random import choice
from SendMessage import SendMsgToChat
from AddReadWriteUsersStats import ReadAllStats, WriteAllStats
from Exceptor import Except
import traceback
from GlobalNames import ReadGN, WriteGN

def SetBotName(msg, event, vk, UserStats, IdBase, parametrs, UserNames, AllChats=False):
    try:
        text=msg[msg.lower().find('sbn')+4:]
        print('SetBotName text: {}\n'.format(text))
        if text=='':
            if UserNames[event.obj.from_id]['sex']==1:
                message=choice(['{} ,умная самая, пустое имя мне ставить?\nИли всё как раз наоборот?!)','{} ,за что такое страшное ты меня без имени решила оставить?','{} , нельзя ставить мне пустое имя']).format(UserStats[event.obj.from_id]['UserName'])
                SendMsgToChat(event, message, vk)
            elif UserNames[event.obj.from_id]['sex']==2:
                message=choice(['{} ,умный самый, пустое имя мне ставить?\nИли всё как раз наоборот?!)','{} ,за что такое страшное ты меня без имени решил оставить?','{} ,нельзя ставить мне пустое имя']).format(UserStats[event.obj.from_id]['UserName'])
                SendMsgToChat(event, message, vk)
            elif UserNames[event.obj.from_id]['sex']==0:
                message=choice(['{} ,умное самое, пустое имя мне ставить?\nИли всё как раз наоборот?!)','{} ,за что такое страшное ты меня без имени решило оставить?','{} ,нельзя ставить мне пустое имя']).format(UserStats[event.obj.from_id]['UserName'])
                SendMsgToChat(event, message, vk)
            text=UserStats[event.obj.from_id]['BotName']
        elif len(text)<=30:
            UserStats[event.obj.from_id]['BotName']=text
            if AllChats:
                print('SetBotName зашло в if\n')
                for chat in IdBase.keys():
                    try:
                        print('chat ', chat,'\n\n')
                        UserStats={}
                        UserStats=ReadAllStats(parametrs, UserStats, chat)
                        print('UserStats до замены имени бота\n', UserStats,'\n\n')
                        try:
                            UserStats[event.obj.from_id]['BotName']=text
                        except Exception as e:
                            print('Trouble with SetBotName for All Chats. Скорее всего нет такого человека в чате: \n{}\n'.format(e))
                        print('UserStats после замены имени бота\n', UserStats,'\n\n')
                        WriteAllStats(parametrs, UserStats, chat)
                        print('Записали UserStats в файл\n\n')
                    except Exception as e:
                        print('G Trouble with SetBotName for All Chats: \n{}\n'.format(e))
                GN=ReadGN()
                try:
                    GN[event.obj.from_id]['BotName']=text
                except:
                    GN[event.obj.from_id]={}
                    GN[event.obj.from_id]['BotName']=text
                    GN[event.obj.from_id]['UserName']=UserStats[event.obj.from_id]['UserName']
                WriteGN(GN)
                UserStats={}
                UserStats=ReadAllStats(parametrs, UserStats, event.chat_id)
                reactions=['{}? Ну бывало и хуже','{}? Ну могло быть и хуже', 'Сам(а) ты {}!', '{}? Как мило', 'Серьёзно? {}?', '{}? Как оригинально...', '{}? Смешно-смешно...(нет)']
                message=choice(reactions).format(UserStats[event.obj.from_id]['BotName'])
                SendMsgToChat(event, message, vk)
                return UserStats
            else:
                print('SetBotName меняет только для данного чата\n')
                UserStats[event.obj.from_id]['BotName']=text
                print('SetBotName text: {}\n'.format(UserStats[event.obj.from_id]['BotName']))
                reactions=['{}? Ну бывало и хуже','{}? Ну могло быть и хуже', 'Сам(а) ты {}!', '{}? Как мило', 'Серьёзно? {}?', '{}? Как оригинально...', '{}? Смешно-смешно...(нет)']
                message=choice(reactions).format(UserStats[event.obj.from_id]['BotName'])
                SendMsgToChat(event, message, vk)
                return UserStats
        else:
            message='{} ,максимальная длина имени бота - 30 символов'.format(UserStats[event.obj.from_id]['UserName'])
            SendMsgToChat(event, message, vk)
    except:
        message='Произошла ошибка при смене имени бота'
        SendMsgToChat(event, message, vk)
        Except(traceback.format_exc(), event, vk)







def SetUserName(msg, event, vk, UserStats, UserNames, IdBase, parametrs, AllChats=False):
    try:
        text=msg[msg.lower().find('smn')+4:]
        if text=='':
            if UserNames[event.obj.from_id]['sex']==1:
                message=choice(['{}, умная самая, пустое имя себе ставить?\nИли всё как раз наоборот?!)','{}, нельзя ставить себе пустое имя']).format(UserStats[event.obj.from_id]['UserName'])
                SendMsgToChat(event, message, vk)
            elif UserNames[event.obj.from_id]['sex']==2:
                message=choice(['{}, умный самый, пустое имя себе ставить?\nИли всё как раз наоборот?!)','{}, нельзя ставить себе пустое имя']).format(UserStats[event.obj.from_id]['UserName'])
                SendMsgToChat(event, message, vk)
            elif UserNames[event.obj.from_id]['sex']==0:
                message=choice(['{}, умное самое, пустое имя себе ставить?\nИли всё как раз наоборот?!)','{}, нельзя ставить себе пустое имя']).format(UserStats[event.obj.from_id]['UserName'])
                SendMsgToChat(event, message, vk)
            text=UserStats[event.obj.from_id]['BotName']
        elif len(text)<=30 and AllChats==False:
            FakeCheck=False
            for man in UserStats.keys():
                print('SetName SetUserName FakeCheck UserStats man: '+UserStats[man]['Name']+'\n'+'ID: '+str(man))
                if text==UserStats[man]['Name'] and text!=UserNames[event.obj.from_id]['nom']:
                    FakeCheck=man
                    print('SetName SetUserName FakeCheck UserStats man: СОВПАЛ!!')
                    break
            if FakeCheck==False:
                NameSpace=2
                fakenamespacecheck=None
                for man in UserStats.keys():
                    if UserStats[man]['UserName']==text:
                        fakenamespacecheck=False
                        while fakenamespacecheck==False:
                            fakenamespacecheck=True
                            for man in UserStats.keys():
                                if text+' №'+str(NameSpace) == UserStats[man]['UserName'] and NameSpace<500:
                                    NameSpace+=1
                                    fakenamespacecheck=False
                                elif text+' №'+str(NameSpace) == UserStats[man]['UserName'] and NameSpace>=500:
                                    fakenamespacecheck=-1
                                    break
                        break

                if fakenamespacecheck==True:
                    message='Серьёзно?!'
                    SendMsgToChat(event, message, vk)
                    message='Окееей...'
                    SendMsgToChat(event, message, vk)
                    UserStats[event.obj.from_id]['UserName']=text+' №'+str(NameSpace)
                    message='Будешь: '+text+' №'+str(NameSpace)
                    SendMsgToChat(event, message, vk)
                    return UserStats
                elif fakenamespacecheck==-1:
                    message='Слишком много повторяющихся имён. Прояви фантазию)'
                    SendMsgToChat(event, message, vk)
                elif fakenamespacecheck==None:
                    UserStats[event.obj.from_id]['UserName']=text
                    reactions=['{}? Самокритично','{}? А ведь похоже на правду', '{}? Так и запишем', 'Ты серьёзно? {}?', '{}? Почему бы и нет...', '{}? Как оригинально...', '{}? Смешно-смешно...(нет)']
                    message=choice(reactions).format(UserStats[event.obj.from_id]['UserName'])
                    SendMsgToChat(event, message, vk)
                    return UserStats
            else:
                print('SetName SetUserName FakeCheck UserStats man ELSE: '+UserStats[man]['Name']+'\n'+'ID: '+str(man)+"\nUserNames[man]['gen']: "+UserNames[man]['gen'])
                text='Фейк '+UserNames[man]['gen']
                NameSpace=2
                fakenamespacecheck=None
                for mans in UserStats.keys():
                    if text in UserStats[mans]['UserName']:
                        fakenamespacecheck=False
                        while fakenamespacecheck==False:
                            fakenamespacecheck=True
                            for man in UserStats.keys():
                                if text+' №'+str(NameSpace) == UserStats[man]['UserName'] and NameSpace<500:
                                    NameSpace+=1
                                    fakenamespacecheck=False
                                elif text+' №'+str(NameSpace) == UserStats[man]['UserName'] and NameSpace>=500:
                                    fakenamespacecheck=-1
                                    break
                        break

                if fakenamespacecheck==None:
                    message='Будешь: '+text
                    SendMsgToChat(event, message, vk)
                    UserStats[event.obj.from_id]['UserName']=text
                    return UserStats
                elif fakenamespacecheck==True:
                    message='Серьёзно?!'
                    SendMsgToChat(event, message, vk)
                    message='Окееей...'
                    SendMsgToChat(event, message, vk)
                    UserStats[event.obj.from_id]['UserName']=text+' №'+str(NameSpace)
                    message='Будешь: '+text+' №'+str(NameSpace)
                    SendMsgToChat(event, message, vk)
                    return UserStats
                elif fakenamespacecheck==-1:
                    message='Слишком много фейков. Прояви фантазию)'
                    SendMsgToChat(event, message, vk)






        elif len(text)<=30 and AllChats==True:
            Names={}
            for man in UserStats.keys():
                Names[man]=UserStats[man]['UserName']
            GN=ReadGN()
            for man in GN.keys():
                Names[man]=GN[man]['UserName']
            FakeCheck=False
            for man in UserStats.keys():
                print('SetName SetUserName FakeCheck UserStats man: '+UserStats[man]['Name']+'\n'+'ID: '+str(man))
                if text==UserStats[man]['Name'] and text!=UserNames[event.obj.from_id]['nom']:
                    FakeCheck=man
                    print('SetName SetUserName FakeCheck UserStats man: СОВПАЛ!!')
                    break
            if FakeCheck==False:
                print('SetName SetUserName FakeCheck==False Names=\n',Names)
                NameSpace=2
                fakenamespacecheck=None
                for man in Names.keys():
                    if Names[man]==text:
                        fakenamespacecheck=False
                        while fakenamespacecheck==False:
                            fakenamespacecheck=True
                            for man in Names.keys():
                                if text+' №'+str(NameSpace) == Names[man] and NameSpace<500:
                                    NameSpace+=1
                                    fakenamespacecheck=False
                                elif text+' №'+str(NameSpace) == Names[man] and NameSpace>=500:
                                    fakenamespacecheck=-1
                                    break
                        break

                if fakenamespacecheck==True:
                    message='Серьёзно?!'
                    SendMsgToChat(event, message, vk)
                    message='Окееей...'
                    SendMsgToChat(event, message, vk)
                    UserStats[event.obj.from_id]['UserName']=text+' №'+str(NameSpace)

                    for chat in IdBase.keys():
                        try:
                            print('chat ', chat,'\n\n')
                            UserStats={}
                            UserStats=ReadAllStats(parametrs, UserStats, chat)
                            print('UserStats до замены имени бота\n', UserStats,'\n\n')
                            try:
                                UserStats[event.obj.from_id]['UserName']=text
                            except Exception as e:
                                print('Trouble with SetBotName for All Chats. Скорее всего нет такого человека в чате: \n{}\n'.format(e))
                            print('UserStats после замены имени бота\n', UserStats,'\n\n')
                            WriteAllStats(parametrs, UserStats, chat)
                            print('Записали UserStats в файл\n\n')
                        except Exception as e:
                            print('G Trouble with SetBotName for All Chats: \n{}\n'.format(e))
                    UserStats={}
                    UserStats=ReadAllStats(parametrs, UserStats, event.chat_id)



                    try:
                        GN[event.obj.from_id]['UserName']=text+' №'+str(NameSpace)
                    except:
                        GN[event.obj.from_id]={}
                        GN[event.obj.from_id]['BotName']=UserStats[event.obj.from_id]['BotName']
                        GN[event.obj.from_id]['UserName']=text+' №'+str(NameSpace)
                    WriteGN(GN)
                    message='Будешь: '+text+' №'+str(NameSpace)
                    SendMsgToChat(event, message, vk)
                    return UserStats
                elif fakenamespacecheck==-1:
                    message='Слишком много повторяющихся имён. Прояви фантазию)'
                    SendMsgToChat(event, message, vk)
                elif fakenamespacecheck==None:
                    UserStats[event.obj.from_id]['UserName']=text
                    reactions=['{}? Самокритично','{}? А ведь похоже на правду', '{}? Так и запишем', 'Ты серьёзно? {}?', '{}? Почему бы и нет...', '{}? Как оригинально...', '{}? Смешно-смешно...(нет)']
                    message=choice(reactions).format(UserStats[event.obj.from_id]['UserName'])

                    for chat in IdBase.keys():
                        try:
                            print('chat ', chat,'\n\n')
                            UserStats={}
                            UserStats=ReadAllStats(parametrs, UserStats, chat)
                            print('UserStats до замены имени бота\n', UserStats,'\n\n')
                            try:
                                UserStats[event.obj.from_id]['UserName']=text
                            except Exception as e:
                                print('Trouble with SetBotName for All Chats. Скорее всего нет такого человека в чате: \n{}\n'.format(e))
                            print('UserStats после замены имени бота\n', UserStats,'\n\n')
                            WriteAllStats(parametrs, UserStats, chat)
                            print('Записали UserStats в файл\n\n')
                        except Exception as e:
                            print('G Trouble with SetBotName for All Chats: \n{}\n'.format(e))
                    UserStats={}
                    UserStats=ReadAllStats(parametrs, UserStats, event.chat_id)



                    try:
                        GN[event.obj.from_id]['UserName']=text
                    except:
                        GN[event.obj.from_id]={}
                        GN[event.obj.from_id]['BotName']=UserStats[event.obj.from_id]['BotName']
                        GN[event.obj.from_id]['UserName']=text
                    WriteGN(GN)




                    SendMsgToChat(event, message, vk)
                    return UserStats
            else:
                print('SetName SetUserName FakeCheck UserStats man ELSE: '+UserStats[man]['Name']+'\n'+'ID: '+str(man)+"\nUserNames[man]['gen']: "+UserNames[man]['gen'])
                text='Фейк '+UserNames[man]['gen']
                NameSpace=2
                fakenamespacecheck=None
                for mans in UserStats.keys():
                    if text in UserStats[mans]['UserName']:
                        fakenamespacecheck=False
                        while fakenamespacecheck==False:
                            fakenamespacecheck=True
                            for man in UserStats.keys():
                                if text+' №'+str(NameSpace) == UserStats[man]['UserName'] and NameSpace<500:
                                    NameSpace+=1
                                    fakenamespacecheck=False
                                elif text+' №'+str(NameSpace) == UserStats[man]['UserName'] and NameSpace>=500:
                                    fakenamespacecheck=-1
                                    break
                        break

                if fakenamespacecheck==None:
                    message='Будешь: '+text
                    SendMsgToChat(event, message, vk)
                    UserStats[event.obj.from_id]['UserName']=text

                    for chat in IdBase.keys():
                        try:
                            print('chat ', chat,'\n\n')
                            UserStats={}
                            UserStats=ReadAllStats(parametrs, UserStats, chat)
                            print('UserStats до замены имени бота\n', UserStats,'\n\n')
                            try:
                                UserStats[event.obj.from_id]['UserName']=text
                            except Exception as e:
                                print('Trouble with SetBotName for All Chats. Скорее всего нет такого человека в чате: \n{}\n'.format(e))
                            print('UserStats после замены имени бота\n', UserStats,'\n\n')
                            WriteAllStats(parametrs, UserStats, chat)
                            print('Записали UserStats в файл\n\n')
                        except Exception as e:
                            print('G Trouble with SetBotName for All Chats: \n{}\n'.format(e))
                    UserStats={}
                    UserStats=ReadAllStats(parametrs, UserStats, event.chat_id)



                    try:
                        GN[event.obj.from_id]['UserName']=text
                    except:
                        GN[event.obj.from_id]={}
                        GN[event.obj.from_id]['BotName']=UserStats[event.obj.from_id]['BotName']
                        GN[event.obj.from_id]['UserName']=text
                    WriteGN(GN)





                    return UserStats
                elif fakenamespacecheck==True:
                    message='Серьёзно?!'
                    SendMsgToChat(event, message, vk)
                    message='Окееей...'
                    SendMsgToChat(event, message, vk)
                    UserStats[event.obj.from_id]['UserName']=text+' №'+str(NameSpace)
                    for chat in IdBase.keys():
                        try:
                            print('chat ', chat,'\n\n')
                            UserStats={}
                            UserStats=ReadAllStats(parametrs, UserStats, chat)
                            print('UserStats до замены имени бота\n', UserStats,'\n\n')
                            try:
                                UserStats[event.obj.from_id]['UserName']=text
                            except Exception as e:
                                print('Trouble with SetBotName for All Chats. Скорее всего нет такого человека в чате: \n{}\n'.format(e))
                            print('UserStats после замены имени бота\n', UserStats,'\n\n')
                            WriteAllStats(parametrs, UserStats, chat)
                            print('Записали UserStats в файл\n\n')
                        except Exception as e:
                            print('G Trouble with SetBotName for All Chats: \n{}\n'.format(e))
                    UserStats={}
                    UserStats=ReadAllStats(parametrs, UserStats, event.chat_id)



                    try:
                        GN[event.obj.from_id]['UserName']=text+' №'+str(NameSpace)
                    except:
                        GN[event.obj.from_id]={}
                        GN[event.obj.from_id]['BotName']=UserStats[event.obj.from_id]['BotName']
                        GN[event.obj.from_id]['UserName']=text+' №'+str(NameSpace)
                    WriteGN(GN)
                    message='Будешь: '+text+' №'+str(NameSpace)
                    SendMsgToChat(event, message, vk)
                    return UserStats
                elif fakenamespacecheck==-1:
                    message='Слишком много фейков. Прояви фантазию)'
                    SendMsgToChat(event, message, vk)

        elif len(text)>30:
            message='{} ,максимальная длина вашего имени для бота - 30 символов'.format(UserStats[event.obj.from_id]['UserName'])
            SendMsgToChat(event, message, vk)

    except:
        message='Произошла ошибка при смене вашего имени'
        SendMsgToChat(event, message, vk)
        Except(traceback.format_exc(), event, vk)

