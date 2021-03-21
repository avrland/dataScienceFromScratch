import feedparser
import sys
import random

rss_chans = [
    "http://fakty.interia.pl/feed",
    "http://rss.gazetaprawna.pl/GazetaPrawna",
    "http://fakty.interia.pl/polska/feed",
    "http://fakty.interia.pl/swiat/feed",
    "http://fakty.interia.pl/nauka/feed",
    "http://fakty.interia.pl/felietony/feed",
    "http://on.interia.pl/feed",
    "http://film.interia.pl/feed",
    "https://biznes.interia.pl/podatki/feed",
    "https://www.tvn24.pl/najnowsze.xml",
    "https://www.tvn24.pl/najwazniejsze.xml"
    "https://eurosport.tvn24.pl/sport,81,m.xml",
    "https://www.tvn24.pl/wiadomosci-z-kraju,3.xml",
    "https://www.tvn24.pl/wiadomosci-ze-swiata,2.xml",
    "https://www.tvn24.pl/biznes-gospodarka,6.xml",
    "https://www.tvn24.pl/pogoda,7.xml",
    "https://www.tvn24.pl/kultura-styl,8.xml",
    "https://www.polsatnews.pl/rss/wszystkie.xml",
    "https://www.polsatnews.pl/rss/polska.xml",
    "https://www.polsatnews.pl/rss/swiat.xml",
    "https://www.polsatnews.pl/rss/wideo.xml"
]
file_object = open('titles.txt', 'a')
x = 0
for rss in rss_chans:
    feed = feedparser.parse( rss )
    feed_len = len(feed.entries)
    for var in range(0, feed_len):
        single_article = feed.entries[var]
        print(single_article.title)
        file_object.write('\n' + single_article.title)
        x = x + 1

file_object.close()

print (x)