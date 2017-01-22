import subprocess
import sys

# some code here

#pid = subprocess.call(["scrapy", 'crawl', 'funny2'])
#pid = subprocess.call(["scrapy", 'crawl', 'jokes_crawler','-o','items.json','-t','json'])
pid = subprocess.call(["scrapy", 'crawl', 'funny2','-o','items_funny2.json','-t','json'])