from crawler import CrawlerBase

from utils import get_english_words
from utils import get_words_and_number_from_text
from utils import get_number_from_text
from utils import str_to_ts


class BatDongSanCrawler(CrawlerBase):
	_URL = 'https://batdongsan.com.vn/'

	@classmethod
	def _get_next_urls(cls, parsed_html):
		results = parsed_html.body.findAll('div', attrs={'class':'p-title'})
		return [
			cls._URL + res.find('a')['href']
			for res in results if res
		]

	@classmethod
	def _is_exist_data(cls, parsed_html):
		results = parsed_html.body.findAll('span', attrs={'class':'gia-title'})
		return bool(results and cls.price(parsed_html))

	@classmethod
	def price(cls, parsed_html):
		results = parsed_html.body.findAll('span', attrs={'class':'gia-title'})
		text = results[0].find('strong').text

		clean_text = get_words_and_number_from_text(text)
		price = get_number_from_text(text)

		if 'triu' in clean_text:
			return int(price * 1000)
		if 't' in clean_text:
			return int(price * 1000000)
		return int(price)

	@classmethod
	def area(cls, parsed_html):
		results = parsed_html.body.findAll('span', attrs={'class':'gia-title'})
		text = results[1].find('strong').text

		clean_text = get_words_and_number_from_text(text)
		area = get_number_from_text(text)
		return int(area)

	@classmethod
	def sub_title(cls, parsed_html):
		results = parsed_html.body.findAll('span', attrs={'class':'diadiem-title'})
		return get_english_words(results[0].text)

	@classmethod
	def from_time(cls, parsed_html):
		results = parsed_html.body.findAll('div', attrs={'style':'width: 175px'})
		raw_time = get_number_from_text(results[0].text)
		time = str_to_ts(str(int(raw_time)), "%d%m%Y")
		print(time)
		return time

	@classmethod
	def address(cls, parsed_html):
		results = parsed_html.body.findAll('div', attrs={'id':'LeftMainContent__productDetail_contactAddress'})
		if not results:
			return ""
		return get_english_words(results[0].find('div', attrs={'style':'text-transform:capitalize;'}).text)

