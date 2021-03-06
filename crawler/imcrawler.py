'''

작성자 : 류현준
작성일 : 2017-08-20
설 명 : 엑셀로 사진을 받아서 그림을 다운받음
변수  : argv[1] (이미지 받을 root dir)
	   argv[2] (엑셀 파일 위치)

install package : xlrd, icrawler

pip3 install icrawler
pip3 install xlrd

'''
#-*- coding: utf-8 -*-

import sys
from icrawler.builtin import GoogleImageCrawler
import xlrd

def getPoliticianImage():

	# image path : first argument
	image_path = sys.argv[1]

	# excel path : second argument
	excel_path = sys.argv[2]

	# max number of image : third argument
	max_num_image = int(sys.argv[3])

	excelFile = xlrd.open_workbook(excel_path)
	politician_key_value_list = excelFile.sheet_by_index(0)

	for i in range(0, politician_key_value_list.nrows):

		# folder name (politician english name)
		folder_name = politician_key_value_list.cell_value(i, 1)

		# directory which you can put
		total_path = image_path + '/' + folder_name

		google_crawler = GoogleImageCrawler(parser_threads=2, downloader_threads=8,
			storage={'root_dir': total_path})

		google_crawler.crawl(keyword=politician_key_value_list.cell_value(i, 0), offset=0, max_num = max_num_image,
							date_min=None, date_max=None, min_size = (200, 200), max_size = None)

def main():
	getPoliticianImage()

if __name__ == '__main__':
	main()