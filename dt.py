import urllib.request

GOOGLE_TOCKEN = ''
raw = urllib.request.urlopen("https://script.google.com/macros/s/{}/exec".format(GOOGLE_TOCKEN))
contents = raw.read()
end = contents.decode().split('\n')
tab = []
for i, record in enumerate(end):
    if record != '':
        record = record.split('\t')
        subarray = record[0].split(' ')
        record.pop(0)
        for item in reversed(subarray):
            record.insert(0, item)
        tab.append(record)

print(tab)
