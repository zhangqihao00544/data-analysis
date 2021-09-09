import random

import requests

def download():
    url = 'https://www.kaggle.com/requests/GetDataViewExternalRequest'
    uas = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38',
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    ]
    headers = {
        'User-Agent': random.choice(uas),
        'Referer': 'https://www.kaggle.com/giripujar/hr-analytics'
    }
    r = requests.get(url=url, headers=headers)
    try:
        r.raise_for_status()
        return r.text
    except Exception:
        return 'j'

if __name__ == '__main__':
    data = download()
    print(data)
    print('hh')