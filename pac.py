#仅用于保持活跃
import requests
from selenium import webdriver
import time

for x in range(1, 3):
    wd = webdriver.Chrome(executable_path=r'D:\z\AI\爬虫\爬取工具\chromedriver_win32\chromedriver.exe')
    time.sleep(1)
    wd.get('https://www.pexels.com/search/cat/?page={}'.format(x))
    time.sleep(3)
    imgs = wd.find_elements_by_xpath('//article/a/img')
    for img in imgs:
        url = img.get_attribute('src')
        if url:
            rsp = requests.get(url, verify=False)
            with open('./img/%d.png' %(int(time.time())), 'wb') as f:
                f.write(rsp.content)
    time.sleep(10)
    wd.quit()
