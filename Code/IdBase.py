import os
from OpenFiles import OpenIdBase, CloseIdBase

def StartIdBase(IdBase, event, vk):
    if (os.stat('/app/Data/IdBase.txt').st_size==0) and (str(IdBase)=='{}'):                                                                         # Если IdBase пусто
        IdBase[event.chat_id]=[]
        members=vk.messages.getConversationMembers(peer_id = 2000000000 + event.chat_id,fields='photo_id')['profiles']
        for member in members:
            IdBase[event.chat_id].append(member['id'])                                          # заполнение базы id
#        print('idbase dict заполнен с нуля при пустом файле')
    elif (os.stat('/app/Data/IdBase.txt').st_size!=0) and (str(IdBase)=='{}'):
        IdBaseFile=OpenIdBase('для считывания id всех людей из всех чатов', 'r')
        temp=int(IdBaseFile.readline().split()[1])                 # //////////////
        for chat in range(temp):  # количество чатов
            IdBaseFile.readline()
            ChatId=int(IdBaseFile.readline().split()[1])           # chat_id:
            IdBase[ChatId]=[]
            IdBaseFile.readline()                                  # //////////////
            humans=int(IdBaseFile.readline().split()[1])           # human=
            IdBaseFile.readline()                                  # **************
            for human in range(humans):
                IdBase[ChatId].append(int(IdBaseFile.readline()))
#        print('IdBase с нуля считан из файла')
        CloseIdBase('после считывания id всех людей из всех чатов', IdBaseFile)
    return IdBase

def IsChatOnBase(IdBase, event):
    CheckChatId=False                                                           # проверяем наличие чата в базе ID
    for elem in IdBase.keys():
        if int(elem)==int(event.chat_id):
#            print('IdBase этого чата уже есть в словаре\n')
            CheckChatId=True
            break
    return CheckChatId

def ChatToIdBase(IdBase, event, vk):
    IdBase[event.chat_id]=[]
    members=vk.messages.getConversationMembers(peer_id = 2000000000 + event.chat_id,fields='photo_id')['profiles']
    for member in members:
        IdBase[event.chat_id].append(member['id'])                                          # Дополняем Базу ID в случае необходимости
    return IdBase

def IdBaseToFile(IdBase):
    IdBaseFile=OpenIdBase('для записи id всех людей из всех чатов после добавления нового', 'w')
    TextToFile='Chats: '+str(len(IdBase.keys()))+'\n'
    IdBaseFile.write(TextToFile)
    for chat in IdBase.keys():
        IdBaseFile.write('///////////////////////////////\n')
        TextToFile='сhat_id: '+str(chat)+'\n'
        IdBaseFile.write(TextToFile)
        IdBaseFile.write('///////////////////////////////\n')
        TextToFile='human= '+str(len(IdBase[chat]))+'\n'
        IdBaseFile.write(TextToFile)
        IdBaseFile.write('*******************************\n')
        for human in IdBase[chat]:
            TextToFile=str(human)+'\n'
            IdBaseFile.write(TextToFile)
    CloseIdBase('после записи id всех людей из всех чатов', IdBaseFile)
