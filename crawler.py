import requests
from bs4 import BeautifulSoup


HEADERS = {
	'USER-AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
}

class CrawlerBase(object):
	"""all paramse using parsed_html from BeautifulSoup"""
	_URL = None  # base url

	def __init__(self):
		self.queue = [self._URL]
		self.crawled_urls = set()

	def get_next_data(self):
		url = self.queue.pop(0)
		if not url or url in self.crawled_urlss:
			return None

		req = requests.get(url=url, headers=HEADERS)
		parsed_html = BeautifulSoup(req.text)

		next_urls = self._get_next_urls(parsed_html)
		self.queue.extend(next_urls)

		data = self._get_data(parsed_html)
		if not data:
			return self.get_next_data()

		data['url'] = url
		return data

	@classmethod
	def _get_data(cls, parsed_html):
		if not cls._is_exist_data(parsed_html):
			return None

		result = dict()
		for method, clm in cls.__dict__.items():
			if method[0] != '_':
				func = getattr(cls, method)
				result[method] = func(parsed_html)

		return result

	@classmethod
	def _get_next_urls():  # all next urls
		return []

	@classmethod
	def _is_exist_data():  # check if this page is accept for crawler
		return True












