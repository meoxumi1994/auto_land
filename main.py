from batdongsan_crawler import BatDongSanCrawler
from model import batdongsan_crawler_col


batdongsan_crawler = BatDongSanCrawler()


for _ in range(1000):
	data = batdongsan_crawler.get_next_data()

	if not batdongsan_crawler_col.find_one({ "url": data["url"]}):
		x = batdongsan_crawler_col.insert_one(data)
		
