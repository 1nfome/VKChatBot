from OpenFiles import OpenGlobalNames, CloseGlobalNames

def ReadGN():
    GlobalNamesFile=OpenGlobalNames('для считывания данных', mode='r')
    GN={}
    for line in GlobalNamesFile:
        Id=int(line[0:-1])
        GN[Id]={}
        GN[Id]['UserName']=GlobalNamesFile.readline()[0:-1]
        GN[Id]['BotName']=GlobalNamesFile.readline()[0:-1]
    CloseGlobalNames('после считывания данных', GlobalNamesFile)
    return GN

def WriteGN(GN):
    GlobalNamesFile=OpenGlobalNames('для записи данных', mode='w')
    for man in GN.keys():
        ttf=str(man)+'\n'
        GlobalNamesFile.write(ttf)
        ttf=str(GN[man]['UserName'])+'\n'
        GlobalNamesFile.write(ttf)
        ttf=str(GN[man]['BotName'])+'\n'
        GlobalNamesFile.write(ttf)
    CloseGlobalNames('после записи данных', GlobalNamesFile)