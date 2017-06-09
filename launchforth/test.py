from datetime import datetime
import re
import json

pattern = '\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\d'

m = re.search(pattern, "2017-06-01T03:06:53.888017Z")
# print m.group(0)


def substitute_date(v, j=None, k=None):
    if isinstance(v, dict):
        for key, val in v.iteritems():
            substitute_date(val, v, key,)
        return
    if isinstance(v, list):
        for i in range(len(v)):
            substitute_date(v[i])
        return 
    if not isinstance(v, basestring):
        return
    m = re.search(pattern, v)
    if m:
        j[k] = datetime.strptime(m.group(0), '%Y-%m-%dT%H:%M:%S')
    return

        # print v
        # print m.group(0)

with open('test.json') as file:
    data = json.load(file)
    # substitute_date(data)
    # print type(data[u'results'][0][u'created'])
    print len(data)
    for key in data.keys():
        print '"' + key + '"'
        



