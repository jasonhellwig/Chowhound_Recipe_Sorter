# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ChowSortPipeline(object):
    def process_item(self, item, spider):
        if item['name']:
            item['name'] = item['name'][0].strip()
            item['votes'] = int(item['votes'][0].split()[0])
            item['link'] = item['link'][0].strip()
            return item
