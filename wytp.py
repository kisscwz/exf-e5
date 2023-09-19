
```python
import requests
from bs4 import BeautifulSoup
import os

def download_images(url, save_dir):
    # 发送请求获取网页内容
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 创建保存图片的文件夹
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    # 查找所有的图片标签
    img_tags = soup.find_all('img')
    
    # 遍历图片标签，下载图片
    for img_tag in img_tags:
        img_url = img_tag['src']
        img_name = img_url.split('/')[-1]
        save_path = os.path.join(save_dir, img_name)
        
        # 下载图片
        try:
            img_data = requests.get(img_url).content
            with open(save_path, 'wb') as img_file:
                img_file.write(img_data)
            print(f"成功下载图片：{img_name}")
        except:
            print(f"下载图片失败：{img_name}")

# 调用函数，传入要爬取的网页链接和保存图片的文件夹路径
url = "https://example.com"  # 替换为你要爬取的网页链接
save_dir = "images"  # 替换为你要保存图片的文件夹路径
download_images(url, save_dir)
```
