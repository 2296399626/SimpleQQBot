from flask import Flask,request
import requests
import api
app = Flask(__name__)

class API:
    @staticmethod
    def send(message):
        url = "http://127.0.0.1:5700/send_msg"#这里要加上http://，不然会报错
        data = request.get_json()#获取上报消息
        params = {
            "message_type":data['message_type'],
            "group_id":data['group_id'],
            "message":message
        }
        requests.get(url,params=params)

'''监听端口，获取QQ信息'''
@app.route('/', methods=["POST"])
def post_data():
    '下面的request.get_json().get......是用来获取关键字的值用的，关键字参考上面代码段的数据格式'
    data = request.get_json()
    print(data)
    if request.get_json().get('message_type')=='private':# 如果是私聊信息
        uid = request.get_json().get('sender').get('user_id') # 获取信息发送者的 QQ号码
        message = request.get_json().get('raw_message') # 获取原始信息
        api.keyword(message, uid) # 将 Q号和原始信息传到我们的后台
    elif request.get_json().get('message_type')=='group':# 如果是群聊信息
        gid = request.get_json().get('group_id') # 获取群号
        uid = request.get_json().get('sender').get('user_id') # 获取信息发送者的 QQ号码
        message = request.get_json().get('raw_message') # 获取原始信息
        api.keyword(message, uid, gid) # 将 Q号和原始信息传到我们的后台

    return "OK"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5701)
