import requests
import random
from flask import Flask,request
from main import API
from map_names import map_name_dict

def keyword(message, uid, gid = None):
    if message == "安可":
        return zai(uid, gid)
    if message[0:4] == 'setu':
        setu(uid, gid)
    if message.lower() == "apex":
        apex_getmap(uid,gid)
    

def zai(uid, gid):
    reply = "安可在哦"
    if gid != None: # 如果是群聊信息
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gid, reply))
    else: # 如果是私聊信息
        requests.get(url='http://127.0.0.1:5700/send_private_msg?user_id={0}&message={1}'.format(uid, reply))

def apex_getmap(uid, gid):
    rep_json = requests.get("https://fn.alphaleagues.com/v2/apex/map/").json()
    if rep_json["success"] is not True:
        return
#     requests.get(url='http://127.0.0.1:5700/send_private_msg?user_id={0}&message={1}'.format(uid, rep_json))
    br_map_en = rep_json["br"]["map"].lower()  # 大逃杀的名字英文
    br_map_zh = map_name_dict["br"].get(br_map_en, br_map_en)   # 大逃杀的名字中文
    br_remaining = rep_json["br"]["times"]["remaining"]["minutes"]  # 大逃杀剩余时间

    content = f"""
当前地图
> 大逃杀: {br_map_zh}
剩余时间: {int(br_remaining)}分钟
""".strip()
    if gid != None:
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gid, content))
    else:
        requests.get(url='http://127.0.0.1:5700/send_private_msg?user_id={0}&message={1}'.format(uid, content))

def setu(uid, gid):
    r18 = 0
    num = 1
#     if tag != None:
#         url = 'https://api.lolicon.app/setu/v2?r18=' + r18
#         + '&num=' + num
#         + '&tag=' + tag
#     else url = 'https://api.lolicon.app/setu/v2?r18=' + r18
#         + '&num=' + num
    url = 'https://api.lolicon.app/setu/v2?size=original'
    menu = requests.get(url)
    setu_url = menu.json()['data'][0]['urls']['original'] # 对传回来的涩图网址进行数据提取
    test = 'https://i.pixiv.re/img-original/img/2023/04/18/00/00/18/107277325_p0.jpg'
    if gid != None:
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gid, r'[CQ:image,' r'file=' + setu_url + r']'))
    else:
        requests.get(url='http://127.0.0.1:5700/send_private_msg?user_id={0}&message={1}'.format(uid, r'[CQ:image,' r'file=' + setu_url + r']'))