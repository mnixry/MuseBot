#!/usr/bin/python
# -*- coding: UTF-8 -*-

# MuseBot
# By:D0OR.TEA
# CreatTime: 2020-11-4
# Msg: love or loved?

print('Program Start')

import os
import re
import time
import json
import _thread
import requests
import webbrowser

from bs4 import BeautifulSoup

# model
import muse_ipc
import muse_cmd
import muse_menu
import muse_ping
import muse_music
import muse_search
import muse_aitalk
import muse_moegirl
import muse_hitokoto
import muse_ipposition
import muse_checkupgrade
# SYS INFO

Version = '0.03'
VersionNickName = 'loved'
Coder = 'D0OR.TEA'
SupportUrl = 'https://github.com/obentnet/MuseBot'

# API
aiTalkAPI = 'https://api.qingyunke.com/api.php?key=free&appid=0&msg='
checkUploadUrl = 'http://106.55.26.167/musebot/nowver.php' 
ipPositionAPIURL = 'https://api.bilibili.com/x/web-interface/zone'
dailyHimgAPIURL = 'https://api.lolicon.app/setu/?r18=1'
baiduSearchAPI = 'https://www.baidu.com/s?ie=UTF-8&wd='
googleSearchAPI = 'https://www.google.com/search?q='
icpQueryUrl = 'http://icp.chinaz.com/home/info?host='

# MuseCodeLogo
def MuseCodeLogo():
    print("""
                  QBB       QBB       QBB     BQv       :BBQBBBB        BBBBBBBBB         
                 1QBr     :XBB       UBB     BB1       BB2   BBB       QQB                
                rQBB:    qBBB       rBB     BBP       BBY   .KU       SBQ                 
               .BBBB.  SEBBB.      .BB.    QBB       .BB5I           7BBBgBBg             
               BBBBD  ZBBBBi       BBi    KBB         ..BBBP        :BB..irr:             
              QB: QBBBD BBs       BBv    sBB             .BB.       BB:                   
             BB5 dBBBQ PBb       MBM    vBB.      rBB    BBJ       BB:                    
            BBB  BBB  QBB        :BB7:qBB         BBM.:iBB5       BBB..ii7.""")
    print("                                                                              V:",Version,'By:',Coder,"")
        

# 基础欢迎
def models():
    print('-'*20)
    print('MuseBot')
    print('-'*20)
    print('v',Version,'by:',Coder)
    print('SupportUrl:',SupportUrl)

# Reboot
def reboot():   # 此功能需要多线程实现
    def reboot_open_new_bot():
        program_path = os.getcwd()
        os.system('python ' + program_path + '\\muse.py')
    def reboot_close_bot():
        os._exit()
    reboot_open_new_bot()
    reboot_close_bot()

# ShutdownBot
def shutdownbot(): 
    while True:
        print('-'*20)
        print('你确定要关闭MuseBot么?')
        chose = input('[y/n]: ')
        if chose == 'y':
            os.system('clear')
            print('正在关闭MuseBot')
            muse_moegirl.main()
            time.sleep(1)
            os._exit()
        elif chose == 'n':
            print('取消关闭')
            break
        else:
            print('???')

# clearCache 清除[__pycache__]缓存
def clearCache():
    fileurl = os.getcwd()
    cacheurl = fileurl+'\\__pycache__'
    print('即将清理:'+cacheurl)
    print('清理完成后,程序将自动重启,是否确定?')
    confirm = input('[y/n]: ')
    if confirm == 'y':
        print('清理中...')
        os.remove(cacheurl)
    elif confirm == 'n':
        print('取消清理')
    else:
        print('你输了些啥')



# about-muse
def aboutmuse():
    os.system('clear')
    MuseCodeLogo()
    print('\n')
    print('~'*10,'% MUSE BOT %','~'*10)
    print('   “智者不入爱河,愚者为情所困.”')
    print('#'*10,'@ 关于系统 @','#'*10)
    print('='*34)
    print('# MuseBot')
    print('当前版本:',Version)

    uploadURL = checkUploadUrl
    newver = requests.get(uploadURL)
    json_str = json.loads(newver.text)

    print('最新版本:',json_str['v'])
    print('当前版本代号:',VersionNickName)
    print('版本作者:',Coder)
    print('支持连接:',SupportUrl)
    print("""
    声明: 此程序为开源程序,可任意修改分发使用,但请不要用作商业用途! 后果自负.
    另如果有更改后分发需求,请务必留下一个著作权.[MuseBot By D0OR.TEA]
    """)
    print('#'*10,'@ 我的故事 @','#'*10)
    print("""
    > 我见到她的第一面,就喜欢上了她...
    > 可她说“我们只能做朋友”....
    Muse,慕涩的恋情。
    代指我在喜欢她的时候，仰慕她，但又羞涩止步于喜欢。。。
    也许是我喜欢的方式不对,又或许是我不够优秀...又或许都是...
    """)

# 读取配置文件
config_path = os.getcwd()+'\\config.json'
content = open(config_path)
config_json_str = json.load(content)
# print(config_json_str['startmews'])

# 主程序运行
os.system('title MuseBot V:'+Version)
MuseCodeLogo() # MUSE LOGO
print('\n')
muse_moegirl.main() # 开机颜文字
os.system('clear') # 前面模组加载完后,清理加载提示

# 判断并执行是否检查更新
if config_json_str['startupgrade'] == True:
    muse_checkupgrade.main() # 检查更新
elif config_json_str['startupgrade'] == False:
    pass
else:
    print('配置文件出错,请检查config.json')
# 检查更新结束

models() # 基础欢迎

# 判断并执行是否输出菜单
if config_json_str['startmenu'] == True:
    muse_menu.main()
elif config_json_str['startmenu'] == False:
    pass
else:
    print('配置文件出错,请检查config.json')

# 让👴来判断你的选择吧
while True:
    # 用户输入
    print('-' * 20)
    user_chose = input('My: ')
    print('-' * 20)
    if user_chose == 'help':
        muse_menu.main()
    elif user_chose == 'aitalk':
        os.system('clear')
        muse_aitalk.aiTalk()
    elif user_chose == 'ip':
        muse_ipposition.main()
    elif user_chose == '':
        pass
    elif user_chose == 'ping':
        muse_ping.main()
    elif user_chose == 'cmd':
        muse_cmd.main()
    elif user_chose == 'setu':
        print('由于接口被反爬处理,该功能被禁用') # 色图功能禁用
    elif user_chose == 'baidu':
        muse_search.baiduSearch()
    elif user_chose == 'google':
        muse_search.googleSearch()
    elif user_chose == 'icp':
        muse_ipc.main()
    elif user_chose == 'netmusic':
        muse_music.main()
    elif user_chose == 'hitokoto':
        muse_hitokoto.main()
    elif user_chose == 'cls':
        os.system('clear')
    elif user_chose == 'upgrade':
        muse_checkupgrade.main()
    elif user_chose == 'reboot':
        reboot()
    elif user_chose == 'shutdown':
        shutdownbot()
    elif user_chose == 'help':
        muse_menu.main()
    elif user_chose == 'about-muse':
        aboutmuse()
    elif user_chose == 'clearcache':
        clearCache()
    elif user_chose == 'well':
        print('well?well what?')
    elif user_chose == '智者不入爱河':
        print('愚者为情所困,作者就是愚者,但可惜的是作者都没有机会变成"愚者"')
    else:
        print("""
        输错了单词?还是想跟我聊聊?
        输入 [help] 来获取命令菜单
        或输 [aitalk] 来获取与我聊天
        """)
