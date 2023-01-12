from SendMessage import SendMsgToChat
from Times import SecToDate

global Permissions, SwearStatus, GraffityLevel, SpeechStatus

Permissions={0:'Юзверь', 1:'Модератор 👁', 2:"Одмэн 💼", 3:"Создатель 👽"}
SwearStatus={0:'Поборник цензуры', 1:'Приличный человек', 2:'Не брезгует бранным словом', 3:'Любит хорошенько выругаться', 4:'Матерится, как пьяный батя', 5:'Словарь алкаша Валеры',  6:'Психованный школьник'}
GraffityLevel={0:'Кому вообще эти граффити нужны?', 1:'Пачкает заборы', 2:'Когда-то ходил(а) в художку', 3:'Ходит в художку', 4:'Я художник, я так вижу!'}
SpeechStatus={0:'Лучший собеседник', 1:'Учится говорить', 2:'Любитель голосовых', 3:'Лень печатать', 4:'Оратор', 5:'Балабол'}
Banned={0:'Нет 💚',1:'Да 🚫'}
Space='ᅠ'


def GetMyFullStat(UserStats, event, ChatSet, vk, vk_session, session):
    print('GetMyFullStat 1\n')
    try:
        TextToMessage='ᅠᅠᅠᅠ[id'+str(event.obj.from_id)+'|Твоя] статистика:\n\n'
        if UserStats[event.obj.from_id]['Status']!='None':
            dl=len(UserStats[event.obj.from_id]['Status'])
            num=9-dl
            TextToMessage=TextToMessage+Space*num+str(UserStats[event.obj.from_id]['Status'])+'\n\n'
        TextToMessage=TextToMessage+'Бот зовёт тебя: '+UserStats[event.obj.from_id]['UserName']+'\n'\
                                    'Твой уровень доступа к командам: '+Permissions[UserStats[event.obj.from_id]['Privilege']]+'\n'\
                                    'Всего сообщений: '+str(UserStats[event.obj.from_id]['MessageTotal'])+'✉\n'
        if UserStats[event.obj.from_id]['MessageTotal']!=0:
            print("UserStats[event.obj.from_id]['SwearTotal']/UserStats[event.obj.from_id]['MessageTotal']={}/{}={}\n".format(UserStats[event.obj.from_id]['SwearTotal'],UserStats[event.obj.from_id]['MessageTotal'],UserStats[event.obj.from_id]['SwearTotal']/UserStats[event.obj.from_id]['MessageTotal']))
            TextToMessage=TextToMessage+'Всего матерных слов: '+str(UserStats[event.obj.from_id]['SwearTotal'])+'\n'\
                                        'Процент матов на сообщение: '+str(int(UserStats[event.obj.from_id]['SwearTotal']/UserStats[event.obj.from_id]['MessageTotal']*100))+'%\n'\
                                        'Всего слов: '+str(UserStats[event.obj.from_id]['WordsTotal'])+'\n'\
                                        'Всего букв: '+str(UserStats[event.obj.from_id]['LetterTotal'])+'\n'\
                                        'Букв на сообщение: '+str(round(UserStats[event.obj.from_id]['LetterTotal']/UserStats[event.obj.from_id]['MessageTotal'],2))+'\n'
            print('GetMyFullStat 2\n')
            if str(UserStats[event.obj.from_id]['TypingTime'])=='Не определена':
                TextToMessage=TextToMessage+'Примерная скорость набора одного сообщения: '+str(UserStats[event.obj.from_id]['TypingTime'])+'\n'
            else:
                TextToMessage=TextToMessage+'Примерная скорость набора одного сообщения: '+str(round(float(UserStats[event.obj.from_id]['TypingTime']),2))+' сек ⏱\n'
            print('GetMyFullStat 3\n')
            TextToMessage=TextToMessage+'\nᅠᅠᅠᅠТы отправил....\n\n'\
                                      'картинок: '+str(UserStats[event.obj.from_id]['Photos'])+Space*(10-len(str(UserStats[event.obj.from_id]['Photos'])))+'🖼\n'\
                                      'видео: '+str(UserStats[event.obj.from_id]['Videos'])+Space*(12-len(str(UserStats[event.obj.from_id]['Videos'])))+'📽\n'\
                                      'музыки/аудио: '+str(UserStats[event.obj.from_id]['Audios'])+Space*(8-len(str(UserStats[event.obj.from_id]['Audios'])))+'🎧\n'\
                                      'гифок: '+str(UserStats[event.obj.from_id]['Gifs'])+Space*(12-len(str(UserStats[event.obj.from_id]['Gifs'])))+'🎞\n'\
                                      'стикеров: '+str(UserStats[event.obj.from_id]['StickersTotal'])+Space*(11-len(str(UserStats[event.obj.from_id]['StickersTotal'])))+'🃏\n'\
                                      'граффити: '+str(UserStats[event.obj.from_id]['Graffity'])+Space*(10-len(str(UserStats[event.obj.from_id]['Graffity'])))+'🖌\n'\
                                      'голосовых сообщений: '+str(UserStats[event.obj.from_id]['Speech'])+Space*(4-len(str(UserStats[event.obj.from_id]['Speech'])))+'🎤\n'\
                                      'голосований: '+str(UserStats[event.obj.from_id]['Poll'])+Space*(9-len(str(UserStats[event.obj.from_id]['Poll'])))+'☑\n'
    except Exception as e:
        print('ошибка в GetMyFullStat: {}\n'.format(e))
    if UserStats[event.obj.from_id]['Privilege']<2:
        TextToMessage=TextToMessage+'\nᅠᅠᅠᅠᅠКроме того:\n\n'
        print('GetMyFullStat 4\n')
        warn=UserStats[event.obj.from_id]['Warn']
        spisok=['2','3','4']
        spisok2=['5','6','7','8','9','0']
        final=' '
        if str(warn)[-1]=='1':
            final='ие'
        elif (str(warn)[-1] in spisok) and (warn<12 or warn>14):
            final='ия'
        elif (str(warn)[-1] in spisok2) or 5<=warn<=20:
            final='ий'
        print('GetMyFullStat 5\n')
        TextToMessage=TextToMessage+'У тебя '+str(warn)+' предупрежден'+final+' из '+str(ChatSet['parametrs']['warn_numbers'])+'⚠\n'\
                                    'И '+str(UserStats[event.obj.from_id]['SpamTotal'])+' из 10 уровень спама 🚦\n'
    attach={}
    if str(UserStats[event.obj.from_id]['Picture']).startswith('https'):
        attach['photo']=UserStats[event.obj.from_id]['Picture']
    else:
        attach['main_photo']=UserStats[event.obj.from_id]['Picture']
    print('GetMyFullStat 6\n')
    SendMsgToChat(event, '', vk, attach, vk_session, session)
    SendMsgToChat(event, TextToMessage, vk)


