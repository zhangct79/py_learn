import requests

r = requests.get('https://www.douban.com/') # 豆瓣首页
print(r.status_code)
print(r.text)

#直接获取json类型数据
r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
r.json()


#需要传入HTTP Header时，我们传入一个dict作为headers参数：
r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})

#cookie
r.cookies['ts']

#上传文件
url = ""
upload_files = {'file': open('report.xls', 'rb')}
r = requests.post(url, files=upload_files)