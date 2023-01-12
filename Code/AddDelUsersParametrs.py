from AddReadWriteUsersStats import WriteAllStats, ReadAllStats
from OpenFiles import OpenParam, CloseParam
from SendMessage import SendMsgToChat
import copy

def AddUsersParametr(BotName, msg, UserStats, event, parametrs, Debug, vk, IdBase):
#    print('парарам\n\n')
    i=0
    if msg.startswith(BotName) and ('addpar' in msg):

        if True:
            if UserStats[event.obj.from_id]['Privilege']==3:
                print('rerfhtre\n\n')
                while i<30:
                    if list(msg)[i:i+7]==list('addpar '):
                        break
                    i+=1
                i+=7
                FirstPoint=i
                if i<30:
                    print('rerfhtre2\n\n')
                    while FirstPoint<70:
                        if list(msg)[FirstPoint]=='.':
                            break
                        FirstPoint+=1
                    FirstPoint+=1
                    if FirstPoint<70:
                        print('rerfhtre3\n\n')
                        SecondPoint=FirstPoint
                        while SecondPoint<130:
                            if list(msg)[SecondPoint]=='.':
                                break
                            SecondPoint+=1
                        SecondPoint+=1
                        if SecondPoint<130:
                            print('rerfhtre4\n\n')
                            Temp1=str(''.join(list(msg)[i:FirstPoint-1]))
                            Temp2=''.join(list(msg)[FirstPoint:SecondPoint-1])
                            try:
                                Temp2=int(Temp2)
                            except:
                                Temp2=str(Temp2)
                            Temp3=str(''.join(list(msg)[SecondPoint:]))
                            newparam=copy.copy(parametrs)
                            newparam[Temp1]=[Temp2, Temp3]
#                            print('temp1= {}  temp2 = {}  temp3 = {}'.format(Temp1,Temp2,Temp3))
                            print('rerfhtre5\n\n')
                            print('IdBase  ', IdBase,'\n\n')
                            for chat in IdBase.keys():
                                try:
                                    print('chat ', chat,'\n\n')
                                    UserStats={}
                                    UserStats=ReadAllStats(parametrs, UserStats, chat)
                                    print('UserStats ', UserStats,'\n\n')
                                    for human in UserStats.keys():                                                            #Добавление нового параметра всем людям
                                        print('human: ',human,'\n')
    #                                    print('тест из AddDelUsersParametrs\n')
    #                                    print('UserStats[{}][{}][{}]={}     /[Temp3={}]/\n'.format(chats, human, Temp1, Temp2, Temp3))
                                        UserStats[human][Temp1]=Temp2
                                    print('UserStats ', UserStats,'\n\n')
                                    WriteAllStats(newparam, UserStats, chat)
                                    print('Записали UserStats в файл\n\n')
                                except Exception as e:
                                    print(e,'\n')
#                            print('\nUserStats: \n', UserStats)
                            print('rerfhtre7\n\n')
                            parametrs[Temp1]=[Temp2, Temp3]
#                            print('\nparametrs: \n', parametrs)
                            ParametrsFile=OpenParam('Для добавления нового параметра', 'a')                               # Добавление нового параметра в файл
                            TextToFile=Temp1+' '+str(Temp2)+'\n'+Temp3+'\n'
                            ParametrsFile.write(TextToFile)
                            print('rerfhtre8\n\n')
                            CloseParam('После добавления нового параметра', ParametrsFile)
                            ToReturn=[]
                            ToReturn.append(UserStats)
                            ToReturn.append(newparam)
                            message='Параметр '+str(Temp1)+', имеющий Default: '+str(Temp2)+' и Special Key: '+str(Temp3)+' успешно добавлен в список параметров и статистику пользователей'
                            SendMsgToChat(event, message, vk)
                            return ToReturn
                        else:
                            message='Default-значение характеристики должно быть не длиннее ~60 символов'
                            SendMsgToChat(event, message, vk)
                    else:
                        message='Название характеристики должно быть не длиннее ~40 символов'
                        SendMsgToChat(event, message, vk)
                else:
                    message='Сори, но походу у бота слишком длинное имя'
                    SendMsgToChat(event, message, vk)
            elif UserStats[event.obj.from_id]['Privilege']<3:
                message='Данная команда разрешена только создателю бота'
                SendMsgToChat(event, message, vk)

def DelUsersParametr(BotName, msg, UserStats, event, parametrs, Debug, vk, IdBase):
    variants={BotName+'удали параметр':2, BotName+' удали параметр':3,BotName+',удали параметр':2,BotName+', удали параметр':3}
    Check=False
    for elem in variants.keys():
        if msg.startswith(elem):
            if UserStats[event.obj.from_id]['Privilege']==3:
                temp=msg.split()[variants[elem]]
                message='Параметр '+str(temp)+', имеющий Default: '+str(parametrs[str(temp)][0])+' и Special Key: '+str(parametrs[str(temp)][1])+' успешно удалён из списка параметров и статистик пользователей'
                newparam=copy.copy(parametrs)
                newparam.pop(temp)
                for chat in IdBase.keys():
                    UserStats={}
                    UserStats=ReadAllStats(parametrs, UserStats, chat)
                    for human in UserStats.keys():                                                            #Добавление нового параметра всем людям
#                       print('тест из AddDelUsersParametrs\n')
#                       print('UserStats[{}][{}][{}]={}     /[Temp3={}]/\n'.format(chats, human, Temp1, Temp2, Temp3))
                        UserStats[human].pop(temp)
                    WriteAllStats(newparam, UserStats, chat)
                ParametrsFile=OpenParam('Для удаления параметра', 'w')
                TextToFile='Name\nStatus\nBotName\nUserName\nPicture\n'
                ParametrsFile.write(TextToFile)
                podparametrs=newparam.copy()
                podparametrs.pop('Name')
                podparametrs.pop('Status')
                podparametrs.pop('BotName')
                podparametrs.pop('UserName')
                podparametrs.pop('Picture')
                for one in podparametrs.keys():
                    TextToFile=one+' '+str(podparametrs[one][0])+'\n'+str(podparametrs[one][1])+'\n'
                    ParametrsFile.write(TextToFile)
                CloseParam('После удаления параметра', ParametrsFile)
                Check=True
                ToReturn=[]
                ToReturn.append(UserStats)
                ToReturn.append(newparam)
                SendMsgToChat(event, message, vk)
                return ToReturn
            else:
                message='Данная команда разрешена только создателю бота'
                SendMsgToChat(event, message, vk)
                Check=True
                break
        if Check==True:
            break