# Covid19Spiders
A scrapy spider that crawl data of Canadian covid-19 information. #scrapy
**Note**: the program is **NOT yet** completed.

## Requirement 
Docker is needed to install splash.

## Installation
Get splash and run it in Docker
`$ pip install scrapy-splash`
`docker run -d -p 8050:8050 scrapinghub/splash`

## Configuration
Already done! But here are the added-ons.

Add following things in the _setting.py_ in your scrapy project:
`SPLASH_URL = 'http://localhost:8050'
DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}
  SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'`

## Run
First, you need go to your program folder.
`cd path/covid19Info`
Use this command to run the program.
`scrapy crawl covid19_tablets`
Then, you'll see the json file in this folder.
