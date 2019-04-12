import urllib.request
from datetime import datetime as dt

class Gcalendar():
    def __init__(self, tocken):
        if len(tocken) == 55:
            self._tocken = tocken
        else:
            raise ValueError('Wrong tocken')

    def get(self):
        return self._convert_data()

    def _get_data(self):
        _raw = urllib.request.urlopen("https://script.google.com/macros/s/{}/exec".format(self._tocken))
        # print(_raw.read())
        return _raw.read().decode()

    def _convert_data(self):
        _contents = self._get_data()
        _records = _contents.split('\n')
        _events_list = []

        # Format an event list with separated values and understandable structure
        for record in _records:
            if record != '':
                record = record.split('\t')
                # subarray = record[0].split(' ')
                # record.pop(0)
                # for item in reversed(subarray):
                #     record.insert(0, item)
                _events_list.append(record)

        # Convert start datetime and end datateime to datetime structure
        for _event in _events_list:
            start_datetime = _event.pop(0)      # take first item, delete it and shift the array
            finish_datetime = _event.pop(0)     # take first item, delete it and shift the array

            # start_datetime = dt.strptime('Thu Apr 18 2019 19:21:13 GMT+0300', '%a %b %d %Y %H:%M:%S %Z')
            start_datetime = dt.strptime(start_datetime, '%a %b %d %Y %H:%M:%S %Z')
            finish_datetime = dt.strptime(finish_datetime, '%a %b %d %Y %H:%M:%S %Z')
        return _events_list

if __name__ == "__main__":
    calendar = Gcalendar('<tocken>')
    from pprint import pprint as print
    print(calendar.get())
