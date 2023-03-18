from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from tqdm import tqdm
import os
from selenium.webdriver.common.by import By

savepath='./result/'
mypaper='./qbl.txt'
with open(mypaper, encoding='utf-8') as file:
    content = file.read()
content=content.replace('\n', '')
content=content.replace('\t', '')
sentences=content.split('.')
NUM=len(sentences)
print('there are ', str(NUM), ' sentences in all.')

begin_id=-1
exit_png=os.listdir(savepath)
if len(exit_png)>0:
    exit_png = sorted(exit_png, key=lambda k: int(k[:-4]))
    begin_id=int(exit_png[-1].split('.')[0])

url='https://www.google.com'
option = Options()
option.add_argument('--headless')
option.add_argument('--disable-gpu')
option.add_argument("--proxy-server=http://127.0.0.1:7890")

for id,sub_sent in enumerate(tqdm(sentences)):
    if id<=begin_id:
        print(id,'continue')
        continue
    else:
        driver = webdriver.Chrome(chrome_options=option)
        driver.get(url)
        time.sleep(0.5)
        driver.find_element_by_name('q').send_keys(sub_sent)
        driver.find_element_by_name('q').send_keys(Keys.ENTER)
        time.sleep(0.5)
        client_height = driver.execute_script("return document.body.scrollHeight")
        driver.set_window_size(1680,client_height)
        time.sleep(0.5)
        #得到页面的快照，留做证明
        driver.save_screenshot(savepath+str(id)+'.png')
        #关闭浏览器
        driver.quit()