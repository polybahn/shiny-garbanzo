from scrapy import Spider
from scrapy import Request
from scrapy.conf import settings
from launchforth.items import LaunchforthItem
from datetime import datetime
import re
import json


def extract_json(resp):
    return json.loads(resp.body_as_unicode()[9:-2].encode('utf-8'))

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
    m = re.search('\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\d', v)
    if m:
        j[k] = datetime.strptime(m.group(0), '%Y-%m-%dT%H:%M:%S')
    return
    
class launchforthSpider(Spider):
    name = 'launchforth'
    allowed_domains = [settings['DOMAIN']]
    start_urls = [settings['PREFIX']+ settings['MONGODB_COLLECTION'] + '/']


    def parse(self, response):
        d = extract_json(response)
        substitute_date(d)
        results = d['results']
        # set primary Id for each content dict object. Then pack them as an Item to store in MongoDB
        for result in results:
            if self.settings['ID_KEY'] in result:
                result[u'_id'] = result[self.settings['ID_KEY']]
        item = LaunchforthItem()
        item['content'] = results
        yield item
        # extract next url to crawl
        if 'next' in d and d['next'] != 'null':
            yield Request(url=d['next'], callback=self.parse)
