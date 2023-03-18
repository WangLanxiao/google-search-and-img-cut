from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from tqdm import tqdm
import os

savepath='./result_baidu/'
mypaper='./mypaperall.txt'
with open(mypaper, encoding='utf-8') as file:
    content = file.read()
sentences=content.split('.')
NUM=len(sentences)
print('there are ', str(NUM), ' sentences in all.')

begin_id=-1
exit_png=os.listdir(savepath)
if len(exit_png)>0:
    exit_png = sorted(exit_png, key=lambda k: int(k[:-4]))
    begin_id=int(exit_png[-1].split('.')[0])

url='http://www.baidu.com'
option = Options()
option.add_argument('--headless')
option.add_argument('--disable-gpu')

#id=kw是百度输入框的地址，得到输入框的ui元素后输入字
for id,sub_sent in enumerate(tqdm(sentences)):
    if id<=begin_id:
        print(id,'continue')
        continue
    driver = webdriver.Chrome(chrome_options=option)
    driver.get(url)
    # driver.find_element_by_id('kw').send_keys(u'word')
    driver.find_element_by_id('kw').send_keys(sub_sent)
    #id是su的是搜索的按钮，用click方法点击
    driver.find_element_by_id('su').click()
    time.sleep(3)
    client_height = driver.execute_script("return document.body.scrollHeight")
    driver.set_window_size(1680,client_height)
    time.sleep(3)
    #得到页面的快照，留做证明
    driver.save_screenshot(savepath+str(id)+'.png')
    #关闭浏览器
    driver.quit()