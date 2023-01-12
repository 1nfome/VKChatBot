import copy
from OpenFiles import OpenUserStats, CloseUserStats
import traceback
from SendMessage import SendMsgToChat
from GlobalNames import ReadGN

def AddChatToStat(parametrs, vk, UserStats, event, Debug):
    if Debug:
        print('\n\n parametrs до:\n',parametrs.keys(),'\n\n')
    parametrs.pop('Name')
    parametrs.pop('Status')
    parametrs.pop('BotName')
    parametrs.pop('UserName')
    parametrs.pop('Picture')
    GN=ReadGN()
    if Debug:
        print('\n\n parametrs после:\n',parametrs.keys(),'\n\n')
    findadmin = vk.messages.getConversationMembers(peer_id = 2000000000 + event.chat_id)['items']
    members = vk.messages.getConversationMembers(peer_id = 2000000000 + event.chat_id,fields='photo_id, photo_max_orig')['profiles']
#    print('AddChatToStat members: {}\n'.format(members))
    for member in members:
        UserStats[member['id']]={}
        UserStats[member['id']]['Name']=member['first_name']+' '+member['last_name']
        UserStats[member['id']]['Status']='None'

        try:
            UserStats[member['id']]['BotName']=GN[member['id']]['BotName']
            UserStats[member['id']]['UserName']=GN[member['id']]['UserName']
        except:
            UserStats[member['id']]['BotName']='Бот'
            UserStats[member['id']]['UserName']=member['first_name']

        try:
            UserStats[member['id']]['Picture']=member['photo_id']
        except:
            UserStats[member['id']]['Picture']=member['photo_max_orig']
        podparametrs=copy.copy(list(parametrs.keys()))
        for elem in podparametrs:
            UserStats[member['id']][elem]=parametrs[elem][0]
#            print('chat_id: {} user № {}, elem  = {}, text = {}'.format(event.chat_id,member['id'],elem,parametrs[elem][0]))
#    print('AddChatToStat 0 check\n')
    for member in findadmin:
#        print('AddChatToStat noname check\n')
        try:
            if member['is_admin']==True:
                UserStats[member['member_id']]['Privilege']=2
        except:
            pass
#    print('AddChatToStat 2 check\n')
    try:
        UserStats[449891250]['Privilege']=3
    except:
        pass
#    print('AddChatToStat 3 check\n')
    return UserStats


def WriteAllStats(parametrs, UserStats, chat_id):
#    print('проверка связи\n\n')
    UserStatsFile=OpenUserStats(chat_id,'Для записи данных беседы', 'w')
    TextToFile='human= '+str(len(UserStats.keys()))+ '\n'
    UserStatsFile.write(TextToFile)
    for humans in UserStats.keys():
        UserStatsFile.write('*********************************\n')
        TextToFile='human_id: '+str(humans)+ '\n'
        UserStatsFile.write(TextToFile)
        UserStatsFile.write('*********************************\n')
        for characteristic in parametrs.keys():
            TextToFile=str(characteristic)+': '+str(UserStats[humans][characteristic])+ '\n'
            UserStatsFile.write(TextToFile)
    CloseUserStats('После записи данных всех бесед в файл', UserStatsFile)
#    print('проверка связи в конце\n\n')

def ReadAllStats(parametrs, UserStats, chat_id):
#    print('проверка1\n')
    UserStatsFile=OpenUserStats(chat_id,'для считывания данных всех чатов из файла','r')
    for i in range(int(UserStatsFile.readline().split()[1])):
#        print('проверка2\n')
        UserStatsFile.readline()                                                        #**********
        human_id=int(UserStatsFile.readline().split()[1])                               #human_id
        UserStatsFile.readline()                                                        #**********
        UserStats[human_id]=dict.fromkeys(list(parametrs.keys()))
        for elem in parametrs:
#            print('проверка3\n')
            text=UserStatsFile.readline().split()[1:]                                #!&&!&!&!&&!&!&!&!&!&!&&!&!&!&&!&!&&!&!!&&!&!!&!&!&!&!&
