# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class ApinoticiaPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("myapinoticia.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS noticia_tb""")
        self.conn.execute("""create table noticia_tb(
    title text, 
    subtitulo text,
    url text,
    data text,
    image_url text
)""")

    def process_item(self, item, spider):
        self.store_db(item)       
        return item
    
    def store_db(self, item):
        self.curr.execute("""insert into noticia_tb values (?,?,?,?,?)""",(str(item['title'][0]),str(item['subtitulo'][0]),str(item['url'][0]),str(item['data'][0]),str(item['image_url'][0])))              
        self.conn.commit()
