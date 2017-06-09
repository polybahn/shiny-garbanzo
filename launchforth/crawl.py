# Ths script doesn't work

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


s = get_project_settings()
s['MONGODB_COLLECTION'] = 'content'
s['ID_KEY'] = 'content_id'

proc = CrawlerProcess(s)
# 'followall' is the name of one of the spiders of the project.
process.crawl('launchforth',custom_settings=s)
process.start()