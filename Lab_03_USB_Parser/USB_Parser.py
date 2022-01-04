import datetime

if __name__ == "__main__":
    file = "setupapi.dev.log"
    with open (file) as inputFile:
        for line in inputFile:
            if 'Device Install (Hardware initiated) - SWD' in line:
                nextLine = next(inputFile)
                
                info = line.split('#')
                deviceInfo = info[1].split('&')
                time = nextLine.split(' ')
                timeFormat = time[5].split('.')
                dateTime = time[4] + " " + timeFormat[0]

                timeInfo = datetime.datetime.strptime(dateTime, '%Y/%m/%d %H:%M:%S')

                timeCompare = datetime.datetime(2021, 4, 8, 22, 0, 0)
                
                if(timeInfo >= timeCompare):
                
                    print(deviceInfo)
                    print('Date:', timeInfo.date())
                    print('Time:', timeInfo.time())
                    print('Date-time:', timeInfo)

                    print()

               
