from vk_api import VkUpload
from vk_api.utils import get_random_id

def SendMsgToChat(event, message, vk, attachs=None, vk_session=None, session=None, man=None):
    vk.messages.setActivity(type='typing',chat_id=event.chat_id)
    attachments = []
    pictures=['jpg','bmp','png']
    if attachs!=None:
        for elem in attachs.keys():
            if elem=='photo':
                image = session.get(attachs[elem], stream=True)
                print('SendMsgToChat photo: {}\n'.format(image.raw))
                photo = VkUpload(vk_session).photo_messages(photos=image.raw)[0]
                attachments.append('photo{}_{}'.format(photo['owner_id'], photo['id']))
            elif elem=='gif':
#                giff = session.get(attachs[elem], stream=True)
#                print('SendMsgToChat giff: {}\n'.format(giff.raw))
#                gif = VkUpload(vk_session).document(doc=giff.raw,
#                                                      title='gif by '+str(man),
#                                                      message_peer_id=event.chat_id+2000000000,
#                                                      doc_type='doc')
#                print('SendMsgToChat gif: {}\n'.format(gif))
#                attachments.append('gif{}_{}'.format(gif['doc']['owner_id'], gif['doc']['id']))
                message=message+'\n\nСсылка на gif: '+attachs[elem]
            elif elem=='audio_message':
#                image = session.get(attachs[elem], stream=True)
#                print('SendMsgToChat audio_message: {}\n'.format(image.raw))
#                audio_message = VkUpload(vk_session).document(doc=image.raw,
#                                                      message_peer_id=event.chat_id+2000000000,
#                                                      doc_type='audio_message')
#                attachments.append('doc{}_{}'.format(audio_message['audio_message']['owner_id'], audio_message['audio_message']['id']))
                message=message+'\n\nСсылка на голосовое: '+attachs[elem]
            elif elem=='audio':
                attachments.append(attachs[elem])
            elif elem=='video':
                if attachs[elem].startswith('video-'):
                    attachments.append(attachs[elem])
                else:
                    message=message+'\n\nСсылка на видео: vk.com/'+attachs[elem]
            elif elem=='poll':
                if attachs[elem].startswith('poll-'):
                    attachments.append(attachs[elem])
                else:
                    message=message+'\n\nСсылка на опрос: vk.com/'+attachs[elem]
            elif elem in pictures:
                picture = session.get(attachs[elem], stream=True)
                print('SendMsgToChat picture: {}\n'.format(picture))
                objectt = VkUpload(vk_session).document(doc=picture.raw,
                                                      title=elem+' by '+str(man),
                                                      message_peer_id=event.chat_id+2000000000,
                                                      doc_type='doc')
                attachments.append('doc{}_{}'.format(objectt['doc']['owner_id'], objectt['doc']['id']))
            elif elem=='main_photo':
                attachments.append('photo'+str(attachs[elem]))
            elif elem=='wall':
                if attachs[elem].startswith('wall-'):
                    attachments.append(attachs[elem])
                else:
                    message=message+'\n\nСсылка на пост: vk.com/'+attachs[elem]
            elif elem=='link':
                if 'story' in attachs[elem]:
                    message=message+'\n\nСсылка на историю: '+attachs[elem]
                if 'audio_playlist' in attachs[elem]:
                    message=message+'\n\nСсылка на музыкальный альбом: '+attachs[elem]
    return vk.messages.send(
                attachment=','.join(attachments),
                chat_id=event.chat_id,
                message=message,
                random_id=get_random_id(),
                disable_mentions=1
            )


def SendMsgToHuman(event, message, vk, attachs=None, vk_session=None, session=None, man=None):
    print('dwdwd')
    vk.messages.setActivity(type='typing',user_id=event.obj.from_id)
    attachments = []
    pictures=['jpg','bmp','png']
    if attachs!=None:
        for elem in attachs.keys():
            if elem=='photo':
                image = session.get(attachs[elem], stream=True)
                print('SendMsgToChat photo: {}\n'.format(image.raw))
                photo = VkUpload(vk_session).photo_messages(photos=image.raw)[0]
                attachments.append('photo{}_{}'.format(photo['owner_id'], photo['id']))
            elif elem=='gif':
