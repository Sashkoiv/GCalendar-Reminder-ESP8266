# GCalendar-Reminder-ESP8266

Te device which is capable to receive Google calendar events and perform an action


[Very important information](https://github.com/mcauser/MicroPython-ESP8266-Nokia-5110-Bitcoin)

[Second importance](https://forum.micropython.org/viewtopic.php?t=5295)


```python
import urequests
r = urequests.get('https://script.google.com/macros/s/(token)/exec')
```

```sh
>>> import upip
>>> upip.install('micropython-urequests')
```

Did it install?
```sh
>>> import os
>>> os.listdir()
['boot.py', 'lib']
>>> os.listdir('lib')
['urequests.py']
```