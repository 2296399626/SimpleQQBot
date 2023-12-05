import requests
import random
from flask import Flask,request
from main import API
import apex_api

def keyword(message, uid, gid = None):
    if message == "安可":
        return zai(uid, gid)
    if message[0:4] == 'setu':
        setu(uid, gid)
    if message.lower() == 'apex':
        apex_getmap(uid, gid)
    elif message[0:1].lower() == 'a':
        apex_getplayers(uid, gid)

def zai(uid, gid):
    reply = "安可在哦"
    if gid != None: # 如果是群聊信息
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gid, reply))
    else: # 如果是私聊信息
        requests.get(url='http://127.0.0.1:5700/send_private_msg?user_id={0}&message={1}'.format(uid, reply))

def apex_getmap(uid, gid):
    content = apex_api.map()
    if gid != None:
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gid, content))
    else:
        requests.get(url='http://127.0.0.1:5700/send_private_msg?user_id={0}&message={1}'.format(uid, content))

def apex_getplayers(uid, gid):
    content = "正在统计，请稍等"
    if gid != None:
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gid, content))
    else:
        requests.get(url='http://127.0.0.1:5700/send_private_msg?user_id={0}&message={1}'.format(uid, content))
    content = apex_api.is_online()
    if gid != None:
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gid, content))
    else:
        requests.get(url='http://127.0.0.1:5700/send_private_msg?user_id={0}&message={1}'.format(uid, content))
#     requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gid, content))

def setu(uid, gid):
    r18 = 0
    num = 1
    url = 'https://api.lolicon.app/setu/v2?size=original'
    menu = requests.get(url)
    setu_url = menu.json()['data'][0]['urls']['original'] # 对传回来的涩图网址进行数据提取
    test = 'https://i.pixiv.re/img-original/img/2023/04/18/00/00/18/107277325_p0.jpg'
    if gid != None:
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gid, r'[CQ:image,' r'file=' + setu_url + r']'))
    else:
        requests.get(url='http://127.0.0.1:5700/send_private_msg?user_id={0}&message={1}'.format(uid, r'[CQ:image,' r'file=' + setu_url + r']'))