import requests
from apex_name_dict import name_dict
from apex_players import players_dict

def map():
    rep_json = requests.get("https://api.mozambiquehe.re/maprotation? \
        version=2&auth=cd1e42d71971b7fcace210e192a4d48f").json()
    
    br_name = name_to_zn(rep_json["battle_royale"]["current"]["map"])  # 大逃杀的名字
    br_time = rep_json["battle_royale"]["current"]["remainingTimer"]
    br_next = name_to_zn(rep_json["battle_royale"]["next"]["map"])
    
    rank_name =  name_to_zn(rep_json["ranked"]["current"]["map"])
    rank_time = rep_json["ranked"]["current"]["remainingTimer"]
    
    ltm_event = name_to_zn(rep_json["ltm"]["current"]["eventName"])
    ltm_name = name_to_zn(rep_json["ltm"]["current"]["map"])
    ltm_time = rep_json["ltm"]["current"]["remainingTimer"]
    ltm_next_event = name_to_zn(rep_json["ltm"]["next"]["eventName"])
    ltm_next = name_to_zn(rep_json["ltm"]["next"]["map"])
    
    content = f"""
当前地图
> 大逃杀: {br_name}
剩余时间: {br_time}
轮换地图: {br_next}
> 排位赛: {rank_name}
剩余时间: {rank_time}
> 限时模式: {ltm_event}
活动场地: {ltm_name}
剩余时间: {ltm_time}
轮换模式: {ltm_next_event}
轮换地图: {ltm_next}
""".strip()

    print(content)
    return content
    
def name_to_zn(name_en):
    name_zn = name_dict.get(name_en, name_en)   # 大逃杀的名字中文
#     print(name_zn)
    return name_zn

def is_online():
    online_list = []
    for player_name, player_uid in players_dict.items():
        req = f"https://api.mozambiquehe.re/bridge?\
auth=cd1e42d71971b7fcace210e192a4d48f&uid={player_uid}&platform=PC"
        print(req)
        rep_json = requests.get(req).json()
        if rep_json["realtime"]["isOnline"] == 1:
            online_list.append(player_name)
#     print(online_list)
    content = "当前APEX在线玩家"
    if len(online_list) > 0:
        for name in online_list:
            content = content + '\n>' + name
    else:
        content = "当前没有玩家在线"
    print(content)
    return content

# is_online()