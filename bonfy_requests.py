# -*- coding: utf-8 -*-

"""
对 requests 的封装
"""

# 请先安装requests
# pip install requests

import random
import requests
from requests.exceptions import ConnectionError, Timeout


def requests_get(url, **kwargs):
    USER_AGENTS = (
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100 101 Firefox/22.0',
        'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0',
        ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) '
         'Chrome/19.0.1084.46 Safari/536.5'),
        ('Mozilla/5.0 (Windows; Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46'
         'Safari/536.5')
    )
    try:
        r = requests.get(
            url,
            timeout=30,
            headers={'User-Agent': random.choice(USER_AGENTS)},
            **kwargs
        )
    except ConnectionError:
        print('Network connection failed.')
    except Timeout:
        print('timeout.')
    return r
