from datetime import datetime
import time

start_time = time.time()


class InitTimeObject:
    def __init__(self) -> None:
        '''
        Forever loop Long-Running Time Object
        '''
        self.stime = datetime.now().time()
        self.setCurrentTime()

    def setCurrentTime(self) -> None:
        '''
        Set global time to current time

        :return:
        '''
        global start_time
        self.start_time = time.time()

    def getTimePC(self) -> str:
        '''
        Make a string of absolute time hh:mm:ss

        :return:
        '''
        self.stime = datetime.now().time()
        stime = self.stime
        if stime.second % 2 == 0:
            timestp = str('%02d' % stime.hour) + ' ' + str('%02d' % stime.minute) + \
                      ' ' + str('%02d' % stime.second)
        else:
            timestp = str('%02d' % stime.hour) + ':' + str('%02d' % stime.minute) + \
                      ':' + str('%02d' % stime.second)
            # + '.' + str(stime.microsecond)[0:2]
        time.sleep(1)
        return timestp

    def getTimeElapsed(self) -> str:
        '''
        Make a string of relative time hh:mm:ss

        :return:
        '''
        delta = time.time() - self.start_time
        second = delta % 60
        microsecond = str(datetime.now().time().microsecond)[0:2]
        minute = delta // 60
        minute = minute % 60
        hour = minute // 60

        if int(second) % 2 == 0:
            timestp = str('%02d' % hour) + ' ' + str('%02d' % minute) + \
                      ' ' + str('%02d' % second)
        else:
            timestp = str('%02d' % hour) + ':' + str('%02d' % minute) + \
                      ':' + str('%02d' % second)
        time.sleep(0.5)

        return timestp


if __name__ =='__main__':
    pass
