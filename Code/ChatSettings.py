from OpenFiles import OpenChatSet, CloseChatSet

def ReadChatSet(chat_id, ChatParam):
    ChatSetFile=OpenChatSet(chat_id, 'для считывания всех настроек чата', 'r')
    ChatSet={}
    ChatSet['parametrs']={}
    for elem in ChatParam.keys():
        tempelem=ChatSetFile.readline().split()[1]
        print('ReadChatSet считано из параметров: '+str(tempelem), 'чат '+str(chat_id))
        try:
            ChatSet['parametrs'][elem]=int(tempelem)
        except:
            ChatSet['parametrs'][elem]=str(tempelem)
    kek=ChatSetFile.readline()                           # ///////////////////////////////
    print('ReadChatSet параметры вродь закончились:', kek, 'чат '+str(chat_id),'\n')
    classnumb=int(ChatSetFile.readline().split()[1])      # количество классов
    print('ReadChatSet Закончили считывать параметры  чата. начали считывать классы', 'чат '+str(chat_id))
    if classnumb>0:
        ChatSet['classes']={}
        for num in range(classnumb):
            NameAndSmile=ChatSetFile.readline().split()
            ChatSet['classes'][NameAndSmile[0]]={}
            try:
                ChatSet['classes'][NameAndSmile[0]]['smile']=NameAndSmile[1]
            except:
                ChatSet['classes'][NameAndSmile[0]]['smile']=''
            ChatSet['classes'][NameAndSmile[0]]['cmds']=ChatSetFile.readline().split()
            ChatSet['classes'][NameAndSmile[0]]['Can_spam']=ChatSetFile.readline().split()[1]
    else:
        ChatSet['classes']=0
    CloseChatSet('после считывания всех настроек из всех чатов', ChatSetFile)
    return ChatSet

def ChatSetToFile(ChatSet, chat_id):
    ChatSetFile=OpenChatSet(chat_id, 'для записи всех настроек чата', 'w')
    print('ChatSettings ChatSetToFile ChatSet',str(ChatSet))
    for param in ChatSet['parametrs'].keys():
        TextToFile=str(param)+': '+str(ChatSet['parametrs'][param])+'\n'
        ChatSetFile.write(TextToFile)
    TextToFile='///////////////////////////////\n'
    ChatSetFile.write(TextToFile)
    print('ChatSet перед записью в файл: '+str(ChatSet), 'чат '+str(chat_id),'\n')
    if ChatSet['classes']!=0:
        TextToFile='Classes: '+str(len(ChatSet['classes'].keys()))+'\n'
        ChatSetFile.write(TextToFile)
        for clas in ChatSet['classes'].keys():
            count=0
            for word in ChatSet['classes'][clas]['cmds']:
                count+=1
            if count>1:
                TextToFile=str(clas)+' '+str(ChatSet['classes'][clas]['smile'])+'\n'+str(' '.join(ChatSet['classes'][clas]['cmds']))+'\nCan_spam '+str(ChatSet['classes'][clas]['Can_spam'])+'\n'
            else:
                TextToFile=str(clas)+' '+str(ChatSet['classes'][clas]['smile'])+'\n'+str(ChatSet['classes'][clas]['cmds'][0])+'\nCan_spam '+str(ChatSet['classes'][clas]['Can_spam'])+'\n'
            ChatSetFile.write(TextToFile)
    else:
        TextToFile='Classes: 0\n'
        ChatSetFile.write(TextToFile)
    CloseChatSet('после записи всех параметров всех чатов в файл', ChatSetFile)