#            print('text: {}\n'.format(text))
            text=' '.join(text)
#            print('text after join: {}\n'.format(text))
            if (not '_' in text):
                try:
                    text=int(text)
                except:
                    text=str(text)
#            print('text after try: {}\n'.format(text))
            UserStats[human_id][elem]=text
#            print('user № {}, elem  = {}, text = {}'.format(i,elem,text))
#    print('проверка4\n')
    CloseUserStats('после считывания данных всех чатов из файла', UserStatsFile)
#    print('проверка5\n')
    return UserStats

def NewUser(event, UserStats, parametrs, vk, ChatSet):
    try:
        GN=ReadGN()
        members = vk.messages.getConversationMembers(peer_id = 2000000000 + event.chat_id,fields='photo_id, photo_max_orig')['profiles']
        if str(event.object.action['type'])=='chat_invite_user' and (not str(event.object.action['member_id']).startswith('-')):
            print('\nЧеловек присоеденился к чату\n')
            CheckUser=False
            for ids in UserStats.keys():
                if str(ids)==str(event.object.action['member_id']):
                    print('\nevent.new_man.id= {}\n'.format(event.object.action['member_id']))
                    CheckUser=True
                    break
            if CheckUser==True:
                if ChatSet['parametrs']['ReturnHello']!='None':
                    SendMsgToChat(event, ChatSet['parametrs']['ReturnHello'], vk)
            if CheckUser==False:
                if ChatSet['parametrs']['HelloMessage']!='None':
                    SendMsgToChat(event, ChatSet['parametrs']['HelloMessage'], vk)
                print('\nЭтого человека нет в базе данных\n')
                human={}
                for member in members:
                    if str(member['id'])==str(event.object.action['member_id']):
                        human=member
                        break
                UserStats[event.object.action['member_id']]={}
                UserStats[event.object.action['member_id']]['Name']=human['first_name']+' '+human['last_name']
                UserStats[event.object.action['member_id']]['Status']='None'

                try:
                    UserStats[event.object.action['member_id']]['BotName']=GN[event.object.action['member_id']]['BotName']
                    UserStats[event.object.action['member_id']]['UserName']=GN[event.object.action['member_id']]['UserName']
                except:
                    UserStats[event.object.action['member_id']]['BotName']='Бот'
                    UserStats[event.object.action['member_id']]['UserName']=member['first_name']


                try:
                    UserStats[event.object.action['member_id']]['Picture']=human['photo_id']
                except:
                    UserStats[event.object.action['member_id']]['Picture']=human['photo_max_orig']
                podparametrs=copy.copy(parametrs)
                podparametrs.pop('Name')
                podparametrs.pop('Status')
                podparametrs.pop('BotName')
                podparametrs.pop('UserName')
                podparametrs.pop('Picture')
                for elem in podparametrs:
                    UserStats[event.object.action['member_id']][elem]='0'
                findadmin = vk.messages.getConversationMembers(peer_id = 2000000000 + event.chat_id)['items']
                for member in findadmin:
                    try:
                        if member['is_admin']==True and member['id']==event.object.action['member_id']:
                            UserStats[member['member_id']]['Privilege']=2
                    except:
                        pass
                if event.object.action['member_id']==449891250:
                    UserStats[449891250]['Privilege']='3'
                print('\nЧеловек успешно добавлен в базу данных\n')
                return UserStats
        elif str(event.object.action['type'])=='chat_invite_user_by_link':
#            print('\nЧеловек присоеденился к чату по ссылке\n')
            CheckUser=False
#            print('\nЧеловек присоеденился к чату по ссылке проверка 1\n')
            for ids in UserStats.keys():
#                print('\nЧеловек присоеденился к чату по ссылке проверка 2\n')
                if str(ids)==str(event.object['from_id']):
#                    print('\nЧеловек присоеденился к чату по ссылке проверка 3\n')
#                    print('\nevent.new_man.id= {}\n'.format(event.object.action['member_id']))
#                    print('\nЧеловек присоеденился к чату по ссылке проверка 4\n')
                    CheckUser=True