#                giff = session.get(attachs[elem], stream=True)
#                print('SendMsgToChat giff: {}\n'.format(giff.raw))
#                gif = VkUpload(vk_session).document(doc=giff.raw,
#                                                      title='gif by '+str(man),
#                                                      message_peer_id=event.chat_id+2000000000,
#                                                      doc_type='doc')
#                print('SendMsgToChat gif: {}\n'.format(gif))
#                attachments.append('gif{}_{}'.format(gif['doc']['owner_id'], gif['doc']['id']))
                message=message+'\n\nСсылка на gif: '+attachs[elem]
            elif elem=='audio_message':
#                image = session.get(attachs[elem], stream=True)
#                print('SendMsgToChat audio_message: {}\n'.format(image.raw))
#                audio_message = VkUpload(vk_session).document(doc=image.raw,
#                                                      message_peer_id=event.chat_id+2000000000,
#                                                      doc_type='audio_message')
#                attachments.append('doc{}_{}'.format(audio_message['audio_message']['owner_id'], audio_message['audio_message']['id']))
                message=message+'\n\nСсылка на голосовое: '+attachs[elem]
            elif elem=='audio':
                attachments.append(attachs[elem])
            elif elem=='video':
                if attachs[elem].startswith('video-'):
                    attachments.append(attachs[elem])
                else:
                    message=message+'\n\nСсылка на видео: vk.com/'+attachs[elem]
            elif elem=='poll':
                if attachs[elem].startswith('poll-'):
                    attachments.append(attachs[elem])
                else:
                    message=message+'\n\nСсылка на опрос: vk.com/'+attachs[elem]
            elif elem in pictures:
                picture = session.get(attachs[elem], stream=True)
                print('SendMsgToChat picture: {}\n'.format(picture))
                objectt = VkUpload(vk_session).document(doc=picture.raw,
                                                      title=elem+' by '+str(man),
                                                      message_peer_id=event.chat_id+2000000000,
                                                      doc_type='doc')
                attachments.append('doc{}_{}'.format(objectt['doc']['owner_id'], objectt['doc']['id']))
            elif elem=='main_photo':
                attachments.append('photo'+str(attachs[elem]))
            elif elem=='wall':
                if attachs[elem].startswith('wall-'):
                    attachments.append(attachs[elem])
                else:
                    message=message+'\n\nСсылка на пост: vk.com/'+attachs[elem]
            elif elem=='link':
                if 'story' in attachs[elem]:
                    message=message+'\n\nСсылка на историю: '+attachs[elem]
                if 'audio_playlist' in attachs[elem]:
                    message=message+'\n\nСсылка на музыкальный альбом: '+attachs[elem]
    print('ddw')
    return vk.messages.send(
                attachment=','.join(attachments),
                user_id=event.obj.from_id,
                message=message,
                random_id=get_random_id()
            )



def SendStickerToChat(event, id, vk):
    vk.messages.send(
                chat_id=event.chat_id,
                sticker_id=id,
                random_id=get_random_id()
            )

def SendGraffityToChat(event, graffiti, session, vk_session, vk):
    message='graffiti{}'.format(graffiti)
    SendMsgToChat(event, message, vk)
    attachments=('graffiti{}'.format(graffiti))
    vk.messages.send(
                peer_id=2000000000+event.chat_id,
                attachment=attachments
            )

def SendAudioMessageToChat(event, Audio, session, vk_session, vk):
    image = session.get(Audio, stream=True)
    Audio = VkUpload(vk_session).document(doc=image.raw,
                                          message_peer_id=event.chat_id+2000000000,
                                          doc_type='audio_message')
    attachments=('doc{}_{}'.format(Audio['audio_message']['owner_id'], Audio['audio_message']['id']))
    vk.messages.send(
                chat_id=event.chat_id,
                attachment=attachments,
                random_id=get_random_id()
            )