import requests

#reuqest模块中，参数都以字典的形式传递
params={'email':'1582500170@qq.com',
        'password':'Luht@11223344',
        'remember': '0'}
url = 'https://www.ketangpai.com/UserApi/login'
res = requests.post(url,data = params)
#使用 json 参数直接传递，然后它就会被自动编码
# res = requests.post(url,json = params)
print(res)
#响应头信息
print('响应头',res.headers)

#返回状态码
print('状态码',res.status_code)
# 内置的状态码查询对象
print(res.status_code == requests.codes.ok)
#抛出异常
print(res.raise_for_status())
#响应报文,返回数据  格式为str
#test可显示html，json，xml格式的数据
print('响应报文',res.text)
print(res.content)
#响应报文json，返回数据格式为dict
#仅限返回数据格式为json时，返回json
print('响应报文',res.json())
print('响应报文',res.json()['info'])

#获取cookie
print('cookies',res.cookies)