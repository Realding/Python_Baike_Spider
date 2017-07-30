# _*_ coding:utf-8 _*_
import url_manager
import html_downloader
import html_parser
import html_outputer

class SpiderMain(object):
	def __init__(self):
		self.urls = url_manager.Url_Manager()
		self.downloader = html_downloader.Html_Downloader()
		self.parser = html_parser.Html_Parser()
		self.outputer = html_outputer.Html_Outputer()

	def craw(self, root_url):
		count = 1
		self.urls.add_new_url(root_url)
		while self.urls.has_new_url():
			try:
				new_url = self.urls.get_new_url()
				print 'craw %d : %s' % (count, new_url)
				html_cont = self.downloader.download(new_url)
				new_urls, new_data = self.parser.parse(new_url, html_cont)
				self.urls.add_new_urls(new_urls)
				self.outputer.collect_data(new_data)

				if count == 1000:
					break
				count += 1
			except:
				print 'craw failed'

		self.outputer.output_html()

if __name__ == "__main__":
	# root_url = "https://baike.baidu.com/item/android/60243"
	root_url = "https://baike.baidu.com/item/python"
	obj_spider = SpiderMain()
	obj_spider.craw(root_url)
