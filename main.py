import urequests

GOOGLE_TOCKEN = ''
r = urequests.get('https://script.google.com/macros/s/{}/exec'.format(GOOGLE_TOCKEN))
print(r.text)

array = r.text.split(' ')
print(array)