import urequests
import ntptime
import utime
from gcalendar import Gcalendar
import machine, neopixel

GOOGLE_TOCKEN = '<tocken>'
NP = neopixel.NeoPixel(machine.Pin(13), 8)


def datetime_formatted():
    '''
    input data format:
        utime.localtime(ntptime.time())
        (2019, 4, 6, 14, 32, 50, 5, 96)
        (YEAR, M, D, TT, MM, SS, w, dy)
    Format the data and time to look like in
    google calendar for easies comparison:
        'Sun',  'Apr',  '07',  '2019',  '08:00:00', 'GMT+0300'
    '''
    day = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
    mon = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

    t = utime.localtime(ntptime.time())
    now = []
    now.append(day[t[6]])                       #add wekday
    now.append(mon[t[1]-1])                     #add mount
    if t[2] < 10:
        now.append('0{}'.format(t[2]))          #add date
    else:
        now.append(t[2])                        #add date
    now.append('{}'.format(t[0]))               #add year
    # TODO: add nice timezone correction
    if t[4] < 10:
        now.append('{}:0{}:00'.format(t[3]+3, t[4])) #add time
    else:
        now.append('{}:{}:00'.format(t[3]+3, t[4]))  #add time

    return now

def check_events():

    cal = Gcalendar(GOOGLE_TOCKEN)
    events = cal.get()

    dt = datetime_formatted()

    for i, event in enumerate(events):
        if i < 8:
            if event[:5] == dt:
                print('{}\t\tequal to {}'.format(event[:5], dt))
                print("An event is comming!")
                NP[i] = (0,255,0, 128)
            else:
                print('{}\t\tNOT equal to {}'.format(event[:5], dt))
                NP[i] = (255,0,0, 128)
            NP.write()

    gotosleep(1)

def gotosleep(time = 1):
    rtc = machine.RTC()
    rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)

    # set RTC.ALARM0 to fire after 'time' seconds (waking the device)
    rtc.alarm(rtc.ALARM0, time*60000)

    # put the device to sleep
    machine.deepsleep()
