from __future__ import absolute_import

import time

from celery import shared_task
from scrapy.crawler import CrawlerProcess

from apps.source.scraper import ProductSpider


@shared_task(name='scrap_product')
def scrap_product():
    process = CrawlerProcess()

    process.crawl(ProductSpider)
    process.start()