def GetMyMiniStat(UserStats, event, ChatSet, vk):
    TextToMessage='ᅠᅠᅠᅠ[id'+str(event.obj.from_id)+'|Твоя] статистика кратко:\n\n'\
                  'Твой уровень доступа к командам: '+Permissions[UserStats[event.obj.from_id]['Privilege']]+'\n'\
                  'Всего сообщений: '+str(UserStats[event.obj.from_id]['MessageTotal'])+'✉\n'
    if UserStats[event.obj.from_id]['Privilege']<2:
        TextToMessage=TextToMessage+'\nᅠᅠᅠᅠКроме того:\n\n'
        warn=UserStats[event.obj.from_id]['Warn']
        spisok=['2','3','4']
        spisok2=['5','6','7','8','9','0']
        final=' '
        if str(warn)[-1]=='1':
            final='ие'
        elif (str(warn)[-1] in spisok) and (warn<12 or warn>14):
            final='ия'
        elif (str(warn)[-1] in spisok2) or 5<=warn<=20:
            final='ий'
        TextToMessage=TextToMessage+'У тебя '+str(warn)+' предупрежден'+final+' из '+str(ChatSet['parametrs']['warn_numbers'])+'⚠\n'\
                                    'И '+str(UserStats[event.obj.from_id]['SpamTotal'])+' из 10 уровень спама 🚦\n'
    SendMsgToChat(event, TextToMessage, vk)

