from OpenFiles import OpenSwearList, CloseSwearList
from SendMessage import SendMsgToChat

def AddSwear(msg, event, vk):
    try:
        text=msg[msg.find('addswear')+9:]
        SwearList=OpenSwearList('Для считывания ругательств в начале добавления нового', 'r')
        Swear=SwearList.read().split()
        Swear.append(text)
        print('AddSwear text:{}\n'.format(text))
        CloseSwearList('После считывания ругательств в начале добавления нового', SwearList)
        SwearList=OpenSwearList('Для перезаписи ругательств и добавления нового', 'w')
        for word in Swear:
            TextToFile=word+' '
            SwearList.write(TextToFile)
        CloseSwearList('После перезаписи ругательств в конце добавления нового', SwearList)
        message='"'+text+'" успешно добавлен в список матов'
        SendMsgToChat(event, message, vk)
    except:
        message='Что-то пошло не так в AddSwear'
        SendMsgToChat(event, message, vk)

def DelSwear(msg, event, vk):
    try:
    #    print('DelSwear 1\n')
        text=msg[msg.find('delswear')+9:]
    #    print('DelSwear 2\n')
        SwearList=OpenSwearList('Для считывания ругательств в начале добавления нового', 'r')
    #    print('DelSwear 3\n')
        Swear=SwearList.read().split()
    #    print('DelSwear 4\nmsg={}\n'.format(msg))
    #    print('DelSwear 4\ntext={}\n'.format(text))
    #    print('DelSwear 4\nSwears={}\n'.format(Swear))
        Swear.remove(text)
    #    print('DelSwear 5\n')
        CloseSwearList('После считывания ругательств в начале добавления нового', SwearList)
    #    print('DelSwear 6\n')
        SwearList=OpenSwearList('Для перезаписи ругательств и добавления нового', 'w')
    #    print('DelSwear 7\n')
        for word in Swear:
            TextToFile=word+' '
            SwearList.write(TextToFile)
    #        print('DelSwear xxxx\n')
        CloseSwearList('После перезаписи ругательств в конце добавления нового', SwearList)
    #    print('DelSwear 8\n')
        message='"'+text+'" успешно удалён из списка матов'
    #    print('DelSwear 9\n')
        SendMsgToChat(event, message, vk)
    #    print('DelSwear 10\n')
    except:
        message='Что-то пошло не так в DelSwear'
        SendMsgToChat(event, message, vk)
