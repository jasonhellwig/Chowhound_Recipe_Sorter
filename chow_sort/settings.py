# -*- coding: utf-8 -*-

# Scrapy settings for chow_sort project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'chow_sort'

SPIDER_MODULES = ['chow_sort.spiders']
NEWSPIDER_MODULE = 'chow_sort.spiders'

ITEM_PIPELINES = {'chow_sort.pipelines.ChowSortPipeline': 0, }

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'chow_sort (+http://www.yourdomain.com)'