def GetUserFullStat(UserStats, event, ChatSet, vk, Id, Name, vk_session, session):
    print('GetUserFullStat\n')
    TextToMessage='Статистика '+Name+':\n\n'
    if UserStats[Id]['Status']!='None':
            dl=len(UserStats[Id]['Status'])
            num=9-dl
            TextToMessage=TextToMessage+Space*num+str(UserStats[Id]['Status'])+'\n\n'
    TextToMessage=TextToMessage+'Бот зовёт его: '+UserStats[Id]['UserName']+'\n'\
                  'Он назвал бота: '+UserStats[Id]['BotName']+'\n'
    if UserStats[Id]['Privilege']<2:
        TextToMessage+='Бот забанил его? '+Banned[UserStats[Id]['BlackList']]+'\n'

    TextToMessage+='Уровень доступа к командам: '+Permissions[UserStats[Id]['Privilege']]+'\n'\
                  'Всего сообщений: '+str(UserStats[Id]['MessageTotal'])+'✉\n'
    if UserStats[Id]['MessageTotal']!=0:
        TextToMessage+='Всего матерных слов: '+str(UserStats[Id]['SwearTotal'])+'\n'\
                       'Процент матов на сообщение: '+str(int(UserStats[Id]['SwearTotal']/UserStats[Id]['MessageTotal']*100))+'%\n'\
                       'Всего слов: '+str(UserStats[Id]['WordsTotal'])+'\n'\
                       'Всего букв: '+str(UserStats[Id]['LetterTotal'])+'\n'\
                       'Букв на сообщение: '+str(round(UserStats[Id]['LetterTotal']/UserStats[Id]['MessageTotal'],2))+'\n'
        print('GetUserFullStat 2\n')
        if str(UserStats[Id]['TypingTime'])=='Не определена':
            TextToMessage=TextToMessage+'Примерная скорость набора одного сообщения: '+str(UserStats[Id]['TypingTime'])+'\n'
        else:
            TextToMessage=TextToMessage+'Примерная скорость набора одного сообщения: '+str(round(float(UserStats[Id]['TypingTime']),2))+' сек ⏱\n'
        print('GetUserFullStat 3\n')
        if UserStats[Id]['LastActiveTime']!='Еще до появления бота':
            date=SecToDate(float(UserStats[Id]['LastActiveTime']))+' по МСК'
        else:
            date=UserStats[Id]['LastActiveTime']
    #    print('GetUserFullStat: {}\n'.format(date))
        TextToMessage=TextToMessage+'Последняя активность в беседе:\n'+str(date)+'\n'\
                      '\nᅠᅠᅠᅠОн отправил....\n\n'\
                      'картинок: '+str(UserStats[Id]['Photos'])+'🖼\n'\
                      'видео: '+str(UserStats[Id]['Videos'])+'📽\n'\
                      'музыки/аудио: '+str(UserStats[Id]['Audios'])+'🎧\n'\
                      'гифок: '+str(UserStats[Id]['Gifs'])+'\n'\
                      'стикеров: '+str(UserStats[Id]['StickersTotal'])+'🃏\n'\
                      'граффити: '+str(UserStats[Id]['Graffity'])+'🖌\n'\
                      'голосовых: '+str(UserStats[Id]['Speech'])+'🎤\n'\
                      'голосований: '+str(UserStats[Id]['Poll'])+'☑\n'
    if UserStats[Id]['Privilege']<2:
        TextToMessage=TextToMessage+'\nᅠᅠᅠᅠᅠКроме того:\n\n'
        print('GetUserFullStat 4\n')
        warn=UserStats[Id]['Warn']
        spisok=['2','3','4']
        spisok2=['5','6','7','8','9','0']
        final=' '
        if str(warn)[-1]=='1':
            final='ие'
        elif (str(warn)[-1] in spisok) and (warn<12 or warn>14):
            final='ия'
        elif (str(warn)[-1] in spisok2) or 5<=warn<=20:
            final='ий'
        TextToMessage=TextToMessage+'У него '+str(warn)+' предупрежден'+final+' из '+str(ChatSet['parametrs']['warn_numbers'])+'⚠\n'\
                                    'И '+str(UserStats[Id]['SpamTotal'])+' из 10 уровень спама 🚦\n'
    attach={}
    if str(UserStats[Id]['Picture']).startswith('https'):
        attach['photo']=UserStats[Id]['Picture']
    else:
        attach['main_photo']=UserStats[Id]['Picture']
    SendMsgToChat(event, '', vk, attach, vk_session, session)
    SendMsgToChat(event, TextToMessage, vk)


def GetUserMiniStat(UserStats, event, ChatSet, vk, Id, Name):
    print('GetUserMiniStat 1\n')
    TextToMessage='Статистика '+Name+' кратко:\n\n'\
                  'Он назвал бота: '+UserStats[Id]['BotName']+'\n'\
                  'Бот зовёт его: '+UserStats[Id]['UserName']+'\n'\
                  'Его уровень доступа к командам: '+Permissions[UserStats[Id]['Privilege']]+'\n'
    if UserStats[Id]['Privilege']<2:
        TextToMessage+='Бот забанил его? '+Banned[UserStats[Id]['BlackList']]+'\n'
    TextToMessage+='Всего сообщений: '+str(UserStats[Id]['MessageTotal'])+'✉\n'
    if UserStats[Id]['MessageTotal']!=0:
        if UserStats[Id]['LastActiveTime']!='Еще до появления бота':
            date=SecToDate(float(UserStats[Id]['LastActiveTime']))+' по МСК'
        else:
            date=UserStats[Id]['LastActiveTime']
        TextToMessage=TextToMessage+'Последняя активность в беседе:\n'+date+'\n'

    if UserStats[Id]['Privilege']<2:
        TextToMessage=TextToMessage+'\nᅠᅠᅠᅠᅠКроме того:\n\n'
        print('GetUserFullStat 4\n')
        warn=UserStats[Id]['Warn']
        spisok=['2','3','4']
        spisok2=['5','6','7','8','9','0']
        final=' '
        if str(warn)[-1]=='1':
            final='ие'
        elif (str(warn)[-1] in spisok) and (warn<12 or warn>14):
            final='ия'
        elif (str(warn)[-1] in spisok2) or 5<=warn<=20:
            final='ий'
        TextToMessage=TextToMessage+'У него '+str(warn)+' предупрежден'+final+' из '+str(ChatSet['parametrs']['warn_numbers'])+'⚠\n'\
                                    'И '+str(UserStats[Id]['SpamTotal'])+' из 10 уровень спама 🚦\n'
    print('GetUserMiniStat 6\n')
    SendMsgToChat(event, TextToMessage, vk)