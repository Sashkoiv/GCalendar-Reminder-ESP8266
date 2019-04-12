import urequests


class Gcalendar():
    def __init__(self, tocken):
        if len(tocken) == 55:
            self._tocken = tocken
        else:
            raise ValueError('Wrong tocken')

    def get(self):
        return self._convert_data()

    def _get_data(self):
        _raw = urequests.get("https://script.google.com/macros/s/{}/exec".format(self._tocken))
        return _raw.text

    def _convert_data(self):
        _contents = self._get_data()
        _records = _contents.split('\n')
        _events_list = []
        for record in _records:
            if record != '':
                record = record.split('\t')
                # format start date
                start_date = record[0].split(' ')
                record.pop(0)
                for item in reversed(start_date):
                    record.insert(0, item)
                _events_list.append(record)
                # format end date
        return _events_list
