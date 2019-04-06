import requests
from retrying import retry
from fake_useragent import UserAgent

# 重新启动3次
@retry(stop_max_attempt_number=3)
def _getUrlPage(url, verify_ssl=False, page_decode='utf-8'):
    '''
    reutn page(utf8)
    '''
    # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}
    headers={"User-Agent":UserAgent().random}
    r = requests.get(url, headers=headers, timeout=5)
    assert r.status_code == 200
    return r.content.decode(page_decode)

def getUrlPage(url, verify_ssl=False, page_decode='utf-8'):
    try: 
        html_str = _getUrlPage(url, verify_ssl, page_decode)
    except:
        html_str = None
    return html_str



if __name__ == "__main__":
    a = getUrlPage("http://www.163.com", page_decode='gbk')
    print(a)