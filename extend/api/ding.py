# encoding:utf-8
"""
 * Created by Arvin.liu on 2018-7-21.
 * QQ 405367236
"""
"""
https://blog.csdn.net/anxiaoyuthss/article/details/71908522
"""
import urllib3
import json


# 源钉云测试
corp_id = 'ding9f3618e7d5c3858035c2f4657eb6378f'
corp_secret = 'rZtkYrpfqDr-kViroug2agaGE8YuwA7zWnCGYoKR0PbChZgZ0A4Z3k4mplwoj9nz'
# 一个钉钉应用的id，以钉钉应用的名义给用户发送消息
agent_id = '181378432'      # 软邦智慧经营测试
# users是用户id列表
users = ['4643562621042451']


def get_access_token():
    url = 'https://oapi.dingtalk.com/gettoken?corpid=%s&corpsecret=%s' % (corp_id, corp_secret)
    request = urllib3.Request(url)
    response = urllib3.urlopen(request)
    response_str = response.read()
    response_dict = json.loads(response_str)
    error_code_key = "errcode"
    access_token_key = "access_token"
    if response_dict.has_key(error_code_key) and response_dict[error_code_key] == 0 and response_dict.has_key(access_token_key):
        return response_dict[access_token_key]
    else:
        return '测试11111111111'


def send_text_to_users(access_token, users, text):
    msg_type, msg = _gen_text_msg(text)
    return _send_msg_to_users(access_token, users, msg_type, msg)


def _gen_text_msg(text):
    msg_type = 'text'
    msg = {"content": text}
    return msg_type, msg


def _send_msg(url, access_token, body):
    posturl = url + access_token
    headers = {'Content-Type': 'application/json'}
    request = urllib3.Request(url=posturl, headers=headers, data=body)
    response = urllib3.urlopen(request)
    resp = response.read()
    print(resp)


def _send_msg_to_users(access_token, users, msg_type, msg):
    to_users = '|'.join(users)
    body_dict = {
        "touser": to_users,
        "agentid": agent_id,
        "msgtype": msg_type
    }
    body_dict[msg_type] = msg
    body = json.dumps(body_dict)
    return _send_msg("https://oapi.dingtalk.com/message/send?access_token=", access_token, body)
