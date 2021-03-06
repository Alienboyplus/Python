import urllib.request
import re

def getHttp(url):
	h = urllib.request.urlopen(url)
	html = h.read()
	return html

def downloadImg(html):
	#可以根据需要来改变正则表达式
	reg = r'_src=".*?\.jpg"'
	imgre=re.compile(reg)
	urls = imgre.findall(html)
	x = 0
	for url in urls:
		#可以根据需要来修改步长，这里为[6:-1]
		urllib.request.urlretrieve(url[6:-1],'D:/script/%s.jpg'%x)
		x += 1

def main():
	#可以根据需要来更换域名，这里以'http://www.lenovo.com.cn'来举例
	html = getHttp('http://www.lenovo.com.cn').decode('UTF-8')
	downloadImg(html)

if __name__ == '__main__':
	main()
	print("done!")