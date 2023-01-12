from time import ctime, time
days={'Sun':'Воскресенье', 'Mon':'Понедельник', 'Tue':'Вторник', 'Wed':'Среда', 'Thu':'Четверг', 'Sat':'Суббота', 'Fri':'Пятница'}
week={1:'Понедельник', 2:'Вторник', 3:'Среда', 4:'Четверг', 5:'Пятница', 6:'Суббота', 7:'Воскресенье'}
weekcase={'Понедельник':'В этот Понедельник', 'Вторник':'В этот Вторник', 'Среда':'В эту Среду', 'Четверг':'В этот Четверг', 'Пятница':'В эту Пятницу'}
weeknumb={'Понедельник':1, 'Вторник':2, 'Среда':3, 'Четверг':4, 'Пятница':5, 'Суббота':6, 'Воскресенье':7}
months={'Jan':'Января', 'Feb':'Февраля', 'Mar':'Марта', 'Apr':'Апреля', 'May':'Мая', 'Jun':'Июня', 'Jul':'Июля', 'Aug':'Августа', 'Sep':'Сентября', 'Oct':'Октября', 'Nov':'Ноября', 'Dec':'Декабря'}

#def SecToDate(sec, delta=60*60*3):
#    print('SecToDate 1\n')
#    Time=ctime(sec+delta).split()
#    print('SecToDate 1\n')
#    print('SecToDate 1\n')
#    #######день недели##########день месяца########месяц#################время дня#########год
#    date=str(days[Time[0]])+' '+str(Time[2])+' '+str(months[Time[1]])+' '+str(Time[3])+' '+str(Time[4])
#    print('SecToDate 1\n')
#    print('times: {}\n'.format(date))
#    return date

def SecToDate(sec, delta=60*60*3):
#    print('SecToDate 1\n')
    Time=ctime(sec+delta).split()
#    print('SecToDate 1\n')
    today=ctime(time()+delta).split()
#    print('SecToDate 1\n')
    if days[Time[0]]==days[today[0]] and Time[2]==today[2] and months[Time[1]]==months[today[1]] and Time[4]==today[4]:
        date='Сегодня в '+Time[3]

    elif Time[4]==today[4] and ((int(today[2])-int(Time[2]))==1) and months[Time[1]]==months[today[1]]:
        date='Вчера в '+str(Time[3])

    elif weeknumb[days[today[0]]]-weeknumb[days[Time[0]]]>1 and today[2]-Time[2]<7and Time[4]==today[4]:
        date=str(weekcase[days[Time[0]]])+' в '+str(Time[3])

    elif Time[4]==today[4]:
        date=str(days[Time[0]])+' '+str(Time[2])+' '+str(months[Time[1]])+' '+str(Time[3])

    else:
        date=str(days[Time[0]])+' '+str(Time[2])+' '+str(months[Time[1]])+' '+str(Time[3])+' '+str(Time[4])

#    print('SecToDate 1\n')
#    print('times: {}\n'.format(date))
    return date