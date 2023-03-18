需要配合谷歌浏览器使用，按照谷歌浏览器的版本去下面的链接下载驱动
https://chromedriver.chromium.org/downloads
https://chromedriver.storage.googleapis.com/index.html
下载win32解压得到一个exe文件，放在编译器python的同目录下即可，我是直接用的anaconda3目录下的python.exe。

所以就放在这里了 C:\ProgramData\Anaconda3\chromedriver.exe


输入论文在mypaper.txt
输出截图在result
按英文句号进行的划分，建议第一次使用debug到这里看一眼比较稳妥。

百度搜索更加稳定

使用谷歌搜索，需要开启VPN 并且存在中间网络问题被迫中止的情况，如果中断需要手工修改begin_id符号。
也可以在代码中指定VPN的IP option.add_argument("--proxy-server=http://127.0.0.1:7890") （全局开启，可以把这一行注释掉）

如果网络error中断了，可以看下保存的result卡在哪里，修改begin_id即可。

页面大小调整：
driver.set_window_size(1680,client_height)

