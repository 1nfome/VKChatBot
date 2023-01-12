from SendMessage import SendMsgToChat

def WhoOnline(vk,event,vk_session,session):
    mans=vk.messages.getConversationMembers(peer_id = 2000000000 + event.chat_id, fields='online')['profiles']
    print('ShowOnline WhoOnline mans:',mans)
    onlines={}
    for man in mans:
        if man['online']==1:
            mobile=False
            try:
                if bool(man['online_app'])==True:
                    mobile=True
            except:
                pass
            if mobile==False:
                try:
                    if bool(man['online_mobile'])==True:
                        mobile=True
                except:
                    pass
            if mobile==True and man['id']!=event.obj.from_id:
                onlines[man['first_name']+' '+man['last_name']]='📱'
            elif mobile==False and man['id']!=event.obj.from_id:
                onlines[man['first_name']+' '+man['last_name']]=''
    if str(onlines)=='{}':
        TextToMessage='Ни кого кроме вас нет в сети'
        SendMsgToChat(event, TextToMessage, vk, {'main_photo':'-185153508_457239025'}, vk_session, session)
    elif len(onlines.keys())==1:
        TextToMessage='В сети только вы и '
        for man in onlines.keys():
            TextToMessage+=man+onlines[man]
        SendMsgToChat(event, TextToMessage, vk)
    else:
        TextToMessage='В сети только вы и еще '+str(len(onlines.keys()))+' человек:\n'
        for man in onlines.keys():
            TextToMessage+=man+onlines[man]+'\n'
        SendMsgToChat(event, TextToMessage, vk)
