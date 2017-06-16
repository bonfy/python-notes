# Web Scraping with Python

这本书的中文译本名称为 《Python 网络数据采集》,作者 Ryan Mitchell， 据说 2017.11 将有2nd Edition

## 笔记

我可能自己有长时间的网站爬取经验，的确如果在以前没有自己玩过爬虫前看这本书，入门还是比较好的，但是如果有经验的话，这本书就可以快速的过一遍了

不过即使是快速过一遍，有些东西还是很有价值的

### 登陆处理cookie

基本的读取cookie, 然后将cookie 作为参数放进requests请求

```python
import requests
params = {'username': 'Ryan', 'password': 'password'}

r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
print("Cookie is set to:")
print(r.cookies.get_dict())
print("-----------")
print("Going to profile page...")
r = requests.get("http://pythonscraping.com/pages/cookies/profile.php",
                      cookies=r.cookies)
print(r.text)
```

如果你面对的网站比较复杂，它经常暗自调整 cookie，或者如果你从一开始就完全不想要用 cookie，该怎么处理呢? Requests 库的 session 函数可以完美地解决这些问题:

```python
import requests
session = requests.Session()
params = {'username': 'username', 'password': 'password'}
s = session.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
print("Cookie is set to:")
print(s.cookies.get_dict())
print("-----------")
print("Going to profile page...")
s = session.get("http://pythonscraping.com/pages/cookies/profile.php") print(s.text)

```

会话(session)对象(调用 requests.Session() 获取)会持续跟踪会话信 息，像 cookie、header，甚至包括运行 HTTP 协议的信息，比如 HTTPAdapter(为 HTTP 和 HTTPS 的链接会话提供统一接口)。


HTTP 接入认证

虽然这看着像是一个普通的 POST 请求，但是有一个 HTTPBasicAuth 对象作为 auth 参数传 递到请求中。显示的结果将是用户名和密码验证成功的页面(如果验证失败，就是一个拒绝接入页面)。
```python
import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('ryan', 'password')
r = requests.post(url="http://pythonscraping.com/pages/auth/login.php", auth=auth)
print(r.text)
```

### 登陆处理验证码

11.1.2 Tesseract 处理 OCR 解决验证码一段可以看下


## 写在最后

这本书入门还是不错的，但是如果更深入的话，希望着重讲下爬取同时爬取多个网站的设计方法
