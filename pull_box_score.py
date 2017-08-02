#!/usr/bin/env python2

from bs4 import BeautifulSoup
import requests 

#### FIRST THREE YEARS 2010/2011/2012 ARE DIFFERENT WAYS TO RETRIEVE THAN 13-17

class Old_Stats:
	'Retrieve the mens volleyball statistics data from years 2010, 2011, 2012 for MAMVIC NAIA Cardinal Stritch' 

# return list of years of stat data
	def years(self):
	
		start_year = 2010
		end_year = 2012

		yearl = []
		for year in range(start_year, end_year + 1):
			yearl.append(year)
		return yearl

	def base_urls(self):
		self.sport_url = '/teamstat.htm?path=mvball'
		base_urll = []
		for year in range(0, len(self.years())):
			self.base_url = 'static.stritchwolves.com/custompages/MVB/' + str(self.years()[year])  
			base_urll.append(self.base_url + self.sport_url)
		return base_urll

	def get_box_score_links(self):
		
		link_list = []
		
		for url_step in range(0, len(self.base_urls())):
			r = requests.get('http://' + self.base_urls()[url_step])
			data = r.text
			soup = BeautifulSoup(data, 'lxml')
			for link in soup.find_all('a'):
				link_list.append('http://' + self.base_urls()[url_step].replace(self.sport_url, '') + '/' + link.get('href'))
		return link_list

	def download_html_links(self):
		for url_step in range(0, len(self.get_box_score_links()) + 1):
			filename = 'box_score' + str(url_step) + '.htm'
			response = requests.get(self.get_box_score_links()[url_step])
			with open('./data/' + filename, "wb") as code:
				code.write(response.content)
