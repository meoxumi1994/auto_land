# -*- coding: utf-8 -*-
import time
import datetime
import re


def get_words_and_number_from_text(text):
	return re.sub('[^0-9a-zA-Z ]+', '', text)


def get_number_from_text(text):
	return float(re.sub('[^0-9.]+', '', text) or 0)


s1 = u'ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ'
s0 = u'AAAAEEEIIOOOOUUYaaaaeeeiioooouuyAaDdIiUuOoUuAaAaAaAaAaAaAaAaAaAaAaAaEeEeEeEeEeEeEeEeIiIiOoOoOoOoOoOoOoOoOoOoOoOoUuUuUuUuUuUuUuYyYyYyYy'


def get_english_words(text):
	english_words = "".join([s0[s1.index(c)] if c in s1 else c for c in text])
	return get_words_and_number_from_text(english_words.lower())

def str_to_ts(str, format):
	""" format like '%d/%m/%Y' """
	return time.mktime(datetime.datetime.strptime(str, format).timetuple())
