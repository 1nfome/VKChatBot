import os


def OpenIdBase(text, mode='r'):
    try:
        IdBaseFile = open('/app/Data/IdBase.txt', mode)
    #        print('IdBase успешно открыт для {} {}\n'.format(mode, text))
    except Exception as e:
        print('Произошла ошибка при открытии файла IdBaseFile для {} {}\n{}\n'.format(mode, text, e))
    return IdBaseFile


def CloseIdBase(text, IdBaseFile):
    try:
        IdBaseFile.close()
    #        print('IdBase {} закрыт {}\n'.format(IdBaseFile.closed, text))
    except Exception as e:
        print('Произошла ошибка при закрытии файла IdBaseFile для {}\n{}\n'.format(text, e))


def OpenGlobalNames(text, mode='r'):
    try:
        GlobalNamesFile = open('/app/Data/GlobalNames.txt', mode)
    #        print('GlobalNames успешно открыт для {} {}\n'.format(mode, text))
    except Exception as e:
        print('Произошла ошибка при открытии файла GlobalNamesFile для {} {}\n{}\n'.format(mode, text, e))
    return GlobalNamesFile


def CloseGlobalNames(text, GlobalNamesFile):
    try:
        GlobalNamesFile.close()
    #        print('GlobalNames {} закрыт {}\n'.format(GlobalNamesFile.closed, text))
    except Exception as e:
        print('Произошла ошибка при закрытии файла GlobalNamesFile для {}\n{}\n'.format(text, e))


def OpenUserMessage(UserId, ChatId, text, mode='r'):
    try:
        Text = "/app/Data/UserMessages/User_" + str(UserId) + "_in chat_" + str(ChatId) + ".txt"
        #        if mode=='w' and (not os.path.isfile(Text)):
        #            os.popen('touch '+Text)
        UserMessageFile = open(Text, mode)
    #        print('UserMessageFile успешно открыт для {} {}\n'.format(mode, text))
    except Exception as e:
        print('Произошла ошибка при открытии файла UserMessageFile для {} {}\n{}\n'.format(mode, text, e))
    return UserMessageFile


def CloseUserMessage(text, UserMessageFile):
    try:
        UserMessageFile.close()
    #        print('UserMessageFile {} закрыт {}\n'.format(UserMessageFile.closed, text))
    except Exception as e:
        print('Произошла ошибка при закрытии файла UserMessageFile для {}\n{}\n'.format(text, e))


def OpenParam(text, mode='r'):
    try:
        ParametrsFile = open('/app/Data/ParamFile.txt', mode)
    #        print('ParametrsFile успешно открыт для {} {}\n'.format(mode, text))
    except Exception as e:
        print('Произошла ошибка при открытии файла ParametrsFile для {} {}\n{}\n'.format(mode, text, e))
    return ParametrsFile


def CloseParam(text, ParametrsFile):
    try:
        ParametrsFile.close()
    #        print('ParametrsFile {} закрыт {}\n'.format(ParametrsFile.closed, text))
    except Exception as e:
        print('Произошла ошибка при закрытии файла ParametrsFile для {}\n{}\n'.format(text, e))


def OpenChatParam(text, mode='r'):
    try:
        ChatParamFile = open('/app/Data/ChatParam.txt', mode)
    #        print('ChatParamFile успешно открыт для {} {}\n'.format(mode, text))
    except Exception as e:
        print('Произошла ошибка при открытии файла ChatParamFile для {} {}\n{}\n'.format(mode, text, e))
    return ChatParamFile


def CloseChatParam(text, ChatParamFile):
    try:
        ChatParamFile.close()
    #        print('ChatParamFile {} закрыт {}\n'.format(ChatParamFile.closed, text))
    except Exception as e:
        print('Произошла ошибка при закрытии файла ChatParamFile для {}\n{}\n'.format(text, e))


def OpenChatSet(chat_id, text, mode='r'):
    try:
        if mode == 'w':
            ChatSetFile = os.open('/app/Data/ChatsSettings/ChatSet_for_' + str(chat_id) + '_chat.txt', os.O_CREAT)
        ChatSetFile = open('/app/Data/ChatsSettings/ChatSet_for_' + str(chat_id) + '_chat.txt', mode)
    #        print('ChatSetFile успешно открыт для {} {}\n'.format(mode, text))
    except Exception as e:
        print('Произошла ошибка при открытии файла ChatSetFile для {} {}\n{}\n'.format(mode, text, e))
    return ChatSetFile


def CloseChatSet(text, ChatSetFile):
    try:
        ChatSetFile.close()
    #        print('ChatSetFile {} закрыт {}\n'.format(ChatSetFile.closed, text))
    except Exception as e:
        print('Произошла ошибка при закрытии файла ChatSetFile для {}\n{}\n'.format(text, e))


def OpenUserStats(chat_id, text, mode='r'):
    try:
        Text = '/app/Data/UserStats/US_for_' + str(chat_id) + '_chat.txt'
        UserStatsFile = open(Text, mode)
    #        print('UserStatsFile успешно открыт для {} {}\n'.format(mode, text))
    except Exception as e:
        print('Произошла ошибка при открытии файла UserStatsFile для {} чата, для {}\n{}\n'.format(chat_id, mode, text,
                                                                                                   e))
    return UserStatsFile


def CloseUserStats(text, UserStatsFile):
    try:
        UserStatsFile.close()
    #        print('UserStatsFile {} закрыт {}\n'.format(UserStatsFile.closed, text))
    except:
        print('Произошла ошибка при закрытии UserStatsFile ', text)


def OpenErrorsFile(text, mode='r'):
    try:
        FileForErrors = open('/app/Data/errorLog.txt', mode)
    except Exception as e:
        print('Ошибка при открытии FileForErrors для {} {}:\n{}\n'.format(mode, text, e))
    return FileForErrors


def CloseErrorsFile(text, FileForErrors):
    try:
        FileForErrors.close()
    except Exception as e:
        print('Ошибка при закрывании FileForErrors {}: \n{}\n'.format(text, e))


def OpenCommandsFile(text, mode='r'):
    try:
        CommandsFile = open('/app/Data/Commands.txt', mode)
    except Exception as e:
        print('Ошибка при открытии CommandsFile для {} {}:\n{}\n'.format(mode, text, e))
    return CommandsFile


def CloseCommandsFile(text, CommandsFile):
    try:
        CommandsFile.close()
    except Exception as e:
        print('Ошибка при закрытии CommandsFile {}:\n{}\n'.format(text, e))


def OpenSwearList(text, mode='r'):
    try:
        SwearList = open('/app/Data/Swear.txt', mode)
    except Exception as e:
        print('Ошибка при открытии SwearList для {} {} :\n{}\n'.format(mode, text, e))
    return SwearList


def CloseSwearList(text, SwearList):
    try:
        SwearList.close()
    except Exception as e:
        print('Ошибка при закрытии SwearList {}:\n{}\n'.format(text, e))


def OpenSpamReact(text, mode='r'):
    try:
        SpamReact = open('/app/Data/SpamReact.txt', mode)
    except Exception as e:
        print('Ошибка при открытии SpamReact для {} {} :\n{}\n'.format(mode, text, e))
    return SpamReact


def CloseSpamReact(text, SpamReact):
    try:
        SpamReact.close()
    except Exception as e:
        print('Ошибка при закрытии SpamReact {}:\n{}\n'.format(text, e))
