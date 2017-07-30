# _*_ coding:utf-8 _*_


class Html_Outputer(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.datas = []
		
	
	def collect_data(self,data):
		if data is None:
			return
		self.datas.append(data)


	def output_html(self):

		fout = open('output.html','w')

		fout.write("<head><meta http-equiv='content-type' content='text/html;charset=\'utf-8\'>")
		fout.write("<html>")
		fout.write("<body>")
		fout.write("<table border = '1'>")

		for data in self.datas:
			fout.write("<tr>")
			# <a href="/tags/tag_table.asp">&lt;table&gt;</a>
			fout.write("<td>")
			fout.write("<a href = \"%s\">" % data['url'].encode('utf-8'))
			fout.write("%s</a></td>" % data['title'].encode('utf-8'))
			# fout.write("</tr>")
			# fout.write("<tr>")
			fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
			fout.write("</tr>")

		fout.write("</table>")
		fout.write("</body>")
		fout.write("</html>")

		fout.close()