#                    print('\nЧеловек присоеденился к чату по ссылке проверка 5\n')
                    break
#            print('\nЧеловек присоеденился к чату по ссылке проверка 6\n')
            if CheckUser==True:
                if ChatSet['parametrs']['ReturnHello']!='None':
                    SendMsgToChat(event, ChatSet['parametrs']['ReturnHello'], vk)
            if CheckUser==False:
                if ChatSet['parametrs']['HelloMessage']!='None':
                    SendMsgToChat(event, ChatSet['parametrs']['HelloMessage'], vk)
#                print('\nЧеловек присоеденился к чату по ссылке проверка 7\n')
#                print('\nЭтого человека нет в базе данных\n')
#                print('\nЧеловек присоеденился к чату по ссылке проверка 8\n')
                human={}
#                print('\nЧеловек присоеденился к чату по ссылке проверка 9\n')
                for member in members:
#                    print('\nЧеловек присоеденился к чату по ссылке проверка 10\n')
                    if str(member['id'])==str(event.object['from_id']):
#                        print('\nЧеловек присоеденился к чату по ссылке проверка 11\n')
                        human=member
                        break
#                print('\nЧеловек присоеденился к чату по ссылке проверка 12\n')
                UserStats[event.object['from_id']]={}
                UserStats[event.object['from_id']]['Name']=human['first_name']+' '+human['last_name']
                UserStats[event.object['from_id']]['Status']='None'

                try:
                    UserStats[event.object['from_id']]['BotName']=GN[event.object['from_id']]['BotName']
                    UserStats[event.object['from_id']]['UserName']=GN[event.object['from_id']]['UserName']
                except:
                    UserStats[event.object['from_id']]['BotName']='Бот'
                    UserStats[event.object['from_id']]['UserName']=member['first_name']


                try:
                    UserStats[event.object['from_id']]['Picture']=human['photo_id']
                except:
                    UserStats[event.object['from_id']]['Picture']=human['photo_max_orig']
#                print('\nЧеловек присоеденился к чату по ссылке проверка 13\n')
                podparametrs=copy.copy(parametrs)
#                print('\nЧеловек присоеденился к чату по ссылке проверка 14\n')
                podparametrs.pop('Name')
                podparametrs.pop('Status')
                podparametrs.pop('BotName')
                podparametrs.pop('UserName')
                podparametrs.pop('Picture')
#                print('\nЧеловек присоеденился к чату по ссылке проверка 16\n')
                for elem in podparametrs:
#                    print('\nЧеловек присоеденился к чату по ссылке проверка 17\n')
                    UserStats[event.object['from_id']][elem]='0'
#                print('\nЧеловек присоеденился к чату по ссылке проверка 18\n')
                findadmin = vk.messages.getConversationMembers(peer_id = 2000000000 + event.chat_id)['items']
#                print('\nЧеловек присоеденился к чату по ссылке проверка 19\n')
                for member in findadmin:
#                    print('\nЧеловек присоеденился к чату по ссылке проверка 20\n')
                    try:
                        if member['is_admin']==True and member['id']==event.object['from_id']:

                            UserStats[member['member_id']]['Privilege']=2
#                            print('\nЧеловек присоеденился к чату по ссылке проверка 21\n')
                    except:
                        pass
#                print('\nЧеловек присоеденился к чату по ссылке проверка 22\n')
                if event.object['from_id']==449891250:
#                    print('\nЧеловек присоеденился к чату по ссылке проверка 23\n')
                    UserStats[449891250]['Privilege']='3'
#                print('\nЧеловек присоеденился к чату по ссылке проверка 24\n')
#                print('\nЧеловек успешно добавлен в базу данных\n')
#                print('\nЧеловек присоеденился к чату по ссылке проверка 25\n')
#                print('\nЧеловек присоеденился к чату по ссылке проверка чччч\n')
                return UserStats
    except Exception as e:
        if str(e)!="'NoneType' object is not subscriptable":
            Except(traceback.format_exc(), event, vk)