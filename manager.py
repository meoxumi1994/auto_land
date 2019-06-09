import statistics 
from model import batdongsan_crawler_col

visualizer_data = dict()


def get_sorted_mean_price(titles):
	def check_titles(_sub_title):
		for tit in titles:
			if tit not in _sub_title:
				return False
		return True

	for data in batdongsan_crawler_col.find({}):
		sub_title = data.get('sub_title')
		area = data.get('area')
		price = data.get('price')

		key = sub_title

		if not check_titles(sub_title):
			continue

		if area > 0:
			value = price / area

			cur_data = visualizer_data.get(key, [])
			cur_data.append(value)

			visualizer_data[key] = cur_data
		

	for key, val_list in visualizer_data.items():
		visualizer_data[key] = int(statistics.mean(val_list))

	sorted_data_list = sorted(visualizer_data.items(), key=lambda kw : kw[1])

	return sorted_data_list