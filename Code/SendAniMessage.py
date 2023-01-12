from SendMessage import SendMsgToChat
from vk_api.utils import get_random_id
from time import sleep
moon={0:'🌑', 1:'🌒', 2:'🌓', 3:'🌔', 4:'🌕', 5:'🌖', 6:'🌗', 7:'🌘'}

def Loading(event, vk):
    moonf=0
    well='|'
    wait=':'
    message='[|'+well*int(100/46)*1+wait*(46-int(100/46)*1)+'|] '+moon[moonf]
    par=vk.messages.send(
                user_id=event.obj.from_id,
                message=message,
                random_id=get_random_id(),
                disable_mentions=1
            )
#    Id=SendMsgToChat(event, message, vk)
    print('SendAniMessage Loading par: '+str(par))
    for iter in range(23):
        i=iter+1
        message='[|'+well*int(100/46)*i+wait*(46-int(100/46)*i)+'|] '+moon[moonf]
        moonf+=1
        if moonf==8:
            moonf=0
        sleep(0.6)
        vk.messages.edit(peer_id =event.obj.from_id, message=message, message_id=par)


