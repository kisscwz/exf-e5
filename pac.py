import requests
# pip install selenium
from selenium import webdriver
import time

for x in range(1, 3):
    # 打开浏览器，用chromedriver.exe插件
    wd = webdriver.Chrome(executable_path=r'D:\z\AI\爬虫\爬取工具\chromedriver_win32\chromedriver.exe')
    time.sleep(1)
    # 访问某个网址
    wd.get('https://www.pexels.com/search/cat/?page={}'.format(x))
    time.sleep(3)
    # 根据xpath的语法，一次性查找多个img标签
    imgs = wd.find_elements_by_xpath('//article/a/img')
    for img in imgs:
        # 根据标签的属性来获取某个值
        url = img.get_attribute('src')
        if url:
            # verify，因为是https请求，verify=False，不进行ssl安全认证
            rsp = requests.get(url, verify=False)
            # ./，指当前目录
            with open('./img/%d.png' %(int(time.time())), 'wb') as f:
                # 将响应内容转换成二进制内容
                f.write(rsp.content)
    time.sleep(10)
    # 退出浏览器
    wd.quit()
————————————————
版权声明：本文为CSDN博主「王挣银」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_29960631/article/details/120027355
