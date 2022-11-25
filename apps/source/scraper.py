import scrapy
from scrapy.crawler import CrawlerProcess

from apps.product.models import Product
from apps.source.models import Source


class ProductSpider(scrapy.Spider):
    name = "product scrap"
    base_url = ""

    # this is what start_urls does
    def start_requests(self):
        # taking only the url from the database
        # TODO:: need to make it generic so that multiple source can be handled
        source = Source.objects.first()
        self.base_url = source.url
        yield scrapy.Request(url=self.base_url, callback=self.parse)

    def parse(self, response):
        data = response.css("div.container-col-links")

        links = []
        for line in data:

            hrefs = line.css("a")
            for href in hrefs:
                category_url = self.base_url + href.css("a").attrib['href']
                links.append(category_url)
        # print(links)
        yield from response.follow_all(links, self.parse_product_url)

    def parse_product_url(self, response):
        data = response.css("div.product__list--item")
        for line in data:
            product_link = self.base_url + line.css("div.product-box").attrib['data-url']
            yield response.follow(product_link, self.parse_product_details)

    def parse_product_details(self, response):
        data = response.css("div.product-description")
        product_summary = data.css("div.description-block").css("li *::text").getall()
        product_summary = {i: summary for i, summary in enumerate(product_summary, start=1)}
        product_data = {
            "title": data.css("h1::text").extract_first(),
            "price": data.css("span.item.price").css("span::text").extract_first(),
            "currency": data.css("span.item.price").css("small::text").extract_first(),
            "summary": product_summary
        }
        product = Product.objects.update_or_create(title=product_data["title"], defaults=product_data)
