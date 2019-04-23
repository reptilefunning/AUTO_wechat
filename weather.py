import requests
from lxml import etree
import json

class WeatherSpider():
	def __init__(self,citynum):
		self.url = 'http://www.weather.com.cn/weather/'+citynum+'.shtml'
		self.url1 = 'http://www.weather.com.cn/weather1d/'+citynum+'.shtml'
		self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"}

	def parse_url(self): 
		response = requests.get(self.url,headers=self.headers)
		response1 = requests.get(self.url1,headers=self.headers)
		return response.content,response1.content
	def get_content(self, html_str):
		html = etree.HTML(html_str)
		# print(html)
		weather_ts = html.xpath("//div[@id='7d']/ul") 
		today_w = ''
		tomorrow_w = ''
		for weather_t in weather_ts:
			today_w += weather_t.xpath("./li[1]/h1/text()")[0] + ' '
			today_w += weather_t.xpath("./li[1]/p[1]/text()")[0] + ' '
			today_w += weather_t.xpath("./li[1]/p[2]/i/text()")[0] + ' '
			today_w += '风向' + weather_t.xpath("./li[1]/p[3]/i/text()")[0]
			tomorrow_w += weather_t.xpath("./li[2]/h1/text()")[0] + ' '
			tomorrow_w += weather_t.xpath("./li[2]/p[1]/text()")[0] + ' '
			tomorrow_w += '风向' + weather_t.xpath("./li[2]/p[3]/i/text()")[0]
		all_w = today_w + '--' + tomorrow_w

		
		return all_w
	def get_content1(self, html_str):
		html = etree.HTML(html_str)
		living_ins =html.xpath("//div[@class='livezs']/ul")
		today_living = ''
		for living_in in living_ins:
			today_living += living_in.xpath("./li[1]/span/text()")[0]
			today_living += living_in.xpath("./li[1]/em/text()")[0] + ':'
			today_living += living_in.xpath("./li[1]/p/text()")[0] + ' '
			today_living += living_in.xpath("./li[2]/a/em/text()")[0] + ' '
			today_living += living_in.xpath("./li[2]/a/p/text()")[0] + ' '
			today_living += living_in.xpath("./li[3]/em/text()")[0] + ':'
			today_living += living_in.xpath("./li[3]/p/text()")[0] + ' '
			today_living += living_in.xpath("./li[4]/a/em/text()")[0] + ' '
			today_living += living_in.xpath("./li[4]/a/p/text()")[0] + ' '
			today_living += living_in.xpath("./li[6]/em/text()")[0] + ':'
			today_living += living_in.xpath("./li[6]/p/text()")[0]
		return today_living
	def run(self):
		html_str,html_str1 = self.parse_url()
		all_w = self.get_content(html_str)
		all_l = self.get_content1(html_str1)
		return all_w+'\n今日: ('+all_l+')'
		
if __name__ == '__main__':
	Wspider = WeatherSpider(" ")
	Wspider.run()
