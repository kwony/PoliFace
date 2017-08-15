#-*- coding: utf-8 -*-

from scrapy.selector import Selector
from bs4 import BeautifulSoup
import requests
import random
import urllib
import os, errno


def fetch_page(url):
	r = requests.get(url)
	html = r.text
	soup = BeautifulSoup(html, 'lxml')
	return soup.prettify('utf-8')

def img_link_from_url(url):
	html = fetch_page(url)
	sel = Selector(text=html)
	img_links = sel.css('.row .item .thumb::attr(href)').extract()
	return img_links

def img_from_link(url, num_pic):
	name = num_pic
	full_name = input + "/" + str(name) + ".jpg"

	try:
		url.encode('ascii')
	except UnicodeEncodeError:
		print(num_pic)
		return
	else:
		print("??")
		pass

	urllib.urlretrieve(url, full_name)

### Start ###


politician_list = ["심상정", "안희정"]

for poli in politician_list:

	input = poli
	bing = "http://www.bing.com/images/search?q=" + input + "&FORM=HDRSC2"

	num_pic = 1

	folder = poli
	if not os.path.exists(folder):
		os.makedirs(folder)

	for link in img_link_from_url(bing):
		img_from_link(link, num_pic)
		if num_pic >= 1000:
			break
		else:
			num_pic = num_pic + 1

	print("length : " + str(len(img_link_from_url(bing))))