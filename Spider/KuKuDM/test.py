from bs4 import BeautifulSoup
import urllib.request
from collections import OrderedDict
import urllib.request
import urllib.parse
import os
from multiprocessing import Pool,Manager
import queue
import time
import random
import socket
import gc

#Python beginner practise only.
#No commercial profit

UA_iphone_6p = "Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12A366 Safari/600.1.4"
episode_title = ""
parameter_global_js = OrderedDict({
    "server0": "http://n.1whour.com/",
    "server": "http://n.1whour.com/",
    "m200911d": "http://n.1whour.com/",
    "m201001d": "http://n.1whour.com/",
    "m201304d": "http://n.1whour.com/",
    "m2007": "http://n.1whour.com/",
})
# for each url in the home page list, do the following actions
url_demo = "http://m.kukudm.com/comiclist/6/42702/1.htm"
url_top_level_domain = "http://m.kukudm.com"
url_bleach_home_page = "http://m.kukudm.com/comiclist/6/"
crawler_max_count = 700


def get_pic_url_from_episode_url(dict_pic, url_episode):
    url_top_level_domain
    url_bleach_home_page
    UA_iphone_6p
    parameter_global_js

    time.sleep(1)
    url_req = urllib.request.Request(url_episode)

    url_req.add_header("User-Agent", UA_iphone_6p)
    url_req.add_header('Referer', 'https://www.baidu.com')

    print("start to open url : %s" % str(url_episode))
    html_episode = urllib.request.urlopen(url_req)

    print("Start to get BeautifulSoup from Html.")
    bs = BeautifulSoup(html_episode, "html.parser")
    html_episode.close()
    print("Got BeautifulSoup from Html.")

    for i in bs.body.find_all("script", {"language": "javascript"}):
        #print("entered for each JS, JS is %s" % i.get_text())

        txt_img = i.get_text().replace('''document.write("''', "")
        tag_img = BeautifulSoup(txt_img, "html.parser").find()

        url_download_pic = tag_img["src"].replace('''"''', "").replace("+", "")
        for _i in parameter_global_js:
            url_download_pic = url_download_pic.replace(str(_i), str(parameter_global_js[_i]))
            dict_pic[url_episode] = url_download_pic

        #check the next page
        url_next_page = bs.find("li",{"class":"last"}).a["href"]
        if url_next_page.find("exit.htm") == -1:
           get_pic_url_from_episode_url(dict_pic, url_top_level_domain +  url_next_page)
        else:
            return 0

def retry_urlretrieve(file_url, file_save_path, retry_cout):
    if retry_cout <= 0:
        raise EnvironmentError("Max retry meets.")
    try:
        print("start to save pic from img_url: %s" % file_url)
        urllib.request.urlretrieve(file_url, file_save_path)
        print("Finish to save pic from img_url: %s" % file_url)
        # sometimes I may get error like:
        # urllib.error.ContentTooShortError: <urlopen error retrieval incomplete: got only 4063 out of 159690 bytes>
        # so I want to re-try one time.
        # if failed again, then give up.
    except:
        print("Try urlretrieve again.")
        retry_cout -= 1
        retry_urlretrieve(file_url, file_save_path, retry_cout)


def save_pic_from_url_dict(dict_pic, folder_title):
    time.sleep(1)
    path_parent = "download/"
    try:
        if not os.path.exists(os.path.join(path_parent, folder_title)):
            os.makedirs(os.path.join(path_parent, folder_title))
    except  Exception as e:
            print("Error code is %s" % e.code)

    num = 1
    for item in dict_pic:
        time.sleep(2)
        img_url = urllib.request.quote(dict_pic[item], safe='/:?=')
        retry_urlretrieve(img_url, str(os.path.join(path_parent, folder_title))+"//%s.jpg" % num, 6)
        num += 1

def crawler_work(q):
    global crawler_max_count
    path_parent = "download/"

    if crawler_max_count <= 0:
        return 1
    try:
        dt = q.get_nowait()
        #debug code to ignore some pages
        #if dt[0] == "死神_第686话 感动完结" \
        #       or dt[0] == "死神_第685话 15年的相伴 下期完结!"\
        #       or dt[0] == "死神_第684话":
        #   return 1
    except Exception as e:
        print("Error code is %s" % e.code)
    else:
        url_episode = dt[1]
        folder_title = dt[0]

        # ignore existing folders
        if os.path.exists(os.path.join(path_parent, folder_title)):
            crawler_max_count -= 1
            print("path %s is already existed, so ignore it." % str(os.path.join(path_parent, folder_title)))
            return 1
        else:
            print("crawler_work for %s -> %s" % (url_episode, folder_title))

        url_download_pic_dic = OrderedDict()
        try:
            get_pic_url_from_episode_url(url_download_pic_dic, url_episode)
        except Exception as e:
            print("Error code is %s" % e.code)

        save_pic_from_url_dict(url_download_pic_dic, folder_title)
        crawler_max_count -= 1
        print("crawler_max_count is %s" % crawler_max_count)
        return 1
'''
def get_job_for_crawler(q):
    result = crawler_work(q)
    if result == 1:
        
        get_job_for_crawler(q)
    else:
        return 0
'''
def get_job_for_crawler(q):
    time.sleep(1)
    return crawler_work(q)


if __name__ == "__main__":
    socket.timeout(30)

    url_req = urllib.request.Request(url_bleach_home_page)
    url_req.add_header("User-Agent", UA_iphone_6p)
    html_home_page = urllib.request.urlopen(url_req)

    lst = BeautifulSoup(html_home_page, "html.parser").find("div", {"class": "classopen"}).find_all("li")

    html_home_page.close()

    #single processing
    que = queue.Queue()
    for c in lst:
        k = c.find("a").string
        v = url_top_level_domain + c.find("a").get("href")
        que.put_nowait((str(k), str(v)))

    #result = get_job_for_crawler(que)

    _quit = 1
    _force_quit = 1200
    while _quit == 1:
        _quit = get_job_for_crawler(que)
        _force_quit -= 1
        gc.collect()
        if _force_quit <= 0:
            _quit = 0

    if _quit == 0:
       print("Done.")
    else:
        print("Unknown error.")

    print("Finished.")

    #Multiprocessing shared queue which stores URL for each episode
    #:( get banned when using multiprocessing...
    #don't want to use proxy so let's forget multiprocessing and use single processing instead
    '''
    que = Manager().Queue()
    for c in lst:
        k = c.find("a").string
        v = url_top_level_domain + c.find("a").get("href")
        que.put_nowait((str(k), str(v)))
    #Multiprocessing to download each episode
    pool = Pool(6)
    for n in range(1, 7):
        pool.apply_async(get_job_for_crawler, (que,))

    pool.close()
    pool.join()
    '''


















