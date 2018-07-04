import scrapy

class LanguageSpider(scrapy.Spider):
    name = "language"
    start_urls = [
        'https://www.bible.com/bible/12/JHN.1.asv?parallel=1861',
        ]
    def parse(self, response):
        for num in range(1, 179):
            dat = response.css('span[class="verse v{0}"]'.format(num))
            if len(dat) != 0:
                eng = dat[0].css('span.content::text').extract()
                twi = dat[1].css('span.content::text').extract()
                yield {
                    'English': eng,
                    'Twi': twi
                }
        for a in response.css('div.next-arrow a'):
            yield response.follow(a, callback=self.parse)
