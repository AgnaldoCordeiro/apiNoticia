import scrapy


class CNNSpider(scrapy.Spider):
    name = 'G1'
    allowed_domains = ['www1.folha.uol.com.br']
    start_urls = ['https://www1.folha.uol.com.br/ultimas-noticias/']

    def parse(self, response):        

        for noticias in response.css(".c-headline--newslist"):
            yield{
            'title': noticias.css('.c-headline__title ::text').get().extract_first(),
            'subtitulo': noticias.css('.c-headline__standfirst ::text').get().extract_first(),
            'url': noticias.css('.c-image-aspect-ratio__link ::attr(href)').extract(),
            'data': noticias.css('.c-headline__dateline ::text').get().extract_first(),
            'image_url': noticias.css('.c-image-aspect-ratio__image ::attr(src)').get().extract(),        



            }
    